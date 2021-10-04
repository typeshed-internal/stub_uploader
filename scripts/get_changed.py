"""
A short script to list names of distributions modified since some
typeshed commit.

This is used by scheduled GitHub auto-upload action to only upload
modified stub packages.
"""


import argparse
import os
import subprocess

from typing import List


def main(typeshed_dir: str, commit: str) -> List[str]:
    """List all distributions that changed since commit."""
    assert typeshed_dir.endswith(os.sep + "typeshed")
    git = subprocess.run(
        ["git", "diff", "--no-renames", "--name-only", "HEAD", commit],
        capture_output=True,
        universal_newlines=True,
        cwd=typeshed_dir,
        check=True,
    )
    changed = set()
    for file in git.stdout.splitlines():
        # Third party stubs live in typeshed/stubs/...
        if file.startswith("stubs" + os.path.sep):
            _, distribution, *_ = file.split(os.path.sep)
            changed.add(distribution)
    return sorted(changed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "previous_commit", help="Previous typeshed commit for which we performed upload"
    )
    args = parser.parse_args()
    for distribution in main(args.typeshed_dir, args.previous_commit):
        print(distribution)
