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

_SCOPE_PREFIX_RE = re.compile(r"^\s*(\([^)]*\)|\[[^\]]*\])\s*:?\s*")
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
    today = datetime.date.today()
    new_entry = process_git_log(log, distribution, version, today)

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


def process_git_log(
    log: str, distribution: str, version: str, today: datetime.date
) -> str:
    entry = f"## [{version}](https://pypi.org/project/types-{distribution}/{version}/) ({today:%Y-%m-%d})\n"
    lines = log.splitlines()
    is_title = True
    for i, line in enumerate(lines):
        if line.strip() == "":
            entry += "\n"
            continue

        # Proper git log lines start with four spaces.
        if not line.startswith("    "):
            is_title = True
            continue  # Ignore header entries.

        if is_title:
            # Remove scope prefix: (), ():, [], []:
            title = _SCOPE_PREFIX_RE.sub("", line.rstrip()[4:])
            entry += f"* {title}\n"
            is_title = False
        else:
            # Decide whether to add ' \'
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            add_backslash = (
                next_line.strip() != ""
                and next_line.startswith("    ")
                and not next_line.lstrip().startswith(("* ", "- ", "+ ", "1. "))
            )
            if add_backslash and not line.rstrip().endswith("\\"):
                line += " \\"
            entry += f"{line.rstrip()}\n"

    entry += "\n"
    # Create hyperlinks for PR numbers.
    entry = re.sub(
        r"\(#(\d+)\)", r"([#\1](https://github.com/python/typeshed/pull/\1))", entry
    )
    # Strip multiple empty lines.
    return re.sub("\n\n+", "\n\n", entry)


if __name__ == "__main__":
    main()
