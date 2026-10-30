"""HTTP access to PyPI, retried on transient failures."""

from __future__ import annotations

import functools
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

RETRIES = 5
RETRY_ON = [429, 500, 502, 503, 504]
# Waits 0.4, 0.8, 1.6 and 3.2 s between retries (urllib3 does not wait before the
# first), so a brief outage does not use up every retry at once.
BACKOFF_FACTOR = 0.2
TIMEOUT = 3
# For sdist downloads. A read timeout limits inactivity, not the whole transfer,
# so a large download only fails here if the server stops sending.
DOWNLOAD_TIMEOUT = 60


@functools.cache
def _session() -> requests.Session:
    # Connection errors (including TLS EOFs) and the statuses in RETRY_ON are
    # retried. After the last retry the final response is returned rather than
    # raised, so callers still see the status code and report it themselves.
    retry_strategy = Retry(
        total=RETRIES,
        status_forcelist=RETRY_ON,
        backoff_factor=BACKOFF_FACTOR,
        raise_on_status=False,
    )
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def pypi_get(url: str, **kwargs: Any) -> requests.Response:
    """GET a URL on PyPI, retrying transient failures."""
    kwargs.setdefault("timeout", TIMEOUT)
    return _session().get(url, **kwargs)
