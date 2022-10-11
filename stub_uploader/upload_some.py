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

from stub_uploader import build_wheel
from stub_uploader.get_version import determine_incremented_version
from stub_uploader.metadata import (
    read_metadata,
    recursive_verify,
    sort_by_dependency,
    uploaded_packages,
)


def main(typeshed_dir: str, pattern: str) -> None:
    """Force upload typeshed stub packages to PyPI."""
    compiled = re.compile(f"^{pattern}$")  # force exact matches
    matching = [
        d
        for d in os.listdir(os.path.join(typeshed_dir, "stubs"))
        if re.match(compiled, d)
    ]
    to_upload = sort_by_dependency(typeshed_dir, matching)

    print("Uploading stubs for:", ", ".join(to_upload))
    for distribution in to_upload:
        metadata = read_metadata(typeshed_dir, distribution)
        recursive_verify(metadata, typeshed_dir)

        version = determine_incremented_version(metadata)

        # TODO: Update changelog
        temp_dir = build_wheel.main(typeshed_dir, distribution, version)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")], check=True)
        uploaded_packages.add(distribution)
        print(f"Successfully uploaded stubs for {distribution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "pattern", help="Regular expression to select distributions for upload"
    )
    args = parser.parse_args()
    main(args.typeshed_dir, args.pattern)
