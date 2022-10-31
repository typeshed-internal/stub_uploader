"""
Basic script to generate a wheel for a third-party distribution in typeshed.

This generates a PEP 561 types stub package using METADATA.toml file for a given
distribution in typeshed stubs. Such package can be used by type-checking tools
like mypy, PyCharm, pytype etc. to check code that uses the corresponding runtime
Python package.

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
import tempfile
from textwrap import dedent
from typing import Optional

from stub_uploader.const import (
    CHANGELOG_PATH,
    META,
    TESTS_NAMESPACE,
    THIRD_PARTY_NAMESPACE,
)
from stub_uploader.metadata import Metadata, read_metadata

CHANGELOG = "CHANGELOG.md"

SUFFIX = "-stubs"

SETUP_TEMPLATE = dedent(
    """
from setuptools import setup

name = "types-{distribution}"
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
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
"""
).lstrip()

NO_LONGER_UPDATED_TEMPLATE = """
*Note:* `types-{distribution}` is unmaintained and won't be updated.
""".lstrip()

OBSOLETE_SINCE_TEXT_TEMPLATE = """
*Note:* The `{distribution}` package includes type annotations or type stubs
since version {obsolete_since}. Please uninstall the `types-{distribution}`
package if you use this or a newer version.
""".lstrip()

DESCRIPTION_INTRO_TEMPLATE = """
## Typing stubs for {distribution}

This is a PEP 561 type stub package for the `{distribution}` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `{distribution}`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/{distribution}. All fixes for
types and metadata should be contributed there.
""".strip()

DESCRIPTION_OUTRO_TEMPLATE = """
See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `{commit}`.
""".strip()


class BuildData:
    def __init__(self, typeshed_dir: str, distribution: str) -> None:
        self.distribution = distribution
        self.stub_dir = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution)


def find_stub_files(top: str) -> list[str]:
    """Find all stub files for a given package, relative to package root.

    Raise if we find any unknown file extensions during collection.
    """
    result = []
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
                    raise ValueError(f"Only stub files are allowed, not {file}")
    return sorted(result)


def copy_stubs(base_dir: str, dst: str) -> None:
    """Copy stubs for given distribution to the build directory.

    For packages change name by appending "-stubs" suffix (PEP 561),
    also convert modules to trivial packages with a single __init__.pyi.
    """
    for entry in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                continue
            stub_dir = os.path.join(dst, entry.split(".")[0] + SUFFIX)
            os.mkdir(stub_dir)
            shutil.copy(
                os.path.join(base_dir, entry), os.path.join(stub_dir, "__init__.pyi")
            )
        else:
            if entry == TESTS_NAMESPACE:
                # Don't package tests for the stubs
                continue
            stub_dir = os.path.join(dst, entry + SUFFIX)
            shutil.copytree(os.path.join(base_dir, entry), stub_dir)

        # We add original METADATA file in case some type-checking tool will want
        # to use it. Note that since it is not easy to package it outside of a package,
        # we copy it to every package in given distribution.
        if os.path.isfile(os.path.join(base_dir, META)):
            shutil.copy(os.path.join(base_dir, META), stub_dir)
        else:
            upper_dir = os.path.dirname(base_dir)
            assert os.path.isfile(os.path.join(upper_dir, META))
            shutil.copy(os.path.join(upper_dir, META), stub_dir)


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


def collect_setup_entries(base_dir: str) -> dict[str, list[str]]:
    """Generate package data for a setuptools.setup() call.

    This reflects the transformations done during copying in copy_stubs().
    """
    package_data = {}
    for entry in os.listdir(base_dir):
        if entry == META:
            # Metadata file entry is added at the end.
            continue
        original_entry = entry
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                if not entry.endswith((".md", ".rst")):
                    if (
                        subprocess.run(
                            ["git", "check-ignore", entry], cwd=base_dir
                        ).returncode
                        != 0
                    ):
                        raise ValueError(f"Only stub files are allowed: {entry}")
                continue
            entry = entry.split(".")[0] + SUFFIX
            # Module -> package transformation is done while copying.
            package_data[entry] = ["__init__.pyi"]
        else:
            if entry == TESTS_NAMESPACE:
                continue
            entry += SUFFIX
            package_data[entry] = find_stub_files(
                os.path.join(base_dir, original_entry)
            )
        package_data[entry].append(META)
    return package_data


def generate_setup_file(
    build_data: BuildData, metadata: Metadata, version: str, commit: str
) -> str:
    """Auto-generate a setup.py file for given distribution using a template."""
    all_requirements = [
        str(req) for req in metadata.requires_typeshed + metadata.requires_external
    ]
    package_data = collect_setup_entries(build_data.stub_dir)
    return SETUP_TEMPLATE.format(
        distribution=build_data.distribution,
        long_description=generate_long_description(
            build_data.distribution, commit, metadata
        ),
        version=version,
        requires=all_requirements,
        packages=list(package_data.keys()),
        package_data=package_data,
    )


def generate_long_description(
    distribution: str, commit: str, metadata: Metadata
) -> str:
    extra_description = metadata.extra_description.strip()
    parts = []
    parts.append(DESCRIPTION_INTRO_TEMPLATE.format(distribution=distribution))
    if extra_description:
        parts.append(extra_description)
    if metadata.obsolete_since:
        parts.append(
            OBSOLETE_SINCE_TEXT_TEMPLATE.format(
                distribution=distribution, obsolete_since=metadata.obsolete_since
            )
        )
    elif metadata.no_longer_updated:
        parts.append(NO_LONGER_UPDATED_TEMPLATE.format(distribution=distribution))
    parts.append(DESCRIPTION_OUTRO_TEMPLATE.format(commit=commit))
    return "\n\n".join(parts)


def main(
    typeshed_dir: str, distribution: str, version: str, build_dir: Optional[str] = None
) -> str:
    """Generate a wheel for a third-party distribution in typeshed.

    Return the path to directory where wheel is created.

    Note: the caller should clean the temporary directory where wheel is
    created after uploading it.
    """
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
        f.write(generate_setup_file(build_data, metadata, version, commit))
    copy_stubs(build_data.stub_dir, tmpdir)
    copy_changelog(distribution, tmpdir)
    current_dir = os.getcwd()
    os.chdir(tmpdir)
    subprocess.run(["python3", "setup.py", "bdist_wheel"])
    subprocess.run(["python3", "setup.py", "sdist"])
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
