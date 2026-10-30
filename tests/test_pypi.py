from __future__ import annotations

import socket
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
from packaging.requirements import Requirement

from stub_uploader import metadata
from stub_uploader.pypi import (
    BACKOFF_FACTOR,
    DOWNLOAD_TIMEOUT,
    RETRIES,
    _session,
    pypi_get,
)


class FlakyHandler(BaseHTTPRequestHandler):
    """Fails the first `failures` requests in the given way, then answers 200."""

    failures = 0
    mode = "503"
    hits = 0

    def do_GET(self) -> None:
        cls = type(self)
        cls.hits += 1
        if cls.hits <= cls.failures:
            if cls.mode == "drop":
                # Close without a response, like a TLS EOF mid-handshake.
                self.connection.shutdown(socket.SHUT_RDWR)
                return
            self.send_response(503)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok": true}')

    def log_message(self, format: str, *args: object) -> None:
        pass


@pytest.fixture(autouse=True)
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Record urllib3's backoff sleeps instead of waiting for them."""
    recorded: list[float] = []
    monkeypatch.setattr("urllib3.util.retry.time.sleep", recorded.append)
    return recorded


@pytest.fixture
def server() -> Iterator[str]:
    FlakyHandler.hits = 0
    httpd = HTTPServer(("127.0.0.1", 0), FlakyHandler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}/pypi/example/json"
    httpd.shutdown()
    httpd.server_close()


def test_retries_transient_status(server: str) -> None:
    FlakyHandler.failures, FlakyHandler.mode = 2, "503"
    resp = pypi_get(server)
    assert resp.status_code == 200
    assert resp.json() == {"ok": True}
    assert FlakyHandler.hits == 3


def test_retries_dropped_connection(server: str) -> None:
    FlakyHandler.failures, FlakyHandler.mode = 2, "drop"
    assert pypi_get(server).status_code == 200
    assert FlakyHandler.hits == 3


def test_returns_last_response_when_retries_run_out(
    server: str, sleeps: list[float]
) -> None:
    FlakyHandler.failures, FlakyHandler.mode = 100, "503"
    resp = pypi_get(server)
    assert resp.status_code == 503
    assert FlakyHandler.hits == RETRIES + 1
    # urllib3 does not wait before the first retry, then backs off exponentially.
    assert sleeps == [BACKOFF_FACTOR * 2**n for n in range(1, RETRIES)]


def test_session_is_shared() -> None:
    assert _session() is _session()


def test_sdist_download_has_a_finite_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    seen: dict[str, object] = {}

    def fake_get(url: str, **kwargs: object) -> object:
        seen.update(kwargs)
        raise RuntimeError("stop after the request")

    monkeypatch.setattr(metadata, "pypi_get", fake_get)
    with pytest.raises(RuntimeError):
        metadata.temp_archive_path(
            {"filename": "x.tar.gz", "url": "https://example.invalid/x.tar.gz"},
            Requirement("x"),
        )
    assert seen["timeout"] == DOWNLOAD_TIMEOUT
