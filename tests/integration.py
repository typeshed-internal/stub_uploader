"""
Integration tests for build scripts. These should not change
anything on PyPI, but can make PyPI queries and may expect
a typeshed checkout side by side.
"""
import os
from scripts import get_version, build_wheel

TYPESHED = "../typeshed"


def test_version() -> None:
    # Check that we can query PyPI for package increments.
    assert get_version.main(TYPESHED, "six", "0.1") >= 0
    assert get_version.main(TYPESHED, "nonexistent-distribution", "0.1") == -1
    assert get_version.main(TYPESHED, "typing-extensions", "0.1") == -1
    assert get_version.main(TYPESHED, "typing-extensions", None) >= 0


def test_build_wheel() -> None:
    # Check that we can build wheels for all distributions.
    for distribution in os.listdir(os.path.join(TYPESHED, "stubs")):
        tmp_dir = build_wheel.main(TYPESHED, distribution, increment=1)
        assert tmp_dir.endswith("/dist")
        assert list(os.listdir(tmp_dir))  # check it is not empty
