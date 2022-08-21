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

from stub_uploader import build_wheel, get_changed, update_changelog
from stub_uploader.metadata import read_metadata
from stub_uploader.get_version import determine_incremented_version


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
        metadata = read_metadata(typeshed_dir, distribution)
        version = determine_incremented_version(metadata)
        update_changelog.update_changelog(
            typeshed_dir, commit, distribution, version, dry_run=dry_run
        )
        temp_dir = build_wheel.main(typeshed_dir, distribution, version)
        if dry_run:
            print(f"Would upload: {distribution}, version {version}")
            continue
        for req in metadata.requires_typeshed:
            build_wheel.verify_typeshed_dependency(typeshed_dir, req, uploaded)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")], check=True)
        build_wheel.update_uploaded(uploaded, distribution)
        print(f"Successfully uploaded stubs for {distribution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "previous_commit", help="Previous typeshed commit for which we performed upload"
    )
    parser.add_argument(
        "uploaded",
        help="File listing previously uploaded packages to validate dependencies",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Should we perform a dry run (don't actually upload)",
    )
    args = parser.parse_args()
    main(args.typeshed_dir, args.previous_commit, args.uploaded, args.dry_run)
