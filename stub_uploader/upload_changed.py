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
from stub_uploader import get_changed
from stub_uploader.upload import upload


def main(typeshed_dir: str, commit: str, dry_run: bool = False) -> None:
    """Upload stub typeshed packages modified since commit."""
    changed = get_changed.main(typeshed_dir, commit)
    # Ignore those distributions that were completely deleted.
    current = set(os.listdir(os.path.join(typeshed_dir, "stubs")))
    changed = [d for d in changed if d in current]
    upload(typeshed_dir, changed, commit, dry_run=dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "previous_commit", help="Previous typeshed commit for which we performed upload"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Should we perform a dry run (don't actually upload)",
    )
    args = parser.parse_args()
    main(args.typeshed_dir, args.previous_commit, args.dry_run)
