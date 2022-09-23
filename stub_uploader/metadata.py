from __future__ import annotations

import functools
import graphlib
import os
import re
from typing import Any, Dict, Iterator, Optional

import requests
import tomli
from packaging.requirements import Requirement

from .const import META, THIRD_PARTY_NAMESPACE, TYPES_PREFIX, UPLOADED_PATH


class InvalidRequires(Exception):
    pass


class Metadata:
    def __init__(self, distribution: str, data: Dict[str, Any]):
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
        return TYPES_PREFIX + self._alleged_upstream_distribution

    @property
    def version_spec(self) -> str:
        # The "version" field in METADATA.toml isn't actually a version, it's more
        # like a specifier, e.g. we allow it to contain wildcards.
        version = self.data["version"]
        assert isinstance(version, str)
        return version

    @property
    def _unvalidated_requires(self) -> list[Requirement]:
        return [Requirement(req) for req in self.data.get("requires", [])]

    @property
    def _unvalidated_requires_typeshed(self) -> list[Requirement]:
        return [
            r
            for r in self._unvalidated_requires
            if canonical_name(r.name) in uploaded_packages.read()
        ]

    @functools.cached_property
    def requires_typeshed(self) -> list[Requirement]:
        reqs = self._unvalidated_requires_typeshed
        for req in reqs:
            verify_typeshed_req(req)
        return reqs

    @property
    def _unvalidated_requires_external(self) -> list[Requirement]:
        return [
            r
            for r in self._unvalidated_requires
            if canonical_name(r.name) not in uploaded_packages.read()
        ]

    @functools.cached_property
    def requires_external(self) -> list[Requirement]:
        reqs = self._unvalidated_requires_external
        for req in reqs:
            verify_external_req(req, self.upstream_distribution)
        return reqs

    @property
    def extra_description(self) -> str:
        return self.data.get("extra_description", "")

    @property
    def obsolete_since(self) -> Optional[str]:
        return self.data.get("obsolete_since")

    @property
    def no_longer_updated(self) -> bool:
        return self.data.get("no_longer_updated", False)


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


def verify_external_req(req: Requirement, upstream_distribution: Optional[str]) -> None:
    if canonical_name(req.name) in uploaded_packages.read():
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

    resp = requests.get(f"https://pypi.org/pypi/{upstream_distribution}/json")
    if resp.status_code != 200:
        raise InvalidRequires(
            f"Expected dependency {req} to be accessible on PyPI, but got {resp.status_code}"
        )

    data = resp.json()

    # TODO: allow external dependencies for stubs for packages that do not ship wheels
    if req.name not in [
        Requirement(r).name for r in (data["info"].get("requires_dist") or [])
    ]:
        raise InvalidRequires(
            f"Expected dependency {req} to be listed in {upstream_distribution}'s requires_dist"
        )


def sort_by_dependency(typeshed_dir: str, distributions: list[str]) -> Iterator[str]:
    # Just a simple topological sort. Unlike previous versions of the code, we do not rely
    # on this to perform validation, like requiring the graph to be complete.
    # We only use this to help with edge cases like multiple packages being uploaded
    # for the first time that depend on each other.
    ts: graphlib.TopologicalSorter[str] = graphlib.TopologicalSorter()

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

    for dist in ts.static_order():
        dist = strip_types_prefix(dist)
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
