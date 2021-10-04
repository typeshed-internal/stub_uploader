"""Unit tests for simple helpers should go here."""

import os
import pytest
from scripts.get_version import strip_dep_version
from scripts.build_wheel import (
    collect_setup_entries,
    sort_by_dependency,
    transitive_deps,
    strip_types_prefix,
    BuildData,
    SUFFIX,
    PY2_SUFFIX,
)


def test_strip_types_prefix() -> None:
    assert strip_types_prefix("types-foo") == "foo"
    with pytest.raises(AssertionError):
        strip_types_prefix("bad")


def test_strip_version() -> None:
    assert strip_dep_version("foo") == "foo"
    assert strip_dep_version("types-foo") == "types-foo"
    assert strip_dep_version("foo==1.1") == "foo"
    assert strip_dep_version("types-foo==1.1") == "types-foo"
    assert strip_dep_version("foo>2.3") == "foo"
    assert strip_dep_version("types-foo>2.3") == "types-foo"


def test_transitive_deps() -> None:
    with pytest.raises(KeyError):
        # We require the graph to be complete for safety.
        transitive_deps({"1": {"2"}})
    assert transitive_deps({"1": {"2"}, "2": set()}) == {"1": {"2"}, "2": set()}
    with pytest.raises(AssertionError):
        transitive_deps({"1": {"1"}})
    with pytest.raises(AssertionError):
        transitive_deps({"1": {"2"}, "2": {"3"}, "3": {"1"}})
    assert transitive_deps({"1": {"2"}, "2": {"3"}, "3": {"4"}, "4": set()}) == (
        {"1": {"2", "3", "4"}, "2": {"3", "4"}, "3": {"4"}, "4": set()}
    )
    assert transitive_deps(
        {
            "1": {"2", "3"},
            "2": {"2a", "2b"},
            "3": {"3a", "3b"},
            "2a": set(),
            "2b": set(),
            "3a": set(),
            "3b": set(),
        }
    ) == (
        {
            "1": {"2", "2a", "2b", "3", "3a", "3b"},
            "2": {"2a", "2b"},
            "3": {"3a", "3b"},
            "2a": set(),
            "2b": set(),
            "3a": set(),
            "3b": set(),
        }
    )


def test_sort_by_dependency() -> None:
    with pytest.raises(KeyError):
        # We require the graph to be complete for safety.
        sort_by_dependency({"1": {"2"}})
    assert sort_by_dependency({"1": {"2"}, "2": set()}) == ["2", "1"]
    with pytest.raises(AssertionError):
        sort_by_dependency({"1": {"1"}})
    with pytest.raises(AssertionError):
        sort_by_dependency({"1": {"2"}, "2": {"3"}, "3": {"1"}})
    # Independent are in alphabetic order.
    assert sort_by_dependency({"2": set(), "1": set()}) == ["1", "2"]
    assert sort_by_dependency({"1": {"2"}, "2": {"3"}, "3": {"4"}, "4": set()}) == [
        "4",
        "3",
        "2",
        "1",
    ]
    assert (
        sort_by_dependency(
            {
                "1": {"2", "3"},
                "2": {"2a", "2b"},
                "3": {"3a", "3b"},
                "2a": set(),
                "2b": set(),
                "3a": set(),
                "3b": set(),
            }
        )
        == ["2a", "2b", "2", "3a", "3b", "3", "1"]
    )


def test_collect_setup_entries() -> None:
    stubs = os.path.join("data", "test_typeshed", "stubs")
    entries = collect_setup_entries(os.path.join(stubs, "singlefilepkg"), SUFFIX)
    assert entries == ({"singlefilepkg-stubs": ["__init__.pyi", "METADATA.toml"]})

    entries = collect_setup_entries(os.path.join(stubs, "singlefilepkg"), PY2_SUFFIX)
    assert entries == (
        {"singlefilepkg-python2-stubs": ["__init__.pyi", "METADATA.toml"]}
    )

    entries = collect_setup_entries(os.path.join(stubs, "multifilepkg"), SUFFIX)
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

    entries = collect_setup_entries(os.path.join(stubs, "nspkg"), SUFFIX)
    assert entries == (
        {
            "nspkg-stubs": [
                "innerpkg/__init__.pyi",
                "METADATA.toml",
            ]
        }
    )


def test_build_data() -> None:
    typeshed = os.path.join("data", "test_typeshed")
    singlefilepkg_bd = BuildData(typeshed, "singlefilepkg")
    assert singlefilepkg_bd.py3_stubs
    assert not singlefilepkg_bd.py2_stubs
    nspkg_bd = BuildData(typeshed, "nspkg")
    assert nspkg_bd.py3_stubs
    assert not nspkg_bd.py2_stubs


def test_collect_setup_entries_bogusfile() -> None:
    stubs = os.path.join("data", "test_typeshed", "stubs")
    with pytest.raises(ValueError, match="Only stub files are allowed: bogusfile.txt"):
        collect_setup_entries(os.path.join(stubs, "bogusfiles"), SUFFIX)

    # Make sure gitignored files aren't collected, nor do they crash function
    with open(os.path.join(stubs, "singlefilepkg", ".METADATA.toml.swp"), "w"):
        pass
    entries = collect_setup_entries(os.path.join(stubs, "singlefilepkg"), SUFFIX)
    assert len(entries["singlefilepkg-stubs"]) == 2

    with open(
        os.path.join(stubs, "multifilepkg", "multifilepkg", ".METADATA.toml.swp"), "w"
    ):
        pass
    entries = collect_setup_entries(os.path.join(stubs, "multifilepkg"), SUFFIX)
    assert len(entries["multifilepkg-stubs"]) == 7
