import pytest

from stub_uploader.metadata import InvalidRequires, Metadata, uploaded_packages
from tests.test_integration import TYPESHED


def test_dependencies() -> None:
    typeshed_pkgs = uploaded_packages.read()

    m = Metadata(
        "tensorflow",
        {
            "version": "2.18.0",
            "dependencies": ["requests", "numpy", "types-protobuf"],
        },
        typeshed_pkgs,
    )
    assert sorted([r.name for r in m.dependencies]) ==  ["numpy", "requests", "types-protobuf"]
    assert m.optional_dependencies == []


def test_optional_dependencies() -> None:
    typeshed_pkgs = uploaded_packages.read()

    m = Metadata(
        "tqdm",
        {
            "version": "4.70.0",
            "optional-dependencies": ["requests", "types-tensorflow"],
        },
        typeshed_pkgs,
    )
    assert m.dependencies == []
    assert sorted([r.name for r in m.optional_dependencies]) == [
        "requests",
        "types-tensorflow",
    ]


def test_invalid_dependencies() -> None:
    typeshed_pkgs = uploaded_packages.read()

    # numpy is not a dependency of mypy, so this should raise an error
    m = Metadata("mypy", {"version": "1.*", "dependencies": ["numpy"]}, typeshed_pkgs)
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.dependencies
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.validate_dependencies_recursively(TYPESHED)


def test_invalid_optional_dependencies() -> None:
    typeshed_pkgs = uploaded_packages.read()

    # numpy is not a dependency of mypy, so this should raise an error
    m = Metadata(
        "mypy", {"version": "1.*", "optional-dependencies": ["numpy"]}, typeshed_pkgs
    )
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.optional_dependencies
    with pytest.raises(InvalidRequires, match="to be listed in mypy's requires_dist"):
        m.validate_dependencies_recursively(TYPESHED)


def test_gdb() -> None:
    typeshed_pkgs = uploaded_packages.read()
    # TODO: change tests once METADATA.toml specifies whether a dist is on PyPI
    m = Metadata("gdb", {"version": "0.1", "dependencies": []}, typeshed_pkgs)
    assert m.dependencies == []

    m = Metadata(
        "gdb", {"version": "0.1", "dependencies": ["cryptography"]}, typeshed_pkgs
    )
    with pytest.raises(InvalidRequires, match="no upstream distribution on PyPI"):
        m.dependencies
