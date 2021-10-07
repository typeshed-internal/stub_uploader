"""
Find the latest typeshed increment for a stub package with given
(or current) version.

If the given version was never uploaded, this will return -1. See
https://github.com/python/typeshed/blob/master/README.md for details
on stub versioning.

This file also contains some helper functions related to querying
distribution information.
"""

from __future__ import annotations

import argparse
import os.path
import re
from collections.abc import Iterable
from typing import Any, Optional, cast

import requests
import toml
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry  # type: ignore[import]

from scripts.const import *

PREFIX = "types-"
URL_TEMPLATE = "https://pypi.org/pypi/{}/json"
RETRIES = 5
RETRY_ON = [429, 500, 502, 503, 504]
TIMEOUT = 3


def fetch_pypi_versions(distribution: str) -> Iterable[str]:
    url = URL_TEMPLATE.format(PREFIX + distribution)
    retry_strategy = Retry(total=RETRIES, status_forcelist=RETRY_ON)
    with requests.Session() as session:
        session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        resp = session.get(url, timeout=TIMEOUT)
    if not resp.ok:
        if resp.status_code == 404:
            # Looks like this is first time this package is ever uploaded.
            return []
        raise ValueError("Error while retrieving version")
    releases: dict[str, Any] = resp.json()["releases"]
    return releases.keys()


def read_base_version(typeshed_dir: str, distribution: str) -> str:
    """Read distribution version from metadata."""
    metadata_file = os.path.join(
        typeshed_dir, THIRD_PARTY_NAMESPACE, distribution, "METADATA.toml"
    )
    with open(metadata_file) as f:
        data = toml.loads(f.read())
    version = data["version"]
    assert isinstance(version, str)
    if version.endswith(".*"):
        version = version[:-2]
    assert re.match(r"\d+(\.\d+)*", version)
    return version


def strip_dep_version(dependency: str) -> str:
    """Strip a possible version suffix, e.g. types-six>=0.1.4 -> types-six."""
    dep_version_pos = len(dependency)
    for pos, c in enumerate(dependency):
        if c in "=<>":
            dep_version_pos = pos
            break
    return dependency[:dep_version_pos]


def check_exists(distribution: str) -> bool:
    """Check if any version of this *stub* distribution has ben ever uploaded."""
    url = URL_TEMPLATE.format(distribution)
    retry_strategy = Retry(total=RETRIES, status_forcelist=RETRY_ON)
    with requests.Session() as session:
        session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        resp = session.get(url, timeout=TIMEOUT)
    if resp.ok:
        return True
    if resp.status_code == 404:
        return False
    raise ValueError("Error while verifying existence")


def main(typeshed_dir: str, distribution: str, version: Optional[str]) -> int:
    """A simple function to get version increment of a third-party stub package.

    Supports basic reties and timeouts (as module constants).
    """
    pypi_versions = fetch_pypi_versions(distribution)
    if not version:
        # Use the METADATA.toml version, if not given one.
        version = read_base_version(typeshed_dir, distribution)
    matching = [v for v in pypi_versions if v.startswith(f"{version}.")]
    if not matching:
        return -1
    increment = max(int(v.split(".")[-1]) for v in matching)
    return increment


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument(
        "version", nargs="?", help="Base version for which to get increment"
    )
    args = parser.parse_args()
    print(main(args.typeshed_dir, args.distribution, args.version))
