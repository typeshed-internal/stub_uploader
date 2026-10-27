"""HTTP access to PyPI, retried on transient failures."""

from __future__ import annotations

import functools
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

RETRIES = 5
RETRY_ON = [429, 500, 502, 503, 504]
TIMEOUT = 3


@functools.cache
def _session() -> requests.Session:
    # Connection errors (including TLS EOFs) and the statuses in RETRY_ON are
    # retried. After the last retry the final response is returned rather than
    # raised, so callers still see the status code and report it themselves.
    retry_strategy = Retry(
        total=RETRIES, status_forcelist=RETRY_ON, raise_on_status=False
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
