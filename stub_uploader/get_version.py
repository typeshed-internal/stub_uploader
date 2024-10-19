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
import datetime

from typing import Any

import requests
from packaging.specifiers import Specifier, SpecifierSet
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


# `today` can be passed as an argument for testing purposes.
def compute_stub_version(
    version_spec: Specifier, published_versions: list[Version], today: datetime.date
) -> Version:
    # The most important postcondition is that the incremented version is greater than
    # all published versions. This ensures that users who don't pin get the most
    # up to date stub. If we ever maintain multiple versions for a stub, this will
    # need revisiting.
    max_published = max(published_versions, default=Version("0"))

    # Parse and massage the base version if necessary. Usually, the base version is
    # just the version_spec without any trailing `.*`. But if the version_spec is a
    # post version, we append the post version to the base version:
    #   1.2.post3 -> 1.2.3
    # This is necessary, since structured post versions (e.g. `1.2.post3.4`) are not
    # supported by PEP 440.
    version_base = Version(version_spec.version.removesuffix(".*"))
    if max_published.epoch > 0 or version_base.epoch > 0:
        raise NotImplementedError("Epochs in versions are not supported")
    elif version_base.is_prerelease or version_base.is_devrelease:
        raise NotImplementedError("Pre- and dev-releases in versions are not supported")
    elif version_base.is_postrelease:
        version_base = Version(f"{version_base.base_version}.{version_base.post}")

    # Usually, the new version should satisfy the version_spec (defined precisely by
    # the `compatible` specifier in `assert_compatibility()`). This allows users to
    # have expectations of what a stub package will contain based on the upstream
    # version they're targeting.
    is_compatible = True

    # We'll try to bump the fourth part of the release. So e.g. if our version_spec is
    # 1.1, we'll release 1.1.0.YYYYMMDD. But if our version_spec is 5.6.7.8, we'll
    # release 5.6.7.8.YYYYMMDD.
    specificity = len(version_base.release)
    stub_specificity = max(specificity + 1, 4)

    if version_base.release < max_published.release[:specificity]:
        # Our published versions have gone too far ahead the upstream version
        # So we can't guarantee our second property.
        # In practice, this will only happen if the specificity of version_spec is
        # changed or we change our versioning scheme.
        # For example, version_base=1.2, max_published=1.3.0.4, return 1.3.0.YYYYMMDD
        stub_specificity = max(stub_specificity, len(max_published.release))
        base_version_parts = list(max_published.release)

        # But can't keep versioning compatible with upstream...
        is_compatible = False
        # We also use the latest stub version as the base version, not the version_spec.
        base_version_changed = False

    elif version_base.release > max_published.release[:specificity]:
        # For example, version_base=1.2, max_published=1.1.0.4, return 1.2.0.YYYYMMDD
        base_version_parts = list(version_base.release)
        base_version_changed = True

    else:
        assert version_base.release == max_published.release[:specificity]
        # For example, version_base=1.1, max_published=1.1.0.YYYYMMDD (old),
        # return 1.1.0.YYYYMMDD (today)
        base_version_parts = list(max_published.release)
        base_version_changed = False

    ensure_specificity(base_version_parts, stub_specificity)
    unused_date = find_unused_date(max_published, base_version_changed, today)
    new_version_parts = [*base_version_parts[:-1], unused_date.strftime("%Y%m%d")]
    new_version = Version(".".join(map(str, new_version_parts)))
    assert_compatibility(
        version_base=version_base, new_version=new_version, is_compatible=is_compatible
    )
    assert (
        new_version > max_published
    ), f"new version {new_version} <= published version {max_published}"
    return new_version


# `today` can be passed as an argument for testing purposes.
def find_unused_date(
    max_published: Version, base_version_changed: bool, today: datetime.date
) -> datetime.date:
    # Is not necessarily a date in case the package predates the switch
    # to the current versioning scheme.
    last_date = max_published.release[-1]

    # If the base version changed, we should always be able to use the current date.
    if base_version_changed:
        return today

    # Make sure that the last published release is not unreasonable large.
    assert int(today.strftime("%Y%m%d")) + 14 > last_date

    new_date = today
    while int(new_date.strftime("%Y%m%d")) <= last_date:
        new_date += datetime.timedelta(days=1)
    return new_date


def assert_compatibility(
    *, version_base: Version, new_version: Version, is_compatible: bool
) -> None:
    compatible = SpecifierSet(f"=={version_base.base_version}.*")
    if is_compatible:
        assert new_version in compatible
    else:
        assert new_version not in compatible


def determine_stub_version(metadata: Metadata) -> str:
    today = datetime.datetime.now(datetime.UTC).date()
    published_stub_versions = fetch_pypi_versions(metadata.stub_distribution)
    version = compute_stub_version(
        metadata.version_spec, published_stub_versions, today
    )
    return str(version)
