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
from typing import Optional

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

name = "{stub_distribution}"
description = "Typing stubs for {distribution}"
long_description = '''
{long_description}
'''.lstrip()

setup(name=name,
      version="{version}",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={{
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/{distribution}.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      }},
      install_requires={requires},
      packages={packages},
      package_data={package_data},
      license="Apache-2.0 license",
      python_requires="{requires_python}",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
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
PyCharm, etc. to check code that uses
`{distribution}`.

This version of `{stub_distribution}` aims to provide accurate annotations
for `{distribution}=={typeshed_version_pin}`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/{distribution}. All fixes for
types and metadata should be contributed there.
""".strip()

DESCRIPTION_OUTRO_TEMPLATE = """
See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `{commit}` and was tested
with mypy {ts_data.mypy_version}, pyright {ts_data.pyright_version}, and
pytype {ts_data.pytype_version}.
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

    @property
    def top_level_packages(self) -> list[str]:
        """Top level package names.

        These are the packages that are not subpackages of any other package
        and includes namespace packages.
        """
        return list(self.package_data.keys())

    def add_file(self, package: str, filename: str, file_contents: str) -> None:
        """Add a file to a package."""
        entry_path = self.base_path / package
        entry_path.mkdir(exist_ok=True)
        (entry_path / filename).write_text(file_contents)
        self.package_data[package].append(filename)


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


def copy_changelog(distribution: str, dst: str) -> None:
    """Copy changelog to the build directory."""
    try:
        shutil.copy(
            os.path.join(CHANGELOG_PATH, f"{distribution}.md"),
            os.path.join(dst, CHANGELOG),
        )
        with open(os.path.join(dst, "MANIFEST.in"), "a") as f:
            f.write(f"include {CHANGELOG}\n")
    except FileNotFoundError:
        pass  # Ignore missing changelogs


def collect_package_data(base_path: Path) -> PackageData:
    """Generate package data for a setuptools.setup() call.

    This reflects the transformations done during copying in copy_stubs().
    """
    package_data: dict[str, list[str]] = {}
    for entry in base_path.iterdir():
        if entry.name == META:
            # Metadata file entry is added at the end.
            continue
        original_entry = entry
        if entry.is_file():
            if entry.suffix != ".pyi":
                if entry.suffix not in (".md", ".rst"):
                    if (
                        subprocess.run(
                            ["git", "check-ignore", entry.name], cwd=str(base_path)
                        ).returncode
                        != 0
                    ):
                        raise ValueError(
                            f"Only stub files are allowed, not {entry.name!r}"
                        )
                continue
            pkg_name = entry.name.split(".")[0] + SUFFIX
            # Module -> package transformation is done while copying.
            package_data[pkg_name] = ["__init__.pyi"]
        else:
            if entry.name == TESTS_NAMESPACE:
                continue
            pkg_name = entry.name + SUFFIX
            package_data[pkg_name] = find_stub_files(str(original_entry))
        package_data[pkg_name].append(META)
    return PackageData(base_path, package_data)


def add_partial_markers(pkg_data: PackageData) -> None:
    for package in pkg_data.top_level_packages:
        pkg_data.add_file(package, "py.typed", "partial\n")


def generate_setup_file(
    build_data: BuildData,
    ts_data: TypeshedData,
    metadata: Metadata,
    version: str,
    commit: str,
) -> str:
    """Auto-generate a setup.py file for given distribution using a template."""
    all_requirements = [
        str(req) for req in metadata.requires_typeshed + metadata.requires_external
    ]
    pkg_data = collect_package_data(build_data.stub_dir)
    if metadata.partial:
        add_partial_markers(pkg_data)
    requires_python = (
        metadata.requires_python
        if metadata.requires_python is not None
        else f">={ts_data.oldest_supported_python}"
    )
    return SETUP_TEMPLATE.format(
        distribution=build_data.distribution,
        stub_distribution=metadata.stub_distribution,
        long_description=generate_long_description(
            build_data.distribution, commit, ts_data, metadata
        ),
        version=version,
        requires=all_requirements,
        packages=pkg_data.top_level_packages,
        package_data=pkg_data.package_data,
        requires_python=requires_python,
    )


def generate_long_description(
    distribution: str, commit: str, ts_data: TypeshedData, metadata: Metadata
) -> str:
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
            typeshed_version_pin=metadata.version_spec,
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
    parts.append(DESCRIPTION_OUTRO_TEMPLATE.format(commit=commit, ts_data=ts_data))
    return "\n\n".join(parts)


def main(
    typeshed_dir: str, distribution: str, version: str, build_dir: Optional[str] = None
) -> str:
    """Generate a wheel for a third-party distribution in typeshed.

    Return the path to directory where wheel is created.

    Note: the caller should clean the temporary directory where wheel is
    created after uploading it.
    """
    ts_data = read_typeshed_data(Path(typeshed_dir))
    build_data = BuildData(typeshed_dir, distribution)
    if build_dir:
        tmpdir = build_dir
    else:
        tmpdir = tempfile.mkdtemp()
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        cwd=typeshed_dir,
    ).stdout.strip()
    metadata = read_metadata(typeshed_dir, distribution)
    with open(os.path.join(tmpdir, "setup.py"), "w") as f:
        f.write(generate_setup_file(build_data, ts_data, metadata, version, commit))
    copy_stubs(build_data.stub_dir, Path(tmpdir))
    copy_changelog(distribution, tmpdir)
    current_dir = os.getcwd()
    os.chdir(tmpdir)
    subprocess.run([sys.executable, "setup.py", "bdist_wheel"])
    subprocess.run([sys.executable, "setup.py", "sdist"])
    os.chdir(current_dir)
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
