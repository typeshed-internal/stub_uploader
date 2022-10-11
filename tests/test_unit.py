"""Unit tests for simple helpers should go here."""

import os
import tempfile

import pytest
from packaging.version import Version

from stub_uploader.build_wheel import collect_setup_entries
from stub_uploader.get_version import compute_incremented_version, ensure_specificity
from stub_uploader.metadata import _UploadedPackages, strip_types_prefix


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


def _incremented_ver(ver: str, published: list[str]) -> str:
    published_vers = [Version(v) for v in published]
    return str(compute_incremented_version(ver, published_vers))


def test_compute_incremented_version() -> None:
    # never before published version
    empty_list: list[str] = []
    assert _incremented_ver("1", empty_list) == "1.0.0.0"
    assert _incremented_ver("1.2", empty_list) == "1.2.0.0"

    # published greater than version spec
    assert _incremented_ver("1.2", ["1.3.0.4"]) == "1.3.0.5"
    assert _incremented_ver("1.1", ["1.2.0.1"]) == "1.2.0.2"
    assert _incremented_ver("1.1", ["1.2"]) == "1.2.0.1"
    assert _incremented_ver("1.1", ["1.2.3"]) == "1.2.3.1"
    assert _incremented_ver("1.1", ["1.2.3.4.5"]) == "1.2.3.4.6"
    assert _incremented_ver("1.4.40", ["1.4.50"]) == "1.4.50.1"
    assert _incremented_ver("1.4.0.40", ["1.4.0.50"]) == "1.4.0.50.1"

    # published less than version spec
    assert _incremented_ver("1.2", ["1.1.0.4"]) == "1.2.0.0"
    assert _incremented_ver("1", ["0.9"]) == "1.0.0.0"
    assert _incremented_ver("1.1", ["0.9"]) == "1.1.0.0"
    assert _incremented_ver("1.2.3", ["1.1.0.17"]) == "1.2.3.0"
    assert _incremented_ver("1.2.3.4", ["1.1.0.17"]) == "1.2.3.4.0"

    # published equals version spec
    assert _incremented_ver("1.1", ["1.1"]) == "1.1.0.1"
    assert _incremented_ver("1.1", ["1.1.0.4"]) == "1.1.0.5"
    assert _incremented_ver("1.1", ["1.1.3.4"]) == "1.1.3.5"
    assert _incremented_ver("1.2.3.4", ["1.2.3.4.5"]) == "1.2.3.4.6"
    assert _incremented_ver("1.2.3.4.5", ["1.2.3.4.5"]) == "1.2.3.4.5.1"

    # test that we do the max version right
    assert _incremented_ver("1.2", ["1.1.0.7", "1.2.0.7", "1.3.0.7"]) == "1.3.0.8"


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
                "c/__init__.pyi",
                "c/d.pyi",
                "c/e.pyi",
                "METADATA.toml",
            ]
        }
    )

    entries = collect_setup_entries(os.path.join(stubs, "nspkg"))
    assert entries == (
        {
            "nspkg-stubs": [
                "innerpkg/__init__.pyi",
                "METADATA.toml",
            ]
        }
    )


def test_collect_setup_entries_bogusfile() -> None:
    stubs = os.path.join("data", "test_typeshed", "stubs")
    with pytest.raises(ValueError, match="Only stub files are allowed: bogusfile.txt"):
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
