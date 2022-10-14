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

from stub_uploader.upload import upload


def main(typeshed_dir: str, pattern: str) -> None:
    """Force upload typeshed stub packages to PyPI."""
    compiled = re.compile(f"^{pattern}$")  # force exact matches
    matching = [
        d
        for d in os.listdir(os.path.join(typeshed_dir, "stubs"))
        if re.match(compiled, d)
    ]
    # TODO: Update changelog by providing the "commit" argument
    upload(typeshed_dir, matching)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "pattern", help="Regular expression to select distributions for upload"
    )
    args = parser.parse_args()
    main(args.typeshed_dir, args.pattern)
