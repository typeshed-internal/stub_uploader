"""
Find the latest typeshed increment for a stub package with given
(or current) version.

If the given version was never uploaded, this will return -1. See
https://github.com/python/typeshed/blob/main/README.md for details
on stub versioning.

This file also contains some helper functions related to querying
distribution information.
"""

from __future__ import annotations

from typing import Any

import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from stub_uploader.const import TYPES_PREFIX
from stub_uploader.metadata import Metadata

URL_TEMPLATE = "https://pypi.org/pypi/{}/json"
RETRIES = 5
RETRY_ON = [429, 500, 502, 503, 504]
TIMEOUT = 3


def fetch_pypi_versions(distribution: str) -> list[Version]:
    assert distribution.startswith(TYPES_PREFIX)
    url = URL_TEMPLATE.format(distribution)
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
    return [Version(release) for release in releases.keys()]


def ensure_specificity(ver: list[int], specificity: int) -> None:
    ver.extend([0] * (specificity - len(ver)))


def compute_incremented_version(
    version_spec: str, published_versions: list[Version]
) -> Version:
    # The most important postcondition is that the incremented version is greater than
    # all published versions. This ensures that users who don't pin get the most
    # up to date stub. If we ever maintain multiple versions for a stub, this will
    # need revisiting.
    max_published = max(published_versions, default=Version("0"))

    # The second thing we try to do (but don't guarantee), is that the incremented
    # version will satisfy the version_spec (defined precisely by the `compatible`
    # specifier below). This allows users to have expectations of what a stub package
    # will contain based on the upstream version they're targeting.
    if version_spec.endswith(".*"):
        compatible = SpecifierSet(f"=={version_spec}")
    else:
        compatible = SpecifierSet(f"=={version_spec}.*")

    # Look up the base version and specificity in METADATA.toml.
    version_base = Version(version_spec.removesuffix(".*"))
    specificity = len(version_base.release)

    if max_published.epoch > 0 or version_base.epoch > 0:
        raise NotImplementedError("Epochs in versions are not supported")

    # We'll try to bump the fourth part of the release. So e.g. if our version_spec is
    # 1.1, we'll release 1.1.0.0, 1.1.0.1, 1.1.0.2, ...
    # But if our version_spec is 5.6.7.8, we'll release 5.6.7.8.0, 5.6.7.8.1, ...
    increment_specificity = max(specificity + 1, 4)

    if version_base.release < max_published.release[:specificity]:
        # Our published versions have gone too far ahead the upstream version
        # So we can't guarantee our second property.
        # In practice, this will only happen if the specificity of version_spec is
        # changed or we change our versioning scheme.
        # For example, version_base=1.2, max_published=1.3.0.4, return 1.3.0.5
        increment_specificity = max(increment_specificity, len(max_published.release))
        incremented = list(max_published.release)
        ensure_specificity(incremented, increment_specificity)
        incremented[-1] += 1

        incremented_version = Version(".".join(map(str, incremented)))
        assert incremented_version > max_published
        # But can't keep versioning compatible with upstream...
        assert incremented_version not in compatible
        return incremented_version

    if version_base.release > max_published.release[:specificity]:
        # For example, version_base=1.2, max_published=1.1.0.4, return 1.2.0.0
        incremented = list(version_base.release)
        ensure_specificity(incremented, increment_specificity)

    else:
        assert version_base.release == max_published.release[:specificity]
        # For example, version_base=1.1, max_published=1.1.0.4, return 1.1.0.5
        incremented = list(max_published.release)
        ensure_specificity(incremented, increment_specificity)
        incremented[-1] += 1

    incremented_version = Version(".".join(map(str, incremented)))
    assert incremented_version > max_published
    assert incremented_version in compatible
    return incremented_version


def determine_incremented_version(metadata: Metadata) -> str:
    published_stub_versions = fetch_pypi_versions(metadata.stub_distribution)
    version = compute_incremented_version(
        metadata.version_spec, published_stub_versions
    )
    return str(version)
