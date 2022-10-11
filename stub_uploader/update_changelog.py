#!/usr/bin/env python3

"""
This script updates the changelog for a single module.
"""

import argparse
import datetime
import os
import re
import subprocess
from pathlib import Path

from stub_uploader.const import CHANGELOG_PATH

THIRD_PARTY_NAMESPACE = "stubs"


def main() -> None:
    args = parse_args()
    update_changelog(
        args.typeshed_dir,
        args.previous_commit,
        args.distribution,
        args.version,
        dry_run=args.dry_run,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    parser.add_argument(
        "previous_commit", help="Previous typeshed commit for which we performed upload"
    )
    parser.add_argument("distribution", help="Distribution to update the changelog for")
    parser.add_argument("version", help="New version to add to the changelog")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Should we perform a dry run (don't actually update)",
    )
    return parser.parse_args()


def update_changelog(
    typeshed_dir: str,
    previous_commit: str,
    distribution: str,
    version: str,
    *,
    dry_run: bool = False,
) -> None:
    dist_path = Path(THIRD_PARTY_NAMESPACE, distribution)
    result = subprocess.run(
        ["git", "log", f"{previous_commit}..HEAD", "--", dist_path],
        cwd=typeshed_dir,
        stdout=subprocess.PIPE,
        check=True,
    )
    log = result.stdout.decode("utf-8")
    if not log:
        print(f"{distribution}: Changelog unchanged")
        return
    new_entry = process_git_log(log, version)

    changelog = os.path.join(CHANGELOG_PATH, f"{distribution}.md")
    try:
        with open(changelog) as f:
            old_entries = f.read()
    except FileNotFoundError:
        old_entries = ""

    if dry_run:
        if old_entries:
            print(
                f"Would add {len(new_entry.splitlines())} lines to existing {changelog}"
            )
        else:
            print(f"Would add {len(new_entry.splitlines())} lines to new {changelog}")
        return

    with open(changelog, "w") as f:
        f.write(new_entry + old_entries)


def process_git_log(log: str, version: str) -> str:
    today = datetime.date.today()
    entry = f"## {version} ({today:%Y-%m-%d})\n"
    for line in log.splitlines():
        if line.strip() == "":
            entry += "\n"
        elif line.startswith("    "):
            # Proper git log lines start with four spaces.
            entry += f"{line.rstrip()[4:]}\n"
        else:
            pass  # Ignore header entries.
    entry += "\n"
    # Strip multiple empty lines.
    return re.sub("\n\n+", "\n\n", entry)


if __name__ == "__main__":
    main()
