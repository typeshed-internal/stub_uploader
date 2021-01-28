"""
Basic script to generate a wheel for a third-party distribution in typeshed.

This generates a PEP 561 types stub package using METADATA.toml file for a given
distribution in typeshed stubs. Such package can be used by type-checking tools
like mypy, PyCharm, pytype etc. to check code that uses the corresponding runtime
Python package.

The generated wheel includes all type stubs (*.pyi files) and the METADATA.toml
itself, no other files can be included.

The types stubs live in https://github.com/python/typeshed/tree/master/stubs,
all fixes for types and metadata should be contributed there, see
https://github.com/python/typeshed/blob/master/CONTRIBUTING.md for more details.
"""

import argparse
import os
import os.path
import shutil
import tempfile
import subprocess
from textwrap import dedent
from typing import List, Dict, Any, Tuple

import toml

META = "METADATA.toml"

# These constants may be adjusted, depending on convention we agree on.
THIRD_PARTY_NAMESPACE = "stubs"
PY2_NAMESPACE = "@python2"
SUFFIX = "-stubs"
PY2_SUFFIX = "-python2-stubs"

SETUP_TEMPLATE = dedent("""
from setuptools import setup

name = "types-{distribution}"
description = "Typing stubs for {distribution}"
long_description = '''
## Typing stubs for {distribution}

This is an auto-generated PEP 561 type stub package for `{distribution}` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `{distribution}`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/{distribution}. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
'''.lstrip()

setup(name=name,
      version="{version}",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires={requires},
      packages={packages},
      package_data={package_data},
      classifiers=[
          "Typing :: Typed",
      ]
)
""").lstrip()


def find_stub_files(top: str) -> List[str]:
    """Find all stub files for a given package, relative to package root.

    Raise if we find any unknown file extensions during collection.
    """
    result = []
    for root, _, files in os.walk(top):
        for file in files:
            if file.endswith(".pyi"):
                name, _ = os.path.splitext(file)
                assert name.isidentifier(), "All file names must be valid Python modules"
                result.append(os.path.relpath(os.path.join(root, file), top))
            elif not file.endswith((".md", ".rst")):
                # Allow having README docs, as some stubs have these (e.g. click).
                raise ValueError("Only stub files are allowed")
    return result


def read_matadata(file: str) -> Dict[str, Any]:
    """Parse metadata from file."""
    with open(file) as f:
        return dict(toml.loads(f.read()))


def copy_stubs(typeshed_dir: str, distribution: str, dst: str, suffix: str) -> None:
    """Copy stubs for given distribution to a temporary directory.

    For packages change name by appending "-stubs" suffix (PEP 561),
    also convert modules to trivial packages with a single __init__.pyi.
    """
    base_dir = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution)
    for entry in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                continue
            stub_dir = os.path.join(dst, entry.split(".")[0] + suffix)
            os.mkdir(stub_dir)
            shutil.copy(os.path.join(base_dir, entry), os.path.join(stub_dir, "__init__.pyi"))
        else:
            if entry == PY2_NAMESPACE:
                # This is not really a package, but Python 2 stubs root.
                # Packages there should be copied using a separate call to this
                # function.
                continue
            else:
                stub_dir = os.path.join(dst, entry + suffix)
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


def collect_setup_entries(
        typeshed_dir: str,
        distribution: str,
        suffix: str,
) -> Tuple[List[str], Dict[str, List[str]]]:
    """Generate package data for a setuptools.setup() call.

    This reflects the transformations done during copying in copy_stubs().
    """
    packages = []
    package_data = {}
    base_dir = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution)
    for entry in os.listdir(base_dir):
        if entry == META:
            # Metadata file entry is added at the end.
            continue
        original_entry = entry
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                if not entry.endswith((".md", ".rst")):
                    raise ValueError("Only stub files are allowed")
                continue
            entry = entry.split('.')[0] + suffix
            packages.append(entry)
            # Module -> package transformation is done while copying.
            package_data[entry] = ["__init__.pyi"]
        else:
            if entry == PY2_NAMESPACE:
                # Again, Python 2 entries should be generated by
                # a separate call to this function.
                continue
            entry += suffix
            packages.append(entry)
            package_data[entry] = find_stub_files(
                os.path.join(base_dir, original_entry)
            )
        package_data[entry].append(META)
    return packages, package_data


def generate_setup_file(typeshed_dir: str, distribution: str, increment: str) -> str:
    """Auto-generate a setup.py file for given distribution using a template."""
    base_dir = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution)
    metadata = read_matadata(os.path.join(base_dir, META))
    packages, package_data = collect_setup_entries(typeshed_dir, distribution, SUFFIX)
    if PY2_NAMESPACE in os.listdir(base_dir):
        # If there are Python 2 only stubs, add entries from the sub-directory.
        py2_packages, py2_package_data = collect_setup_entries(
            typeshed_dir, os.path.join(distribution, PY2_NAMESPACE), PY2_SUFFIX
        )
        packages += py2_packages
        package_data.update(py2_package_data)
    version = metadata["version"]
    requires = metadata.get("requires", [])
    known_distributions = set(os.listdir(os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE)))
    for dependency in requires:
        assert dependency.startswith("types-"), "Only dependencies on stub packages are allowed"
        dep_name = dependency[len("types-"):]
        assert dep_name in known_distributions, "Only dependencies on typeshed stubs are allowed"
    assert version.count(".") == 1, f"Version must be major.minor, not {version}"
    return SETUP_TEMPLATE.format(
        distribution=distribution,
        version=f"{version}.{increment}",
        requires=requires,
        packages=packages,
        package_data=package_data,
    )


def main(typeshed_dir: str, distribution: str, increment: int) -> str:
    """Generate a wheel for a third-party distribution in typeshed.

    Return the path to directory where wheel is created.

    Note: the caller should clean the temporary directory where wheel is
    created after uploading it.
    """
    base_dir = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution)
    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, "setup.py"), "w") as f:
        f.write(generate_setup_file(typeshed_dir, distribution, str(increment)))
    copy_stubs(typeshed_dir, distribution, tmpdir, SUFFIX)
    if PY2_NAMESPACE in os.listdir(base_dir):
        # If there are Python 2 only stubs, copy them too.
        copy_stubs(typeshed_dir, os.path.join(distribution, PY2_NAMESPACE), tmpdir, PY2_SUFFIX)
    os.chdir(tmpdir)
    subprocess.run(["python3", "setup.py", "bdist_wheel", "--universal"])
    return f"{tmpdir}/dist"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("increment", help="Stub version increment")
    args = parser.parse_args()
    print("Wheel is built in:", main(args.typeshed_dir, args.distribution, args.increment))
