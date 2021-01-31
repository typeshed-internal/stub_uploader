"""
Integration tests for build scripts. These should not change
anything on PyPI, but can make PyPI queries and may expect
a typeshed checkout side by side.
"""
import os
import pytest
from scripts import get_version, build_wheel

TYPESHED = "../typeshed"
UPLOADED = "data/uploaded_packages.txt"


def test_version() -> None:
    # Check that we can query PyPI for package increments.
    assert get_version.main(TYPESHED, "six", "0.1") >= 0
    assert get_version.main(TYPESHED, "nonexistent-distribution", "0.1") == -1
    assert get_version.main(TYPESHED, "typing-extensions", "0.1") == -1
    assert get_version.main(TYPESHED, "typing-extensions", None) >= 0


def test_check_exists() -> None:
    assert get_version.check_exists("six")
    assert not get_version.check_exists("nonexistent-distribution")


def test_build_wheel() -> None:
    # Check that we can build wheels for all distributions.
    for distribution in os.listdir(os.path.join(TYPESHED, "stubs")):
        tmp_dir = build_wheel.main(TYPESHED, distribution, increment=1)
        assert tmp_dir.endswith("/dist")
        assert list(os.listdir(tmp_dir))  # check it is not empty


def test_verify_dependency() -> None:
    # Check some known dependencies that they verify as valid.
    build_wheel.verify_dependency(TYPESHED, "types-six", UPLOADED)
    build_wheel.verify_dependency(TYPESHED, "types-six==0.1.1", UPLOADED)
    build_wheel.verify_dependency(TYPESHED, "types-typing-extensions", UPLOADED)
    build_wheel.verify_dependency(TYPESHED, "types-typing-extensions>=3.7", UPLOADED)
    # Also check couple errors.
    with pytest.raises(AssertionError):
        build_wheel.verify_dependency(TYPESHED, "unsupported", UPLOADED)
    with pytest.raises(AssertionError):
        build_wheel.verify_dependency(TYPESHED, "types-unknown-xxx", UPLOADED)
