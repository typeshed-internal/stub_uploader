"""
Integration tests for build scripts. These should not change
anything on PyPI, but can make PyPI queries and may expect
a typeshed checkout side by side.
"""
import os

import pytest
from packaging.requirements import Requirement
from packaging.version import Version

from stub_uploader import build_wheel, get_version
from stub_uploader.const import THIRD_PARTY_NAMESPACE
from stub_uploader.metadata import (
    InvalidRequires,
    Metadata,
    read_metadata,
    recursive_verify,
    sort_by_dependency,
    strip_types_prefix,
    verify_external_req,
    verify_typeshed_req,
)

TYPESHED = "../typeshed"


def test_fetch_pypi_versions() -> None:
    """Check that we can query PyPI for package increments."""
    assert Version("1.16.0") in get_version.fetch_pypi_versions("types-six")
    assert Version("1.5.4") in get_version.fetch_pypi_versions("types-typed-ast")
    assert not get_version.fetch_pypi_versions("types-nonexistent-distribution")


@pytest.mark.parametrize(
    "distribution", os.listdir(os.path.join(TYPESHED, THIRD_PARTY_NAMESPACE))
)
def test_build_wheel(distribution: str) -> None:
    """Check that we can build wheels for all distributions."""
    tmp_dir = build_wheel.main(TYPESHED, distribution, version="1.1.1")
    assert tmp_dir.endswith("/dist")
    assert list(os.listdir(tmp_dir))  # check it is not empty


@pytest.mark.parametrize(
    "distribution", os.listdir(os.path.join(TYPESHED, THIRD_PARTY_NAMESPACE))
)
def test_version_increment(distribution: str) -> None:
    get_version.determine_incremented_version(read_metadata(TYPESHED, distribution))


def test_unvalidated_properties() -> None:
    m = Metadata("fake", {"version": "0.1", "requires": ["numpy", "types-six>=0.1"]})
    assert [r.name for r in m._unvalidated_requires] == ["numpy", "types-six"]
    assert [r.name for r in m._unvalidated_requires_external] == ["numpy"]
    assert [r.name for r in m._unvalidated_requires_typeshed] == ["types-six"]


def test_verify_typeshed_req() -> None:
    # Check that some known dependencies verify as valid.
    verify_typeshed_req(Requirement("types-six"))
    verify_typeshed_req(Requirement("types-six==0.1.1"))
    verify_typeshed_req(Requirement("types-typed-ast"))
    verify_typeshed_req(Requirement("types-typed-ast>=3.7"))

    with pytest.raises(InvalidRequires, match="to start with types-"):
        verify_typeshed_req(Requirement("unsupported"))

    with pytest.raises(InvalidRequires, match="to be uploaded from stub_uploader"):
        verify_typeshed_req(Requirement("types-unknown-xxx"))

    m = Metadata("mypy", {"version": "0.1", "requires": ["types-unknown-xxx"]})
    assert m.requires_typeshed == []


def test_verify_external_req() -> None:
    # Check that some known dependencies verify as valid.
    verify_external_req(
        Requirement("typing-extensions"), "mypy", _unsafe_ignore_allowlist=True
    )
    verify_external_req(
        Requirement("mypy-extensions"), "mypy", _unsafe_ignore_allowlist=True
    )

    with pytest.raises(InvalidRequires, match="to be present in the allowlist"):
        verify_external_req(Requirement("typing-extensions"), "mypy")

    m = Metadata("pandas", {"version": "0.1", "requires": ["numpy"]})
    assert [r.name for r in m.requires_external] == ["numpy"]

    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        verify_external_req(Requirement("numpy"), "mypy")

    with pytest.raises(InvalidRequires, match="to not be uploaded from stub_uploader"):
        verify_external_req(Requirement("types-typed-ast"), "mypy")

    with pytest.raises(InvalidRequires, match="to not start with types-"):
        verify_external_req(Requirement("types-unknown-xxx"), "mypy")

    m = Metadata("mypy", {"version": "0.1", "requires": ["numpy"]})
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.requires_external
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        recursive_verify(m, TYPESHED)

    # TODO: change tests once METADATA.toml specifies whether a dist is on PyPI
    m = Metadata("gdb", {"version": "0.1", "requires": []})
    assert m.requires_external == []

    m = Metadata("gdb", {"version": "0.1", "requires": ["something"]})
    with pytest.raises(InvalidRequires, match="no upstream distribution on PyPI"):
        m.requires_external


def test_dependency_order() -> None:
    """Test sort_by_dependency correctly sorts all packages by dependency."""
    distributions = os.listdir(os.path.join(TYPESHED, "stubs"))
    to_upload = list(sort_by_dependency(TYPESHED, distributions))
    assert len(set(to_upload)) == len(to_upload)
    for distribution in distributions:
        for req in read_metadata(TYPESHED, distribution).requires_typeshed:
            assert to_upload.index(strip_types_prefix(req.name)) < to_upload.index(
                distribution
            )


def test_recursive_verify_single() -> None:
    m = read_metadata(TYPESHED, "six")
    assert recursive_verify(m, TYPESHED) == {"types-six"}

    m = read_metadata(TYPESHED, "tzlocal")
    assert recursive_verify(m, TYPESHED) == {"types-tzlocal", "types-pytz"}


@pytest.mark.parametrize(
    "distribution", os.listdir(os.path.join(TYPESHED, THIRD_PARTY_NAMESPACE))
)
def test_recursive_verify(distribution: str) -> None:
    recursive_verify(read_metadata(TYPESHED, distribution), TYPESHED)
