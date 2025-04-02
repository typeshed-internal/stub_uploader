"""
Basic script to generate a wheel for a third-party distribution in typeshed.

This generates a PEP 561 types stub package using METADATA.toml file for a given
distribution in typeshed stubs. Such package
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
the corresponding runtime Python package.

The generated wheel includes all type stubs (*.pyi files) and the METADATA.toml
itself, no other files can be included.

The types stubs live in https://github.com/python/typeshed/tree/main/stubs,
all fixes for types and metadata should be contributed there, see
https://github.com/python/typeshed/blob/main/CONTRIBUTING.md for more details.

This file also contains some helper functions related to wheel validation and upload.
"""

import argparse
import os
import os.path
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from textwrap import dedent

from stub_uploader.const import (
    CHANGELOG_PATH,
    META,
    TESTS_NAMESPACE,
    THIRD_PARTY_NAMESPACE,
)
from stub_uploader.metadata import Metadata, read_metadata
from stub_uploader.ts_data import TypeshedData, read_typeshed_data

CHANGELOG = "CHANGELOG.md"

SUFFIX = "-stubs"

PARTIAL_STUBS_DESCRIPTION = """
This stub package is marked as [partial](https://peps.python.org/pep-0561/#partial-stub-packages).
If you find that annotations are missing, feel free to contribute and help complete them.
""".lstrip()

SETUP_TEMPLATE = dedent(
    """
from setuptools import setup

setup(package_data={package_data})
"""
)

PYPROJECT_TEMPLATE = dedent(
    """
[build-system]
build-backend = "setuptools.build_meta"
requires = ["setuptools>=77.0.3"]

[project]
name = "{stub_distribution}"
version = "{version}"
license = "Apache-2.0"
license-files = ["LICENSE"]
description = "Typing stubs for {distribution}"
readme = {{ text = \"\"\"\\\n{long_description}\n\"\"\", content-type = "text/markdown" }}
classifiers = [
  "Programming Language :: Python :: 3",
  "Typing :: Stubs Only",
]
requires-python = "{requires_python}"
dependencies = {requires}

[project.urls]
"Homepage" = "https://github.com/python/typeshed"
"GitHub" = "https://github.com/python/typeshed"
"Changes" = "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/{distribution}.md"
"Issue tracker" = "https://github.com/python/typeshed/issues"
"Chat" = "https://gitter.im/python/typing"

[tool.setuptools]
packages = {packages}
include-package-data = false
"""
).lstrip()

NO_LONGER_UPDATED_TEMPLATE = """
*Note:* `{stub_distribution}` is unmaintained and won't be updated.
""".lstrip()

OBSOLETE_SINCE_TEXT_TEMPLATE = """
*Note:* The `{distribution}` package includes type annotations or type stubs
since version {obsolete_since}. Please uninstall the `{stub_distribution}`
package if you use this or a newer version.
""".lstrip()

DESCRIPTION_INTRO_TEMPLATE = """
## Typing stubs for {distribution}

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the {formatted_distribution} package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `{distribution}`. This version of
`{stub_distribution}` aims to provide accurate annotations for
`{distribution}{typeshed_version_spec}`.
""".strip()

DESCRIPTION_OUTRO_TEMPLATE = """
This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/{distribution}`](https://github.com/python/typeshed/tree/main/stubs/{distribution})
directory.

This package was tested with
mypy {ts_data.mypy_version},
pyright {ts_data.pyright_version},
and pytype {ts_data.pytype_version}.
It was generated from typeshed commit
[`{commit}`](https://github.com/python/typeshed/commit/{commit}).
""".strip()


class BuildData:
    def __init__(self, typeshed_dir: str, distribution: str) -> None:
        self.distribution = distribution
        self.stub_dir = Path(typeshed_dir) / THIRD_PARTY_NAMESPACE / distribution


class PackageData:
    """Information about the packages of a distribution and their contents."""

    def __init__(self, base_path: Path, package_data: dict[str, list[str]]) -> None:
        self.base_path = base_path
        self.package_data = package_data

    def package_source_path(self, package_name: str) -> Path:
        """Return the relative path of a given package name in the typeshed directory.

        The package name can use dotted notation to address sub-packages.
        The top-level package name can optionally include the "-stubs" suffix.
        """
        top_level, *sub_packages = package_name.split(".")
        if top_level.endswith(SUFFIX):
            top_level = top_level[: -len(SUFFIX)]
        return Path(top_level, *sub_packages)

    def package_build_path(self, package_name: str) -> Path:
        """Return the relative path of a given package name in the build directory.

        The package name can use dotted notation to address sub-packages.
        The top-level package name will include the "-stubs" suffix.
        """
        top_level, *sub_packages = package_name.split(".")
        if not top_level.endswith(SUFFIX):
            top_level += SUFFIX
        return Path(top_level, *sub_packages)

    def is_single_file_package(self, package_name: str) -> bool:
        filename = package_name.split("-")[0] + ".pyi"
        return (self.base_path / filename).exists()

    @property
    def top_level_packages(self) -> list[str]:
        """Top level package names.

        These are the packages that are not sub-packages of any other package
        and includes namespace packages. Their name includes the "-stubs"
        suffix.
        """
        return list(self.package_data.keys())

    @property
    def top_level_non_namespace_packages(self) -> list[str]:
        """Top level non-namespace package names.

        This will return all packages that are not subpackages of any other
        package, other than namespace packages in dotted notation, e.g. if
        "flying" is a top level namespace package, and "circus" is a
        non-namespace sub-package, this will return ["flying-stubs.circus"].
        """
        packages: list[str] = []
        for top_level in self.top_level_packages:
            if self.is_single_file_package(top_level):
                packages.append(top_level)
            else:
                packages.extend(self._find_non_namespace_sub_packages(top_level))
        return packages

    def _find_non_namespace_sub_packages(self, package: str) -> list[str]:
        path = self.base_path / self.package_source_path(package)
        if is_namespace_package(path):
            sub_packages: list[str] = []
            for entry in path.iterdir():
                if entry.is_dir():
                    sub_name = package + "." + entry.name
                    sub_packages.extend(self._find_non_namespace_sub_packages(sub_name))
            return sub_packages
        else:
            return [package]

    def add_file(self, package: str, filename: str) -> None:
        """Add a file to a top-level package."""
        top_level, *sub_packages = package.split(".")
        assert top_level.endswith(SUFFIX)
        path = Path(*sub_packages, filename)
        self.package_data[top_level].append(str(path))


def is_namespace_package(path: Path) -> bool:
    return not (path / "__init__.pyi").exists()


def find_stub_files(top: str) -> list[str]:
    """Find all stub files for a given package, relative to package root.

    Raise if we find any unknown file extensions during collection.
    """
    result: list[str] = []
    for root, _, files in os.walk(top):
        for file in files:
            if file.endswith(".pyi"):
                name, _ = os.path.splitext(file)
                assert (
                    name.isidentifier()
                ), "All file names must be valid Python modules"
                result.append(os.path.relpath(os.path.join(root, file), top))
            elif file == "py.typed":
                result.append(os.path.relpath(os.path.join(root, file), top))
            elif not file.endswith((".md", ".rst")):
                # Allow having README docs, as some stubs have these (e.g. click).
                if (
                    subprocess.run(["git", "check-ignore", file], cwd=top).returncode
                    != 0
                ):
                    raise ValueError(f"Only stub files are allowed, not {file!r}")
    return sorted(result)


def copy_stubs(base_dir: Path, dst: Path) -> None:
    """Copy stubs for given distribution to the build directory.

    For packages change name by appending "-stubs" suffix (PEP 561),
    also convert modules to trivial packages with a single __init__.pyi.
    """
    for entry in base_dir.iterdir():
        if entry.is_file():
            if entry.suffix != ".pyi":
                continue
            stub_dir = dst / (entry.stem + SUFFIX)
            stub_dir.mkdir(exist_ok=True)
            shutil.copy(entry, stub_dir / "__init__.pyi")
        else:
            if entry.name == TESTS_NAMESPACE:
                # Don't package tests for the stubs
                continue
            # Don't append the suffix if already present
            stub_dir = dst / ensure_suffix(entry.name, SUFFIX)
            shutil.copytree(entry, stub_dir, dirs_exist_ok=True)

        # We add original METADATA file in case some type-checking tool will want
        # to use it. Note that since it is not easy to package it outside of a package,
        # we copy it to every package in given distribution.
        shutil.copy(base_dir / META, stub_dir)


def ensure_suffix(s: str, suffix: str) -> str:
    """Ensure that a string ends with a suffix."""
    return s if s.endswith(suffix) else s + suffix


def create_py_typed(metadata: Metadata, pkg_data: PackageData, dst: Path) -> None:
    """Create py.typed files as necessary."""
    for package in pkg_data.top_level_non_namespace_packages:
        py_typed_path = dst / pkg_data.package_build_path(package) / "py.typed"
        py_typed_path.write_text("partial\n" if metadata.partial else "")


def copy_license(ts_data: TypeshedData, dst: Path) -> None:
    """Copy the license file from the typeshed repository to the build directory."""
    shutil.copy(ts_data.typeshed_path / "LICENSE", dst / "LICENSE")


def copy_changelog(distribution: str, dst: Path) -> None:
    """Copy changelog to the build directory."""
    try:
        shutil.copy(CHANGELOG_PATH / f"{distribution}.md", dst / CHANGELOG)
        with open(dst / "MANIFEST.in", "a") as f:
            f.write(f"include {CHANGELOG}\n")
    except FileNotFoundError:
        pass  # Ignore missing changelogs


def collect_package_data(base_path: Path) -> PackageData:
    """Generate package data for a setuptools.setup() call.

    This reflects the transformations done during copying in copy_stubs().
    """
    package_data: dict[str, list[str]] = {}
    for entry in base_path.iterdir():
        if is_ignored_distribution_file(entry):
            continue
        elif entry.is_file() and entry.suffix == ".pyi":
            pkg_name = entry.stem
            # Module -> package transformation is done while copying.
            stub_files = ["__init__.pyi"]
        elif entry.is_dir():
            pkg_name = entry.name
            stub_files = find_stub_files(str(entry))
        else:
            raise ValueError(f"Only stub files are allowed, not {entry.name!r}")
        package_data[pkg_name + SUFFIX] = [*stub_files, META]
    pkg_data = PackageData(base_path, package_data)
    for package in pkg_data.top_level_non_namespace_packages:
        pkg_data.add_file(package, "py.typed")
    return pkg_data


def is_ignored_distribution_file(entry: Path) -> bool:
    if entry.is_file():
        if entry.name == META:
            return True
        if entry.suffix in (".md", ".rst"):
            return True
        if (
            subprocess.run(
                ["git", "check-ignore", entry.name], cwd=str(entry.parent)
            ).returncode
            == 0
        ):
            return True
    elif entry.is_dir():
        if entry.name == TESTS_NAMESPACE:
            return True
    return False


def generate_setup_file(pkg_data: PackageData) -> str:
    """Auto-generate a setup.py file for given distribution using a template."""
    return SETUP_TEMPLATE.format(package_data=pkg_data.package_data)


def generate_pyproject_file(
    ts_data: TypeshedData,
    build_data: BuildData,
    pkg_data: PackageData,
    metadata: Metadata,
    version: str,
) -> str:
    """Auto-generate a setup.py file for given distribution using a template."""
    all_requirements = [
        str(req) for req in metadata.requires_typeshed + metadata.requires_external
    ]
    requires_python = (
        metadata.requires_python
        if metadata.requires_python is not None
        else f">={ts_data.oldest_supported_python}"
    )
    return PYPROJECT_TEMPLATE.format(
        distribution=build_data.distribution,
        stub_distribution=metadata.stub_distribution,
        long_description=generate_long_description(
            build_data.distribution, ts_data, metadata
        ),
        version=version,
        requires=all_requirements,
        packages=pkg_data.top_level_packages,
        requires_python=requires_python,
    )


def generate_long_description(
    distribution: str, ts_data: TypeshedData, metadata: Metadata
) -> str:
    commit = ts_data.read_current_commit()

    extra_description = metadata.extra_description.strip()
    parts: list[str] = []

    if metadata.upstream_repository is not None:
        formatted_distribution = f"[`{distribution}`]({metadata.upstream_repository})"
    else:
        formatted_distribution = f"`{distribution}`"

    parts.append(
        DESCRIPTION_INTRO_TEMPLATE.format(
            distribution=distribution,
            formatted_distribution=formatted_distribution,
            stub_distribution=metadata.stub_distribution,
            typeshed_version_spec=metadata.version_spec,
        )
    )
    if extra_description:
        parts.append(extra_description)
    if metadata.obsolete_since:
        parts.append(
            OBSOLETE_SINCE_TEXT_TEMPLATE.format(
                distribution=distribution,
                stub_distribution=metadata.stub_distribution,
                obsolete_since=metadata.obsolete_since,
            )
        )
    elif metadata.no_longer_updated:
        parts.append(
            NO_LONGER_UPDATED_TEMPLATE.format(
                stub_distribution=metadata.stub_distribution
            )
        )
    if metadata.partial:
        parts.append(PARTIAL_STUBS_DESCRIPTION)
    parts.append(
        DESCRIPTION_OUTRO_TEMPLATE.format(
            distribution=distribution,
            commit=commit,
            ts_data=ts_data,
        )
    )
    return "\n\n".join(parts)


def main(
    typeshed_dir: str, distribution: str, version: str, build_dir: str | None = None
) -> str:
    """Generate a wheel for a third-party distribution in typeshed.

    Return the path to directory where wheel is created.

    Note: the caller should clean the temporary directory where wheel is
    created after uploading it.
    """
    ts_data = read_typeshed_data(Path(typeshed_dir))
    # TODO: Merge BuildData and PackageData and encapsulate MetaData.
    # See also https://github.com/typeshed-internal/stub_uploader/issues/123
    build_data = BuildData(typeshed_dir, distribution)
    metadata = read_metadata(typeshed_dir, distribution)
    pkg_data = collect_package_data(build_data.stub_dir)

    if build_dir:
        tmpdir = Path(build_dir)
    else:
        tmpdir = Path(tempfile.mkdtemp())

    (tmpdir / "setup.py").write_text(generate_setup_file(pkg_data))
    (tmpdir / "pyproject.toml").write_text(
        generate_pyproject_file(ts_data, build_data, pkg_data, metadata, version)
    )
    copy_stubs(build_data.stub_dir, tmpdir)
    create_py_typed(metadata, pkg_data, tmpdir)
    (tmpdir / "README.md").write_text(
        generate_long_description(distribution, ts_data, metadata)
    )
    copy_license(ts_data, tmpdir)
    copy_changelog(distribution, tmpdir)

    print(f"\033[0;33mRunning '{sys.executable} -m build --no-isolation' in {tmpdir}")
    print()
    subprocess.run(["pip freeze | egrep 'build|twine'"], shell=True)
    print("\033[0m")
    subprocess.run(
        [sys.executable, "-m", "build", "--no-isolation"],
        cwd=tmpdir,
    )
    return f"{tmpdir}/dist"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-dir", default=None, help="build directory")
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("version", help="New stub version")
    args = parser.parse_args()
    print(
        "Wheel is built in:",
        main(args.typeshed_dir, args.distribution, args.version, args.build_dir),
    )
