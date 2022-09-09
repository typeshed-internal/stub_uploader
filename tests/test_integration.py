"""
Integration tests for build scripts. These should not change
anything on PyPI, but can make PyPI queries and may expect
a typeshed checkout side by side.
"""
import os
import pytest
from packaging.version import Version
from stub_uploader import get_version, build_wheel
from stub_uploader.metadata import read_metadata

TYPESHED = "../typeshed"
UPLOADED = "data/uploaded_packages.txt"


def test_fetch_pypi_versions() -> None:
    """Check that we can query PyPI for package increments."""
    assert Version("1.16.0") in get_version.fetch_pypi_versions("six")
    assert Version("1.5.4") in get_version.fetch_pypi_versions("typed-ast")
    assert not get_version.fetch_pypi_versions("nonexistent-distribution")


def test_check_exists() -> None:
    assert get_version.check_exists("six")
    assert not get_version.check_exists("nonexistent-distribution")


@pytest.mark.parametrize("distribution", os.listdir(os.path.join(TYPESHED, "stubs")))
def test_build_wheel(distribution: str) -> None:
    """Check that we can build wheels for all distributions."""
    tmp_dir = build_wheel.main(TYPESHED, distribution, version="1.1.1")
    assert tmp_dir.endswith("/dist")
    assert list(os.listdir(tmp_dir))  # check it is not empty


@pytest.mark.parametrize("distribution", os.listdir(os.path.join(TYPESHED, "stubs")))
def test_version_increment(distribution: str) -> None:
    get_version.determine_incremented_version(read_metadata(TYPESHED, distribution))


def test_verify_dependency() -> None:
    # Check some known dependencies that they verify as valid.
    build_wheel.verify_dependency(TYPESHED, "types-six", UPLOADED)
    build_wheel.verify_dependency(TYPESHED, "types-six==0.1.1", UPLOADED)
    build_wheel.verify_dependency(TYPESHED, "types-typed-ast", UPLOADED)
    build_wheel.verify_dependency(TYPESHED, "types-typed-ast>=3.7", UPLOADED)
    # Also check couple errors.
    with pytest.raises(AssertionError):
        build_wheel.verify_dependency(TYPESHED, "unsupported", UPLOADED)
    with pytest.raises(AssertionError):
        build_wheel.verify_dependency(TYPESHED, "types-unknown-xxx", UPLOADED)


def test_dependency_order() -> None:
    """Test that all packages are correctly sorted by dependency."""
    distributions = os.listdir(os.path.join(TYPESHED, "stubs"))
    to_upload = build_wheel.sort_by_dependency(
        build_wheel.make_dependency_map(TYPESHED, distributions)
    )
    assert len(set(to_upload)) == len(to_upload)
    for distribution in distributions:
        for dependency in read_metadata(TYPESHED, distribution).requires:
            assert to_upload.index(
                build_wheel.strip_types_prefix(
                    get_version.strip_dep_version(dependency)
                )
            ) < to_upload.index(distribution)
