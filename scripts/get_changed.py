import argparse
import os.path
import subprocess

from typing import List


def main(commit: str) -> List[str]:
    git = subprocess.run(["git", "diff", "--name-only", "HEAD", commit],
                         capture_output=True, universal_newlines=True)
    changed = set()
    for file in git.stdout.splitlines():
        if file.startswith("stubs" + os.path.sep):
            _, distribution, *_ = file.split(os.path.sep)
            changed.add(distribution)
    return sorted(changed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("previous_commit", help="Third-party distribution to build")
    args = parser.parse_args()
    for distribution in main(args.previous_commit):
        print(distribution)
