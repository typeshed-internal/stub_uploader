import argparse
import os
import subprocess

from scripts import get_version
from scripts import build_wheel
from scripts import get_changed


def main(commit: str, dry_run: bool = False) -> None:
    changed = get_changed.main(commit)
    for distribution in changed:
        increment = get_version.main(distribution, None)
        increment += 1
        temp_dir = build_wheel.main(distribution, increment)
        if dry_run:
            print(f"Would upload: {distribution}, increment {increment}")
            continue
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("previous_commit", help="Previous typeshed commit for which we performed upload")
    parser.add_argument("--dry-run", action="store_true", help="Should we perform a dry run (don't actually upload)")
    args = parser.parse_args()
    main(args.previous_commit, args.dry_run)
