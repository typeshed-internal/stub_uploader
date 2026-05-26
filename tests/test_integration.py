"""
Integration tests for build scripts. These should not change
anything on PyPI, but can make PyPI queries and may expect
a typeshed checkout side by side.
"""

import os
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

import pytest
from packaging.requirements import Requirement
from packaging.version import Version

from stub_uploader import build_wheel, get_version
from stub_uploader.const import THIRD_PARTY_NAMESPACE
from stub_uploader.metadata import (
    InvalidRequires,
    Metadata,
    read_metadata,
    sort_by_dependency,
    strip_types_prefix,
    uploaded_packages,
    verify_external_req,
    verify_requires_python,
)
from stub_uploader.ts_data import read_typeshed_data

TYPESHED = "../typeshed"
THIRD_PARTY_PATH = Path(TYPESHED) / THIRD_PARTY_NAMESPACE


def test_fetch_pypi_versions() -> None:
    """Check that we can query PyPI for package increments."""
    assert Version("1.16.0") in get_version.fetch_pypi_versions("types-six")
    assert Version("1.5.4") in get_version.fetch_pypi_versions("types-typed-ast")
    assert not get_version.fetch_pypi_versions("types-nonexistent-distribution")


@pytest.mark.parametrize("distribution", os.listdir(THIRD_PARTY_PATH))
def test_build_wheel(distribution: str) -> None:
    """Check that we can build wheels for all distributions."""
    with TemporaryDirectory(prefix="stub-uploader-") as tmp_dir:
        build_path = build_wheel.main(
            TYPESHED, distribution, version="1.1.1", build_dir=tmp_dir
        )
        assert build_path.name == "dist"
        assert list(build_path.iterdir())  # check it is not empty


@pytest.mark.parametrize(
    "distribution,file_list",
    [
        ("flake8", [Path("flake8-stubs") / "checker.pyi"]),
        ("protobuf", [Path("google-stubs") / "protobuf" / "__init__.pyi"]),
    ],
)
def test_build_wheel_files(distribution: str, file_list: list[Path]) -> None:
    """Assert that a wheel contains certain files."""
    with TemporaryDirectory(prefix="stub-uploader-") as tmp_dir:
        build_path = build_wheel.main(
            TYPESHED, distribution, version="1.1.1", build_dir=tmp_dir
        )
        wheels = list(build_path.glob("*.whl"))
        assert len(wheels) == 1
        with ZipFile(wheels[0], "r") as zip_file:
            zip_file.extractall(build_path)
        for file_path in file_list:
            assert build_path.joinpath(file_path).exists()


@pytest.mark.parametrize("distribution", os.listdir(THIRD_PARTY_PATH))
def test_version_increment(distribution: str) -> None:
    get_version.determine_stub_version(read_metadata(TYPESHED, distribution))


def test_metadata_dependencies() -> None:
    typeshed_pkgs = uploaded_packages.read()

    m = Metadata(
        "auth0-python",
        {"version": "0.1", "dependencies": ["cryptography", "types-requests>=0.1"]},
        typeshed_pkgs,
    )
    assert sorted([r.name for r in m.dependencies]) == [
        "cryptography",
        "types-requests",
    ]

    m = Metadata("pandas", {"version": "0.1", "dependencies": ["numpy"]}, typeshed_pkgs)
    assert [r.name for r in m.dependencies] == ["numpy"]

    # numpy is not a dependency of mypy, so this should raise an error
    m = Metadata("mypy", {"version": "0.1", "dependencies": ["numpy"]}, typeshed_pkgs)
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.dependencies
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.validate_dependencies_recursively(TYPESHED)

    # TODO: change tests once METADATA.toml specifies whether a dist is on PyPI
    m = Metadata("gdb", {"version": "0.1", "dependencies": []}, typeshed_pkgs)
    assert m.dependencies == []

    m = Metadata(
        "gdb", {"version": "0.1", "dependencies": ["cryptography"]}, typeshed_pkgs
    )
    with pytest.raises(InvalidRequires, match="no upstream distribution on PyPI"):
        m.dependencies


def test_verify_external_req() -> None:
    # Check that some known dependencies verify as valid.
    verify_external_req(
        Requirement("typing-extensions"),
        "mypy",
        _unsafe_ignore_allowlist=True,
    )
    verify_external_req(
        Requirement("mypy-extensions"),
        "mypy",
        _unsafe_ignore_allowlist=True,
    )
    # Check that types-foo can depend on foo
    verify_external_req(Requirement("setuptools"), "setuptools")

    with pytest.raises(
        InvalidRequires, match="to be present in the stub_uploader allowlist"
    ):
        verify_external_req(Requirement("typing-extensions"), "mypy")

    # Check differing runtime and stub dependencies
    verify_external_req(Requirement("pandas-stubs"), "geopandas")
    with pytest.raises(
        InvalidRequires,
        match=(
            r"Expected dependency pandas to be present in the stub_uploader allowlist"
            r"\. Did you mean pandas-stubs\?"
        ),
    ):
        verify_external_req(Requirement("pandas"), "geopandas")

    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        verify_external_req(Requirement("numpy"), "mypy")


def test_dependency_order() -> None:
    """Test sort_by_dependency correctly sorts all packages by dependency."""
    distributions = os.listdir(os.path.join(TYPESHED, "stubs"))
    to_upload = list(sort_by_dependency(TYPESHED, distributions))
    assert len(set(to_upload)) == len(to_upload)
    for distribution in distributions:
        for dep in read_metadata(TYPESHED, distribution).dependencies:
            if dep.is_typeshed_pkg:
                assert to_upload.index(strip_types_prefix(dep.name)) < to_upload.index(
                    distribution
                )


def test_recursive_verify_single() -> None:
    m = read_metadata(TYPESHED, "six")
    assert m.validate_dependencies_recursively(TYPESHED) == {"types-six"}

    m = read_metadata(TYPESHED, "requests-oauthlib")
    assert m.validate_dependencies_recursively(TYPESHED) == {
        "types-requests-oauthlib",
        "types-requests",
        "types-oauthlib",
    }


def test_dependency_order_single() -> None:
    assert list(sort_by_dependency(TYPESHED, ["requests-oauthlib"])) == [
        "requests-oauthlib"
    ]
    assert list(sort_by_dependency(TYPESHED, ["requests-oauthlib", "oauthlib"])) == [
        "oauthlib",
        "requests-oauthlib",
    ]


@pytest.mark.parametrize("distribution", os.listdir(THIRD_PARTY_PATH))
def test_recursive_verify(distribution: str) -> None:
    m = read_metadata(TYPESHED, distribution)
    m.validate_dependencies_recursively(TYPESHED)


def test_read_typeshed_data() -> None:
    read_typeshed_data(Path(TYPESHED))


def test_verify_requires_python() -> None:
    verify_requires_python(">=3.10")

    with pytest.raises(InvalidRequires, match="Invalid requires-python specifier"):
        verify_requires_python(">=fake")

    with pytest.raises(
        InvalidRequires, match="Expected requires-python to be a '>=' specifier"
    ):
        verify_requires_python("==3.10")


@pytest.mark.parametrize(
    "distribution,expected_packages",
    [
        ("fpdf2", ["fpdf-stubs"]),
        ("pytz", ["pytz-stubs"]),
        ("protobuf", ["google-stubs"]),
        ("google-cloud-ndb", ["google-stubs"]),
    ],
)
def test_pkg_data_top_level_packages(
    distribution: str, expected_packages: list[str]
) -> None:
    pkg_data = build_wheel.collect_package_data(THIRD_PARTY_PATH / distribution)
    assert pkg_data.top_level_packages == expected_packages


@pytest.mark.parametrize(
    "distribution,expected_packages",
    [
        ("fpdf2", ["fpdf-stubs"]),
        ("pytz", ["pytz-stubs"]),
        ("protobuf", ["google-stubs.protobuf"]),
        ("google-cloud-ndb", ["google-stubs.cloud.ndb"]),
    ],
)
def test_pkg_data_non_namespace_packages(
    distribution: str, expected_packages: list[str]
) -> None:
    pkg_data = build_wheel.collect_package_data(THIRD_PARTY_PATH / distribution)
    assert pkg_data.top_level_non_namespace_packages == expected_packages
