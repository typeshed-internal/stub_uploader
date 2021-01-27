import argparse
import os
import re
import subprocess

from scripts import get_version
from scripts import build_wheel


def main(pattern: str) -> None:
    compiled = re.compile(pattern)
    for distribution in os.listdir("stubs"):
        if not re.match(compiled, distribution):
            continue
        increment = get_version.main(distribution, None)
        increment += 1
        temp_dir = build_wheel.main(distribution, increment)
        subprocess.run(["twine", "upload", os.path.join(temp_dir, "*")])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="Pattern to select distributions for upload")
    args = parser.parse_args()
    main(args.pattern)
