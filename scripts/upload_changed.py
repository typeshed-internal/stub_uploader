"""
Entry point for scheduled GitHub auto-upload action.

This does following things:
* Reads the list of stub packages modified since last commit in typeshed
* Checks what is the current stub version increment for each package on PyPI
* Bumps the increment, builds and uploads (unless run with --dry-run) each
  new package to PyPI
* Verifies validity of stub dependencies, and updates known dependencies if needed
"""

import argparse
import os
import subprocess

from scripts import get_version
from scripts import build_wheel
from scripts import get_changed


def main(typeshed_dir: str, commit: str, uploaded: str, dry_run: bool = False) -> None:
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
        for dependency in build_wheel.read_matadata(
            os.path.join(typeshed_dir, build_wheel.THIRD_PARTY_NAMESPACE, distribution)
        ).get("requires", []):
            if get_version.check_exists(get_version.strip_dep_version(dependency)):
                # If this dependency is already present, check it was uploaded by us.
                build_wheel.verify_dependency(typeshed_dir, dependency, uploaded)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")], check=True)
        build_wheel.update_uploaded(uploaded, distribution)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("previous_commit", help="Previous typeshed commit for which we performed upload")
    parser.add_argument("uploaded", help="Previously uploaded packages to validate dependencies")
    parser.add_argument("--dry-run", action="store_true", help="Should we perform a dry run (don't actually upload)")
    args = parser.parse_args()
    main(args.typeshed_dir, args.previous_commit, args.uploaded, args.dry_run)
