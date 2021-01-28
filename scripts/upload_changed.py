"""
Entry point for scheduled GitHub auto-upload action.

This does three things:
* Reads the list of stub packages modified since last commit in typeshed
* Checks what is the current stub version increment for each package on PyPI
* Bumps the increment, builds and uploads (unless run with --dry-run) each
  new package to PyPI
"""

import argparse
import os
import subprocess

from scripts import get_version
from scripts import build_wheel
from scripts import get_changed


def main(typeshed_dir: str, commit: str, dry_run: bool = False) -> None:
    """Upload stub typeshed packages modified since commit."""
    changed = get_changed.main(typeshed_dir, commit)
    for distribution in changed:
        # Setting base version to None, so it will be read from current METADATA.toml.
        increment = get_version.main(typeshed_dir, distribution, None)
        increment += 1
        temp_dir = build_wheel.main(typeshed_dir, distribution, increment)
        if dry_run:
            print(f"Would upload: {distribution}, increment {increment}")
            continue
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("previous_commit", help="Previous typeshed commit for which we performed upload")
    parser.add_argument("--dry-run", action="store_true", help="Should we perform a dry run (don't actually upload)")
    args = parser.parse_args()
    main(args.typeshed_dir, args.previous_commit, args.dry_run)
