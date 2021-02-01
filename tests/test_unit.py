"""Unit tests for simple helpers should go here."""

import pytest  # type: ignore[import]
from scripts.get_version import strip_dep_version
from scripts.build_wheel import sort_by_dependency, transitive_deps, strip_types_prefix


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
    assert transitive_deps(
        {"1": {"2"}, "2": {"3"}, "3": {"4"}, "4": set()}
    ) == (
        {"1": {"2", "3", "4"}, "2": {"3", "4"}, "3": {"4"}, "4": set()}
    )
    assert transitive_deps(
        {
            "1": {"2", "3"}, "2": {"2a", "2b"}, "3": {"3a", "3b"},
            "2a": set(), "2b": set(), "3a": set(), "3b": set()
        }
    ) == (
        {
            "1": {"2", "2a", "2b", "3", "3a", "3b"}, "2": {"2a", "2b"}, "3": {"3a", "3b"},
            "2a": set(), "2b": set(), "3a": set(), "3b": set()
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
    assert sort_by_dependency(
        {"1": {"2"}, "2": {"3"}, "3": {"4"}, "4": set()}
    ) == ["4", "3", "2", "1"]
    assert sort_by_dependency(
        {
            "1": {"2", "3"}, "2": {"2a", "2b"}, "3": {"3a", "3b"},
            "2a": set(), "2b": set(), "3a": set(), "3b": set()
        }
    ) == ["2a", "2b", "2", "3a", "3b", "3", "1"]
