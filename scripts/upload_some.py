"""
Entry point for manual GitHub upload action.

This does three things:
* Finds all distributions with names that match the pattern provided
* Checks what is the current stub version increment for each package on PyPI
* Bumps the increment, builds and uploads the each new package to PyPI
"""

import argparse
import os
import re
import subprocess

from scripts import get_version
from scripts import build_wheel


def main(typeshed_dir: str, pattern: str) -> None:
    """Force upload typeshed stub packages to PyPI."""
    compiled = re.compile(f"^{pattern}$")  # force exact matches
    for distribution in os.listdir(os.path.join(typeshed_dir, "stubs")):
        if not re.match(compiled, distribution):
            continue
        # Setting base version to None, so it will be read from current METADATA.toml.
        increment = get_version.main(typeshed_dir, distribution, version=None)
        increment += 1
        temp_dir = build_wheel.main(typeshed_dir, distribution, increment)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("pattern", help="Pattern to select distributions for upload")
    args = parser.parse_args()
    main(args.typeshed_dir, args.pattern)
