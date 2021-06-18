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

This file also contains some helper functions related to wheel validation and upload.
"""

import argparse
import os
import os.path
import shutil
import tempfile
import subprocess
from collections import defaultdict
from functools import cmp_to_key
from glob import glob
from textwrap import dedent
from typing import List, Dict, Any, Tuple, Set

from scripts import get_version

import toml

META = "METADATA.toml"

# These constants may be adjusted, depending on convention we agree on.
THIRD_PARTY_NAMESPACE = "stubs"
PY2_NAMESPACE = "@python2"
TESTS_NAMESPACE = "@tests"
SUFFIX = "-stubs"
PY2_SUFFIX = "-python2-stubs"

SETUP_TEMPLATE = dedent("""
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
      install_requires={requires},
      packages={packages},
      package_data={package_data},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
""").lstrip()

OBSOLETE_TEXT_TEMPLATE = """
*Note:* The `{distribution}` package includes type annotations or type stubs
since version {obsolete_since}. Please uninstall the `types-{distribution}`
package if you use this or a newer version.
""".lstrip()


DESCRIPTION_INTRO_TEMPLATE = """
## Typing stubs for {distribution}

This is an auto-generated PEP 561 type stub package for `{distribution}` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `{distribution}`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/{distribution}. All fixes for
types and metadata should be contributed there.
""".strip()

DESCRIPTION_OUTRO_TEMPLATE = """
See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `{commit}`.
""".strip()


class BuildData:
    def __init__(self, typeshed_dir: str, distribution: str) -> None:
        self.distribution = distribution
        self._base_dir = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution)
        self.meta_path = os.path.join(self._base_dir, META)
        # Python 3 (and mixed Python 2 and 3) stubs exist if at least one
        # *.pyi file exists on the top-level or one level down, *excluding*
        # the @python2 directory.
        self.py3_stubs = (
            len(glob(f"{self._base_dir}/*.pyi")) >= 1
            or len(glob(f"{self._base_dir}/[!@]*/*.pyi")) >= 1
        )
        # Python 2 stubs exist if a @python2 directory exists.
        self.py2_stubs = PY2_NAMESPACE in os.listdir(self._base_dir)

    @property
    def py3_stub_dir(self) -> str:
        return self._base_dir

    @property
    def py2_stub_dir(self) -> str:
        return os.path.join(self._base_dir, PY2_NAMESPACE)


def strip_types_prefix(dependency: str) -> str:
    assert dependency.startswith("types-"), "Currently only dependencies on stub packages are supported"
    return dependency[len("types-"):]


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
                raise ValueError(f"Only stub files are allowed, not {file}")
    return result


def read_metadata(file: str) -> Dict[str, Any]:
    """Parse metadata from file."""
    with open(file) as f:
        return dict(toml.loads(f.read()))


def copy_stubs(base_dir: str, dst: str, suffix: str) -> None:
    """Copy stubs for given distribution to a temporary directory.

    For packages change name by appending "-stubs" suffix (PEP 561),
    also convert modules to trivial packages with a single __init__.pyi.
    """
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
            if entry == TESTS_NAMESPACE:
                # Don't package tests for the stubs
                continue
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
        base_dir: str,
        suffix: str,
) -> Tuple[List[str], Dict[str, List[str]]]:
    """Generate package data for a setuptools.setup() call.

    This reflects the transformations done during copying in copy_stubs().
    """
    packages = []
    package_data = {}
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
            if entry == TESTS_NAMESPACE:
                continue
            entry += suffix
            packages.append(entry)
            package_data[entry] = find_stub_files(
                os.path.join(base_dir, original_entry)
            )
        package_data[entry].append(META)
    return packages, package_data


def verify_dependency(typeshed_dir: str, dependency: str, uploaded: str) -> None:
    """Verify this is a valid dependency, i.e. a stub package uploaded by us."""
    known_distributions = set(os.listdir(os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE)))
    assert ";" not in dependency, "Semicolons in dependencies are not supported"
    dependency = get_version.strip_dep_version(dependency)
    assert strip_types_prefix(dependency) in known_distributions, "Only dependencies on typeshed stubs are allowed"
    with open(uploaded) as f:
        uploaded_distributions = set(f.read().splitlines())

    msg = f"{dependency} looks like a foreign distribution."
    uploaded_distributions_lower = [d.lower() for d in uploaded_distributions]
    if dependency not in uploaded_distributions and dependency.lower() in uploaded_distributions_lower:
        msg += " Note: list is case sensitive"
    assert dependency in uploaded_distributions, msg


def update_uploaded(uploaded: str, distribution: str) -> None:
    with open(uploaded) as f:
        current = set(f.read().splitlines())
    if f"types-{distribution}" not in current:
        with open(uploaded, "w") as f:
            f.write("\n".join(sorted(current | {f"types-{distribution}"})))


def make_dependency_map(typeshed_dir: str, distributions: List[str]) -> Dict[str, Set[str]]:
    """Return relative dependency map among distributions.

    Important: this only includes dependencies *within* the given
    list of distributions.
    """
    result: Dict[str, Set[str]] = {d: set() for d in distributions}
    for distribution in distributions:
        data = read_metadata(
            os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution, META)
        )
        for dependency in data.get("requires", []):
            dependency = strip_types_prefix(get_version.strip_dep_version(dependency))
            if dependency in distributions:
                result[distribution].add(dependency)
    return result


def transitive_deps(dep_map: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """Propagate dependencies to compute a transitive dependency map.

    Note: this algorithm is O(N**2) in general case, but we don't worry,
    because N is small (less than 1000). So it will take few seconds at worst,
    while building/uploading 1000 packages will take minutes.
    """
    transitive: Dict[str, Set[str]] = defaultdict(set)
    for distribution in dep_map:
        to_add = {distribution}
        while to_add:
            new = to_add.pop()
            extra = dep_map[new]
            transitive[distribution] |= extra
            assert distribution not in transitive[distribution], f"Cyclic dependency {distribution} -> {distribution}"
            to_add |= extra
    return transitive


def sort_by_dependency(dep_map: Dict[str, Set[str]]) -> List[str]:
    """Sort distributions by dependency order (those depending on nothing appear first)."""
    trans_map = transitive_deps(dep_map)

    # We can't use builtin sort w.r.t. trans_map because it makes various assumptions
    # about properties of equality and order (like their mutual transitivity).
    def sort(ds: List[str]) -> List[str]:
        if not ds:
            return []
        pivot = ds.pop()
        not_dependent = [d for d in ds if pivot not in trans_map[d]]
        dependent = [d for d in ds if pivot in trans_map[d]]
        return sort(not_dependent) + [pivot] + sort(dependent)

    # Return independent packages sorted by name for stability.
    return sort(sorted(dep_map))


def generate_setup_file(build_data: BuildData, increment: str, commit: str) -> str:
    """Auto-generate a setup.py file for given distribution using a template."""
    metadata = read_metadata(build_data.meta_path)
    packages = []
    package_data = {}
    if build_data.py3_stubs:
        py3_packages, py3_package_data = collect_setup_entries(
            build_data.py3_stub_dir, SUFFIX
        )
        packages += py3_packages
        package_data.update(py3_package_data)
    if build_data.py2_stubs:
        # If there are Python 2 only stubs, add entries from the sub-directory.
        py2_packages, py2_package_data = collect_setup_entries(
            build_data.py2_stub_dir, PY2_SUFFIX
        )
        packages += py2_packages
        package_data.update(py2_package_data)
    version = metadata["version"]
    assert version.count(".") == 1, f"Version must be major.minor, not {version}"
    return SETUP_TEMPLATE.format(
        distribution=build_data.distribution,
        long_description=generate_long_description(build_data.distribution, commit, metadata),
        version=f"{version}.{increment}",
        requires=metadata.get("requires", []),
        packages=packages,
        package_data=package_data,
    )


def generate_long_description(
        distribution: str, commit: str, metadata: Dict[str, Any]
) -> str:
    extra_description = metadata.get("extra_description", "").strip()
    parts = []
    parts.append(DESCRIPTION_INTRO_TEMPLATE.format(distribution=distribution))
    if extra_description:
        parts.append(extra_description)
    if "obsolete_since" in metadata:
        parts.append(OBSOLETE_TEXT_TEMPLATE.format(
            distribution=distribution,
            obsolete_since=metadata["obsolete_since"]
        ))
    parts.append(DESCRIPTION_OUTRO_TEMPLATE.format(commit=commit))
    return "\n\n".join(parts)


def main(typeshed_dir: str, distribution: str, increment: int) -> str:
    """Generate a wheel for a third-party distribution in typeshed.

    Return the path to directory where wheel is created.

    Note: the caller should clean the temporary directory where wheel is
    created after uploading it.
    """
    build_data = BuildData(typeshed_dir, distribution)
    assert build_data.py3_stubs or build_data.py2_stubs, "no stubs found"
    tmpdir = tempfile.mkdtemp()
    commit = subprocess.run(["git", "rev-parse", "HEAD"],
                            capture_output=True, universal_newlines=True, cwd=typeshed_dir
                            ).stdout.strip()
    with open(os.path.join(tmpdir, "setup.py"), "w") as f:
        f.write(generate_setup_file(build_data, str(increment), commit))
    if build_data.py3_stubs:
        copy_stubs(build_data.py3_stub_dir, tmpdir, SUFFIX)
    if build_data.py2_stubs:
        # If there are Python 2 only stubs, copy them too.
        copy_stubs(build_data.py2_stub_dir, tmpdir, PY2_SUFFIX)
    current_dir = os.getcwd()
    os.chdir(tmpdir)
    universal_args = []
    if build_data.py2_stubs and build_data.py3_stubs:
        universal_args.append("--universal")
    subprocess.run(["python3", "setup.py", "bdist_wheel"] + universal_args)
    subprocess.run(["python3", "setup.py", "sdist"])
    os.chdir(current_dir)
    return f"{tmpdir}/dist"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("increment", help="Stub version increment")
    args = parser.parse_args()
    print("Wheel is built in:", main(args.typeshed_dir, args.distribution, args.increment))
