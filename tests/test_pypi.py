from __future__ import annotations

import socket
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from stub_uploader.pypi import RETRIES, _session, pypi_get


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


def test_returns_last_response_when_retries_run_out(server: str) -> None:
    FlakyHandler.failures, FlakyHandler.mode = 100, "503"
    resp = pypi_get(server)
    assert resp.status_code == 503
    assert FlakyHandler.hits == RETRIES + 1


def test_session_is_shared() -> None:
    assert _session() is _session()
