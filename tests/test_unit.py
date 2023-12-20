"""Unit tests for simple helpers should go here."""

import datetime
from io import StringIO
import os
import tempfile
from typing import Any

import pytest
from packaging.version import Version

from stub_uploader.build_wheel import collect_setup_entries
from stub_uploader.get_version import (
    AlreadyUploadedError,
    compute_stub_version,
    ensure_specificity,
)
from stub_uploader.metadata import _UploadedPackages, strip_types_prefix, Metadata
from stub_uploader.ts_data import parse_requirements


def test_strip_types_prefix() -> None:
    assert strip_types_prefix("types-foo") == "foo"
    with pytest.raises(ValueError):
        strip_types_prefix("bad")


def test_ensure_specificity() -> None:
    ver = [1]
    ensure_specificity(ver, 3)
    assert ver == [1, 0, 0]

    ver = [1, 2, 3]
    ensure_specificity(ver, 3)
    assert ver == [1, 2, 3]

    ver = [1, 2, 3, 4, 5]
    ensure_specificity(ver, 3)
    assert ver == [1, 2, 3, 4, 5]


STUB_DATE = datetime.date(2024, 9, 12)
STUB_V = STUB_DATE.strftime("%Y%m%d")
FUTURE_V = "20240913"


def _stub_ver(ver: str, published: list[str]) -> str:
    published_vers = [Version(v) for v in published]
    return str(compute_stub_version(ver, published_vers, STUB_DATE))


def test_compute_stub_version() -> None:
    # never before published version
    empty_list: list[str] = []
    assert _stub_ver("1", empty_list) == f"1.0.0.{STUB_V}"
    assert _stub_ver("1.2", empty_list) == f"1.2.0.{STUB_V}"
    assert _stub_ver("1.2.post3", empty_list) == f"1.2.3.{STUB_V}"

    # published greater than version spec
    assert _stub_ver("1.1", ["1.2"]) == f"1.2.0.{STUB_V}"
    assert _stub_ver("1.1", ["1.2.3"]) == f"1.2.3.{STUB_V}"
    assert _stub_ver("1.2", ["1.3.0.4"]) == f"1.3.0.{STUB_V}"
    assert _stub_ver("1.1", ["1.2.3.4.5"]) == f"1.2.3.4.{STUB_V}"
    assert _stub_ver("1.4.40", ["1.4.50"]) == f"1.4.50.{STUB_V}"
    assert _stub_ver("1.4.0.40", ["1.4.0.50"]) == f"1.4.0.50.{STUB_V}"
    assert _stub_ver("1.2.post3", ["1.2.3.4"]) == f"1.2.3.{STUB_V}"

    # published less than version spec
    assert _stub_ver("1.2", ["1.1.0.4"]) == f"1.2.0.{STUB_V}"
    assert _stub_ver("1", ["0.9"]) == f"1.0.0.{STUB_V}"
    assert _stub_ver("1.1", ["0.9"]) == f"1.1.0.{STUB_V}"
    assert _stub_ver("1.2.3", ["1.1.0.70"]) == f"1.2.3.{STUB_V}"
    assert _stub_ver("1.2.3", [f"1.1.0.{STUB_V}"]) == f"1.2.3.{STUB_V}"
    assert _stub_ver("1.2.3", [f"1.1.0.{FUTURE_V}"]) == f"1.2.3.{STUB_V}"
    assert _stub_ver("1.2.3.4", ["1.1.0.17"]) == f"1.2.3.4.{STUB_V}"
    assert _stub_ver("1.2.post3", ["1.1.0.17"]) == f"1.2.3.{STUB_V}"
    assert _stub_ver("1.2.3", ["1.1.0.21000101"]) == f"1.2.3.{STUB_V}"

    # published equals version spec
    assert _stub_ver("1.1", ["1.1"]) == f"1.1.0.{STUB_V}"
    assert _stub_ver("1.1", ["1.1.0.19991204"]) == f"1.1.0.{STUB_V}"
    assert _stub_ver("1.1", ["1.1.3.19991204"]) == f"1.1.3.{STUB_V}"
    assert _stub_ver("1.2.3.4", ["1.2.3.4.19991204"]) == f"1.2.3.4.{STUB_V}"
    assert _stub_ver("1.2.3.4.5", ["1.2.3.4.5"]) == f"1.2.3.4.5.{STUB_V}"

    # test with multiple published versions
    assert (
        _stub_ver("1.2", ["1.1.0.7", "1.2.0.7", "1.3.0.19991204"]) == f"1.3.0.{STUB_V}"
    )


def test_compute_stub_version__already_uploaded() -> None:
    with pytest.raises(AlreadyUploadedError):
        _stub_ver("1.2.*", ["1.2.0.1", f"1.2.0.{STUB_V}"])


def test_collect_setup_entries() -> None:
    stubs = os.path.join("data", "test_typeshed", "stubs")
    entries = collect_setup_entries(os.path.join(stubs, "singlefilepkg"))
    assert entries == ({"singlefilepkg-stubs": ["__init__.pyi", "METADATA.toml"]})

    entries = collect_setup_entries(os.path.join(stubs, "multifilepkg"))
    assert entries == (
        {
            "multifilepkg-stubs": [
                "__init__.pyi",
                "a.pyi",
                "b.pyi",
                os.path.join("c", "__init__.pyi"),
                os.path.join("c", "d.pyi"),
                os.path.join("c", "e.pyi"),
                "METADATA.toml",
            ]
        }
    )

    entries = collect_setup_entries(os.path.join(stubs, "nspkg"))
    assert entries == (
        {
            "nspkg-stubs": [
                os.path.join("innerpkg", "__init__.pyi"),
                "METADATA.toml",
            ]
        }
    )


def test_collect_setup_entries_bogusfile() -> None:
    stubs = os.path.join("data", "test_typeshed", "stubs")
    with pytest.raises(
        ValueError, match="Only stub files are allowed, not 'bogusfile.txt'"
    ):
        collect_setup_entries(os.path.join(stubs, "bogusfiles"))

    # Make sure gitignored files aren't collected, nor do they crash function
    with open(os.path.join(stubs, "singlefilepkg", ".METADATA.toml.swp"), "w"):
        pass
    entries = collect_setup_entries(os.path.join(stubs, "singlefilepkg"))
    assert len(entries["singlefilepkg-stubs"]) == 2

    with open(
        os.path.join(stubs, "multifilepkg", "multifilepkg", ".METADATA.toml.swp"), "w"
    ):
        pass
    entries = collect_setup_entries(os.path.join(stubs, "multifilepkg"))
    assert len(entries["multifilepkg-stubs"]) == 7


def test_uploaded_packages() -> None:
    with tempfile.TemporaryDirectory() as td:
        file_path = os.path.join(td, "uploaded_packages.txt")
        with open(file_path, "w") as f:
            f.write("types-SqLaLcHeMy\n")

        up = _UploadedPackages(file_path)
        assert up.read() == {"types-sqlalchemy"}

        up.add("SQLAlchemy")
        assert up.read() == {"types-sqlalchemy"}

        up.add("six")
        assert up.read() == {"types-sqlalchemy", "types-six"}

        with open(file_path) as f:
            assert f.read() == "types-SqLaLcHeMy\ntypes-six"


_REQUIREMENTS_TXT = """# This is a comment

pkg1==1.2
pkg2==2.3.4  # This is a comment
pkg3==2023.4.13; python_version >= "3.6"
multispec==3.4.5,>3.4.5
range>=1.2.3
no_version
"""


@pytest.mark.parametrize(
    "name,version",
    [
        ("pkg1", "1.2"),
        ("pkg2", "2.3.4"),
        ("pkg3", "2023.4.13"),
    ],
)
def test_parse_requirements__parsed_packages(name: str, version: str) -> None:
    requirements = parse_requirements(StringIO(_REQUIREMENTS_TXT))
    assert name in requirements, f"package {name} not found"
    assert requirements[name] == version, f"package {name} has wrong version"


@pytest.mark.parametrize(
    "name",
    [
        "multispec",
        "range",
        "no_version",
    ],
)
def test_parse_requirements__skipped_packages(name: str) -> None:
    requirements = parse_requirements(StringIO(_REQUIREMENTS_TXT))
    assert name not in requirements, f"package {name} was not skipped"


@pytest.mark.parametrize(
    "data,expected",
    [
        ({}, None),
        ({"upstream_repository": 12345}, None),
        ({"upstream_repository": "https://[].foo.com"}, None),
        (
            {"upstream_repository": "https://github.com/psf/requests"},
            "https://github.com/psf/requests",
        ),
    ],
)
def test_upstream_repo_validation(data: dict[str, Any], expected: str | None) -> None:
    m = Metadata("foo", data)
    assert m.upstream_repository == expected
    assert type(m.upstream_repository) is type(expected)
