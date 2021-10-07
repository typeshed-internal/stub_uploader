"""
Entry point for manual GitHub upload action.

This does following things:
* Finds all distributions with names that match the pattern provided
* Checks what is the current stub version increment for each package on PyPI
* Bumps the increment, builds and uploads the each new package to PyPI
* Verifies validity of stub dependencies, and updates known dependencies if needed
"""

import argparse
import os
import re
import subprocess

from scripts import build_wheel
from scripts.metadata import determine_version, read_metadata


def main(typeshed_dir: str, pattern: str, uploaded: str) -> None:
    """Force upload typeshed stub packages to PyPI."""
    compiled = re.compile(f"^{pattern}$")  # force exact matches
    matching = [
        d
        for d in os.listdir(os.path.join(typeshed_dir, "stubs"))
        if re.match(compiled, d)
    ]
    # Sort by dependency to prevent depending on foreign distributions.
    to_upload = build_wheel.sort_by_dependency(
        build_wheel.make_dependency_map(typeshed_dir, matching)
    )
    print("Uploading stubs for:", ", ".join(to_upload))
    for distribution in to_upload:
        version = determine_version(typeshed_dir, distribution)
        for dependency in read_metadata(typeshed_dir, distribution).get("requires", []):
            build_wheel.verify_dependency(typeshed_dir, dependency, uploaded)
        # TODO: Update changelog
        temp_dir = build_wheel.main(typeshed_dir, distribution, version)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")], check=True)
        build_wheel.update_uploaded(uploaded, distribution)
        print(f"Successfully uploaded stubs for {distribution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "pattern", help="Regular expression to select distributions for upload"
    )
    parser.add_argument(
        "uploaded",
        help="File listing previously uploaded packages to validate dependencies",
    )
    args = parser.parse_args()
    main(args.typeshed_dir, args.pattern, args.uploaded)
