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
    # Ignore those distributions that were completely deleted.
    current = set(os.listdir(os.path.join(typeshed_dir, "stubs")))
    changed = [d for d in changed if d in current]
    # Sort by dependency to prevent depending on foreign distributions.
    to_upload = build_wheel.sort_by_dependency(
        build_wheel.make_dependency_map(typeshed_dir, changed)
    )
    print("Building and uploading stubs for:", ", ".join(to_upload))
    for distribution in to_upload:
        # Setting base version to None, so it will be read from current METADATA.toml.
        increment = get_version.main(typeshed_dir, distribution, None)
        if increment >= 0:
            print(f"Existing version found for {distribution}")
        increment += 1
        temp_dir = build_wheel.main(typeshed_dir, distribution, increment)
        if dry_run:
            print(f"Would upload: {distribution}, increment {increment}")
            continue
        for dependency in build_wheel.read_metadata(
            os.path.join(
                typeshed_dir, build_wheel.THIRD_PARTY_NAMESPACE, distribution, build_wheel.META
            )
        ).get("requires", []):
            build_wheel.verify_dependency(typeshed_dir, dependency, uploaded)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")], check=True)
        build_wheel.update_uploaded(uploaded, distribution)
        print(f"Successfully uploaded stubs for {distribution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument("previous_commit", help="Previous typeshed commit for which we performed upload")
    parser.add_argument("uploaded", help="File listing previously uploaded packages to validate dependencies")
    parser.add_argument("--dry-run", action="store_true", help="Should we perform a dry run (don't actually upload)")
    args = parser.parse_args()
    main(args.typeshed_dir, args.previous_commit, args.uploaded, args.dry_run)
