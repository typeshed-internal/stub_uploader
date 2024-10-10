from __future__ import annotations

import functools
import graphlib
import os
import re
import tarfile
import urllib.parse
from collections.abc import Generator, Iterable
from glob import glob
from pathlib import Path
import tempfile
from typing import Any, Optional

import requests
import tomli
from packaging.requirements import Requirement
from packaging.specifiers import Specifier, InvalidSpecifier

from .const import META, THIRD_PARTY_NAMESPACE, TYPES_PREFIX, UPLOADED_PATH


class InvalidRequires(Exception):
    pass


class Metadata:
    def __init__(self, distribution: str, data: dict[str, Any]):
        assert not distribution.startswith(TYPES_PREFIX)
        self._alleged_upstream_distribution = distribution
        self.data = data

    @property
    def upstream_distribution(self) -> Optional[str]:
        # TODO: add a field to METADATA.toml if the stubs are for a package
        # that does not exist on PyPI
        if self._alleged_upstream_distribution == "gdb":
            return None
        return self._alleged_upstream_distribution

    @property
    def stub_distribution(self) -> str:
        distribution = self.data.get(
            "stub_distribution", TYPES_PREFIX + self._alleged_upstream_distribution
        )
        assert isinstance(distribution, str)
        return distribution

    @property
    def version_spec(self) -> Specifier:
        # The "version" field in METADATA.toml isn't actually a version, it's more
        # like a specifier, e.g. we allow it to contain wildcards.
        version = self.data["version"]
        assert isinstance(version, str)
        if version[0].isdigit():
            version = f"=={version}"
        spec = Specifier(version)
        assert spec.operator in {"==", "~="}
        return spec

    @property
    def _unvalidated_requires(self) -> list[Requirement]:
        return [Requirement(req) for req in self.data.get("requires", [])]

    @property
    def _unvalidated_requires_typeshed(self) -> list[Requirement]:
        typeshed = uploaded_packages.read()
        return [
            r for r in self._unvalidated_requires if canonical_name(r.name) in typeshed
        ]

    @functools.cached_property
    def requires_typeshed(self) -> list[Requirement]:
        reqs = self._unvalidated_requires_typeshed
        for req in reqs:
            verify_typeshed_req(req)
        return reqs

    @property
    def _unvalidated_requires_external(self) -> list[Requirement]:
        typeshed = uploaded_packages.read()
        return [
            r
            for r in self._unvalidated_requires
            if canonical_name(r.name) not in typeshed
        ]

    @functools.cached_property
    def requires_external(self) -> list[Requirement]:
        reqs = self._unvalidated_requires_external
        for req in reqs:
            verify_external_req(req, self.upstream_distribution)
        return reqs

    @property
    def extra_description(self) -> str:
        description = self.data.get("extra_description", "")
        assert isinstance(description, str)
        return description

    @property
    def obsolete_since(self) -> str | None:
        obsolete = self.data.get("obsolete_since")
        assert isinstance(obsolete, (str, type(None)))
        return obsolete

    @property
    def no_longer_updated(self) -> bool:
        updated = self.data.get("no_longer_updated", False)
        assert isinstance(updated, bool)
        return updated

    @property
    def upload(self) -> bool:
        upload = self.data.get("upload", True)
        assert isinstance(upload, bool)
        return upload

    @property
    def partial(self) -> bool:
        partial = self.data.get("partial_stub", False)
        assert isinstance(partial, bool)
        return partial

    @property
    def requires_python(self) -> str | None:
        req = self.data.get("requires_python", None)
        assert isinstance(req, (str, type(None)))
        verify_requires_python(req)
        return req

    @functools.cached_property
    def upstream_repository(self) -> str | None:
        ts_upstream_repo = self.data.get("upstream_repository")
        if not isinstance(ts_upstream_repo, str):
            # either typeshed doesn't list it for these stubs,
            # or it gives a non-str for the field (bad!)
            return None
        try:
            parsed_url = urllib.parse.urlsplit(ts_upstream_repo)
        except ValueError:
            return None
        if parsed_url.scheme != "https":
            return None
        return ts_upstream_repo


def read_metadata(typeshed_dir: str, distribution: str) -> Metadata:
    """Parse metadata from file."""
    assert not distribution.startswith(TYPES_PREFIX)
    path = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution, META)
    with open(path, "rb") as f:
        data = tomli.load(f)
    return Metadata(distribution=distribution, data=data)


def canonical_name(name: str) -> str:
    # https://peps.python.org/pep-0503/#normalized-names
    return re.sub(r"[-_.]+", "-", name).lower()


class _UploadedPackages:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._cached: Optional[list[str]] = None

    def read(self) -> set[str]:
        if self._cached is not None:
            return set(map(canonical_name, self._cached))
        with open(self._file_path) as f:
            self._cached = f.read().splitlines()
        return set(map(canonical_name, self._cached))

    def add(self, distribution: str) -> None:
        assert not distribution.startswith(TYPES_PREFIX)
        stub_dist = TYPES_PREFIX + distribution
        if canonical_name(stub_dist) not in self.read():
            with open(self._file_path) as f:
                current = f.read().splitlines()
            current.append(stub_dist)
            current.sort()
            with open(self._file_path, "w") as f:
                f.write("\n".join(current))
            self._cached = None


uploaded_packages = _UploadedPackages(UPLOADED_PATH)


def strip_types_prefix(dependency: str) -> str:
    if not dependency.startswith(TYPES_PREFIX):
        raise ValueError("Expected dependency on a typeshed package")
    return dependency.removeprefix(TYPES_PREFIX)


def verify_typeshed_req(req: Requirement) -> None:
    if not req.name.startswith(TYPES_PREFIX):
        raise InvalidRequires(f"Expected dependency {req} to start with {TYPES_PREFIX}")

    if not canonical_name(req.name) in uploaded_packages.read():
        raise InvalidRequires(
            f"Expected dependency {req} to be uploaded from stub_uploader"
        )

    # TODO: make sure that if a typeshed distribution depends on other typeshed stubs,
    # the upstream depends on the upstreams corresponding to those stubs.
    # See https://github.com/typeshed-internal/stub_uploader/pull/61#discussion_r979327370


# Presence in the top 1000 PyPI packages could be a necessary but not sufficient criterion for
# inclusion in this allowlist.
# Note we could loosen our criteria once we address:
# https://github.com/typeshed-internal/stub_uploader/pull/61#discussion_r979327370
EXTERNAL_REQ_ALLOWLIST = {
    "Flask",
    "Flask-SQLAlchemy",
    "MarkupSafe",
    "Pillow",
    "Werkzeug",
    "arrow",
    "backports.zoneinfo",  # Remove after we drop Python 3.8 support.
    "click",
    "cryptography",
    "django-stubs",
    "djangorestframework-stubs",
    "matplotlib",
    "numpy",
    "pandas-stubs",
    "referencing",
    "setuptools",
    "torch",
    "tree-sitter",
    "urllib3",
}


def validate_response(resp: requests.Response, req: Requirement) -> None:
    if resp.status_code != 200:
        raise InvalidRequires(
            f"Expected dependency {req} to be accessible on PyPI, but got {resp.status_code}"
        )


def extract_sdist_requires(
    sdist_data: dict[str, str], req: Requirement
) -> Generator[Requirement, None, None]:
    tmpdir = tempfile.mkdtemp()
    archive_path = Path(tmpdir, sdist_data["filename"])

    resp = requests.get(sdist_data["url"], stream=True)
    validate_response(resp, req)
    with open(archive_path, "wb") as file:
        file.write(resp.raw.read())

    with tarfile.open(archive_path) as file_in:
        if hasattr(tarfile, "data_filter"):
            file_in.extraction_filter = tarfile.data_filter
        file_in.extractall(tmpdir)

    # Only a single folder with "<package-version>.egg-info/requires.txt" in the archive should exist
    # but this supports possible edge-cases and doesn't require knowing any variable name in the path.
    requires_filepath = Path(tmpdir, "*", "*.egg-info", "requires.txt")
    matches = glob(str(requires_filepath))
    for match in matches:
        with open(match) as requires_file:
            lines = requires_file.readlines()
        for line in lines:
            # Skip empty lines and extras
            if line[0] not in {"\n", "["}:
                yield Requirement(line)


def verify_external_req(
    req: Requirement,
    upstream_distribution: Optional[str],
    _unsafe_ignore_allowlist: bool = False,  # used for tests
) -> None:
    req_canonical_name = canonical_name(req.name)

    if req_canonical_name in uploaded_packages.read():
        raise InvalidRequires(
            f"Expected dependency {req} to not be uploaded from stub_uploader"
        )
    if req.name.startswith(TYPES_PREFIX):
        # technically this could be allowed, but it's very suspicious
        raise InvalidRequires(
            f"Expected dependency {req} to not start with {TYPES_PREFIX}"
        )

    if upstream_distribution is None:
        raise InvalidRequires(
            f"There is no upstream distribution on PyPI, so cannot verify {req}"
        )

    if req.name not in EXTERNAL_REQ_ALLOWLIST and not _unsafe_ignore_allowlist:
        raise InvalidRequires(
            f"Expected dependency {req.name} to be present in the stub_uploader allowlist"
        )

    resp = requests.get(f"https://pypi.org/pypi/{upstream_distribution}/json")
    validate_response(resp, req)
    data: dict[str, Any] = resp.json()

    # TODO: PyPI doesn't seem to have version specific requires_dist. This does mean we can be
    # broken by new releases of upstream packages, even if they do not match the version spec we
    # have for the upstream distribution.

    if req_canonical_name in [
        canonical_name(Requirement(r).name)
        for r in (data["info"].get("requires_dist") or [])
    ]:
        return  # Ok!

    sdist_data: dict[str, Any] | None = next(
        (
            url_data
            for url_data in reversed(data["urls"])
            if url_data["packagetype"] == "sdist"
        ),
        None,
    )
    if not (
        sdist_data
        and req_canonical_name
        in [canonical_name(r.name) for r in extract_sdist_requires(sdist_data, req)]
    ):
        raise InvalidRequires(
            f"Expected dependency {req} to be listed in {upstream_distribution}'s "
            + "requires_dist or the sdist's *.egg-info/requires.txt"
        )


def sort_by_dependency(
    typeshed_dir: str, distributions: Iterable[str]
) -> Generator[str, None, None]:
    # Just a simple topological sort. Unlike previous versions of the code, we do not rely
    # on this to perform validation, like requiring the graph to be complete.
    # We only use this to help with edge cases like multiple packages being uploaded
    # for the first time that depend on each other.
    ts: graphlib.TopologicalSorter[str] = graphlib.TopologicalSorter()

    dist_map: dict[str, str] = {}  # maps stub distribution name to directory name
    for dist in os.listdir(os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE)):
        metadata = read_metadata(typeshed_dir, dist)
        ts.add(
            metadata.stub_distribution,
            # Use _unvalidated_requires instead of requires_typeshed, in case we're uploading
            # a new package B that depends on another new package A. Sorting topologically means
            # that the A will be in uploaded_packages.txt by the time it comes to verify and
            # upload B.
            *[r.name for r in metadata._unvalidated_requires],
        )
        dist_map[metadata.stub_distribution] = dist

    # ts.static_order may contain external dependencies, so we filter them out
    ordered = [
        dist_map[stub_dist] for stub_dist in ts.static_order() if stub_dist in dist_map
    ]

    distributions = set(distributions)
    missing = distributions - set(ordered)
    assert not missing, f"Failed to find distributions {missing}"

    for dist in ordered:
        if dist in distributions:
            yield dist


def recursive_verify(metadata: Metadata, typeshed_dir: str) -> set[str]:
    # While metadata.requires_typeshed and metadata.requires_external will perform validation on the
    # stub distribution itself, it seems useful to be able to validate the transitive typeshed
    # dependency graph for a stub distribution
    _verified: set[str] = set()

    def _verify(metadata: Metadata) -> None:
        if metadata.stub_distribution in _verified:
            return
        _verified.add(metadata.stub_distribution)

        # calling these checks metadata's requires
        assert isinstance(metadata.requires_typeshed, list)
        assert isinstance(metadata.requires_external, list)

        # and recursively verify all our internal dependencies as well
        for req in metadata.requires_typeshed:
            _verify(read_metadata(typeshed_dir, strip_types_prefix(req.name)))

    _verify(metadata)
    return _verified


def verify_requires_python(requires_python: str | None) -> None:
    if requires_python is None:
        return
    try:
        specifier = Specifier(requires_python)
    except InvalidSpecifier as e:
        raise InvalidRequires(
            f"Invalid requires_python specifier: {requires_python}"
        ) from e
    if specifier.operator != ">=":
        raise InvalidRequires(
            f"Expected requires_python to be a '>=' specifier: {requires_python}"
        )
