"""Unit tests for simple helpers should go here."""

import datetime
import os
import tempfile
from io import StringIO
from pathlib import Path
from typing import Any

import pytest
from packaging.specifiers import Specifier
from packaging.version import Version

from stub_uploader.build_wheel import collect_package_data
from stub_uploader.get_version import compute_stub_version, ensure_specificity
from stub_uploader.metadata import Metadata, _UploadedPackages, strip_types_prefix
from stub_uploader.ts_data import TypeshedData, parse_requirements, read_typeshed_data
from stub_uploader.update_changelog import process_git_log


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


DISTRIBUTION = "setuptools"
TODAY = datetime.date(2024, 9, 12)
TODAY_V = TODAY.strftime("%Y%m%d")
TOMORROW_V = "20240913"
IN_TWO_DAYS_V = "20240914"


def _stub_ver(ver: str, published: list[str]) -> str:
    published_vers = [Version(v) for v in published]
    if ver[0].isdigit():
        ver = f"=={ver}"
    spec = Specifier(ver)
    return str(compute_stub_version(spec, published_vers, TODAY))


def test_compute_stub_version() -> None:
    # never before published version
    empty_list: list[str] = []
    assert _stub_ver("1", empty_list) == f"1.0.0.{TODAY_V}"
    assert _stub_ver("1.2", empty_list) == f"1.2.0.{TODAY_V}"
    assert _stub_ver("1.2.post3", empty_list) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("~=1.2", empty_list) == f"1.2.0.{TODAY_V}"
    assert _stub_ver("~=1.2.3", empty_list) == f"1.2.3.{TODAY_V}"

    # published greater than version spec
    assert _stub_ver("1.1", ["1.2"]) == f"1.2.0.{TODAY_V}"
    assert _stub_ver("1.1", ["1.2.3"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("1.2", ["1.3.0.4"]) == f"1.3.0.{TODAY_V}"
    assert _stub_ver("1.1", ["1.2.3.4.5"]) == f"1.2.3.4.{TODAY_V}"
    assert _stub_ver("1.4.40", ["1.4.50"]) == f"1.4.50.{TODAY_V}"
    assert _stub_ver("1.4.0.40", ["1.4.0.50"]) == f"1.4.0.50.{TODAY_V}"
    assert _stub_ver("1.2.post3", ["1.2.3.4"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("~=1.2", ["1.3.0.4"]) == f"1.3.0.{TODAY_V}"
    assert _stub_ver("~=1.2.3", ["1.2.4.40"]) == f"1.2.4.{TODAY_V}"

    # published less than version spec
    assert _stub_ver("1.2", ["1.1.0.4"]) == f"1.2.0.{TODAY_V}"
    assert _stub_ver("1", ["0.9"]) == f"1.0.0.{TODAY_V}"
    assert _stub_ver("1.1", ["0.9"]) == f"1.1.0.{TODAY_V}"
    assert _stub_ver("1.2.3", ["1.1.0.70"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("1.2.3", [f"1.1.0.{TODAY_V}"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("1.2.3", [f"1.1.0.{TOMORROW_V}"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("1.2.3.4", ["1.1.0.17"]) == f"1.2.3.4.{TODAY_V}"
    assert _stub_ver("1.2.post3", ["1.1.0.17"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("1.2.3", ["1.1.0.21000101"]) == f"1.2.3.{TODAY_V}"
    assert _stub_ver("~=1.2", ["1.1.0.40"]) == f"1.2.0.{TODAY_V}"
    assert _stub_ver("~=1.2.3", ["1.2.2.40"]) == f"1.2.3.{TODAY_V}"

    # published equals version spec
    assert _stub_ver("1.1", ["1.1"]) == f"1.1.0.{TODAY_V}"
    assert _stub_ver("1.1", ["1.1.0.19991204"]) == f"1.1.0.{TODAY_V}"
    assert _stub_ver("1.1", ["1.1.3.19991204"]) == f"1.1.3.{TODAY_V}"
    assert _stub_ver("1.2.3.4", ["1.2.3.4.19991204"]) == f"1.2.3.4.{TODAY_V}"
    assert _stub_ver("1.2.3.4.5", ["1.2.3.4.5"]) == f"1.2.3.4.5.{TODAY_V}"
    assert _stub_ver("~=1.2.3", ["1.2.3.40"]) == f"1.2.3.{TODAY_V}"

    # test with multiple published versions
    assert (
        _stub_ver("1.2", ["1.1.0.7", "1.2.0.7", "1.3.0.19991204"]) == f"1.3.0.{TODAY_V}"
    )

    # today's package was already uploaded
    assert (
        _stub_ver("1.2.*", ["1.2.0.1", f"1.2.0.{TODAY_V}", f"1.2.0.{TOMORROW_V}"])
        == f"1.2.0.{IN_TWO_DAYS_V}"
    )
    assert (
        _stub_ver("1.2.*", [f"1.1.0.{TODAY_V}", f"1.1.0.{TOMORROW_V}"])
        == f"1.2.0.{TODAY_V}"
    )
    assert (
        _stub_ver("~=1.2.3", [f"1.2.3.{TODAY_V}", f"1.2.3.{TOMORROW_V}"])
        == f"1.2.3.{IN_TWO_DAYS_V}"
    )
    assert _stub_ver("~=1.2.3", [f"1.4.0.{TODAY_V}"]) == f"1.4.0.{TOMORROW_V}"


def test_collect_package_data() -> None:
    stubs = Path("data") / "test_typeshed" / "stubs"
    pkg_data = collect_package_data(stubs / "singlefilepkg")
    assert pkg_data.top_level_packages == ["singlefilepkg-stubs"]
    assert pkg_data.package_data == (
        {"singlefilepkg-stubs": ["__init__.pyi", "METADATA.toml", "py.typed"]}
    )

    pkg_data = collect_package_data(stubs / "multifilepkg")
    assert pkg_data.top_level_packages == ["multifilepkg-stubs"]
    assert pkg_data.package_data == (
        {
            "multifilepkg-stubs": [
                "__init__.pyi",
                "a.pyi",
                "b.pyi",
                os.path.join("c", "__init__.pyi"),
                os.path.join("c", "d.pyi"),
                os.path.join("c", "e.pyi"),
                "METADATA.toml",
                "py.typed",
            ]
        }
    )

    pkg_data = collect_package_data(stubs / "nspkg")
    assert pkg_data.top_level_packages == ["nspkg-stubs"]
    assert pkg_data.package_data == (
        {
            "nspkg-stubs": [
                os.path.join("innerpkg", "__init__.pyi"),
                "METADATA.toml",
                os.path.join("innerpkg", "py.typed"),
            ]
        }
    )


def test_collect_package_data_bogusfile() -> None:
    stubs = Path("data") / "test_typeshed" / "stubs"
    with pytest.raises(
        ValueError, match="Only stub files are allowed, not 'bogusfile.txt'"
    ):
        collect_package_data(stubs / "bogusfiles")

    # Make sure gitignored files aren't collected, nor do they crash function
    with open(os.path.join(stubs, "singlefilepkg", ".METADATA.toml.swp"), "w"):
        pass
    pkg_data = collect_package_data(stubs / "singlefilepkg")
    assert set(pkg_data.package_data["singlefilepkg-stubs"]) == {
        "__init__.pyi",
        "py.typed",
        "METADATA.toml",
    }

    with open(
        os.path.join(stubs, "multifilepkg", "multifilepkg", ".METADATA.toml.swp"), "w"
    ):
        pass
    pkg_data = collect_package_data(stubs / "multifilepkg")
    assert set(pkg_data.package_data["multifilepkg-stubs"]) == {
        "__init__.pyi",
        "a.pyi",
        "b.pyi",
        "c/__init__.pyi",
        "c/d.pyi",
        "c/e.pyi",
        "py.typed",
        "METADATA.toml",
    }


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


def _build_pyproject(oldest_supported_python: str | None = "3.10") -> str:
    pp = "[tool.typeshed]\n"
    if oldest_supported_python is not None:
        pp += f'oldest_supported_python = "{oldest_supported_python}"\n'
    return pp


_REQUIREMENTS_TXT = """# This is a comment

pkg1==1.2
pkg2==2.3.4  # This is a comment
pkg3==2023.4.13; python_version >= "3.6"
multispec==3.4.5,>3.4.5
range>=1.2.3
no_version
"""


def _build_requirements(
    *,
    mypy: str | None = "1.11.1",
    pyright: str | None = "1.1.381",
) -> str:
    req = _REQUIREMENTS_TXT
    if mypy is not None:
        req += f"\nmypy=={mypy}"
    if pyright is not None:
        req += f"\npyright=={pyright}"
    return req


def _test_typeshed_data(pyproject: str, requirements: str) -> TypeshedData:
    with tempfile.TemporaryDirectory() as td:
        temp_path = Path(td)
        (temp_path / "pyproject.toml").write_text(pyproject)
        (temp_path / "requirements-tests.txt").write_text(requirements)
        return read_typeshed_data(temp_path)


def test_read_typeshed_data__success() -> None:
    pp = _build_pyproject(oldest_supported_python="3.10")
    req = _build_requirements(mypy="1.11.1")
    data = _test_typeshed_data(pp, req)
    assert data.oldest_supported_python == "3.10"
    assert data.mypy_version == Version("1.11.1")


def test_read_typeshed_data__oldest_python_missing() -> None:
    pp = _build_pyproject(oldest_supported_python=None)
    req = _build_requirements(mypy=None)
    with pytest.raises(KeyError, match="oldest_supported_python"):
        _test_typeshed_data(pp, req)


def test_read_typeshed_data__oldest_python_invalid() -> None:
    pp = _build_pyproject(oldest_supported_python="3.12invalid")
    req = _build_requirements(mypy=None)
    with pytest.raises(ValueError, match="oldest_supported_python"):
        _test_typeshed_data(pp, req)


def test_read_typeshed_data__type_checkers_missing() -> None:
    pp = _build_pyproject()
    req = _build_requirements(mypy=None)
    with pytest.raises(KeyError, match="mypy"):
        _test_typeshed_data(pp, req)


def test_read_typeshed_data__invalid_type_checker_version() -> None:
    pp = _build_pyproject()
    req = _build_requirements(mypy="1.2.2invalid")
    with pytest.raises(ValueError, match="mypy"):
        _test_typeshed_data(pp, req)


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


def test_process_git_log() -> None:
    git_log = """
commit 126768408a69b7a3a09b7d3992970b289f92937e

    Replace `Incomplete | None = None` in third party stubs (#14063)

commit 337fd828e819988af2d3600283d8068bbbab7f50

    Bump setuptools to 80.7.* (#14069)
    
    Body text #12345 python/typeshed#12345 https://example.com/#123

commit 58f581cea1a5040a733e6284adf81bf0793ac26a

    [tqdm] Update to 4.67.2 (#15348)

    Closes: #15347
    Diff: https://github.com/tqdm/tqdm/compare/v4.67.1...v4.67.2
"""
    expected_entry = f"""\
## [80.7.0.{TODAY_V}](https://pypi.org/project/types-{DISTRIBUTION}/80.7.0.{TODAY_V}/) ({TODAY:%Y-%m-%d})

* Replace `Incomplete | None = None` in third party stubs ([#14063](https://github.com/python/typeshed/pull/14063))

* Bump setuptools to 80.7.* ([#14069](https://github.com/python/typeshed/pull/14069))

    Body text #12345 python/typeshed#12345 https://example.com/#123

* Update to 4.67.2 ([#15348](https://github.com/python/typeshed/pull/15348))

    Closes: #15347 \\
    Diff: https://github.com/tqdm/tqdm/compare/v4.67.1...v4.67.2

"""
    actual_entry = process_git_log(git_log, DISTRIBUTION, f"80.7.0.{TODAY_V}", TODAY)
    assert actual_entry == expected_entry
