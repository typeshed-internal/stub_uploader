"""
Information about typeshed.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable
from dataclasses import dataclass, fields
from pathlib import Path
import re
import subprocess

from packaging.requirements import Requirement
from packaging.version import Version
from tomli import load as toml_load

REQUIREMENTS = "requirements-tests.txt"
PYPROJECT = "pyproject.toml"


@dataclass
class TypeshedData:
    typeshed_path: Path
    mypy_version: Version
    pyright_version: Version
    pytype_version: Version
    oldest_supported_python: str

    def read_current_commit(self) -> str:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            cwd=self.typeshed_path,
        ).stdout.strip()


def read_typeshed_data(typeshed_path: Path) -> TypeshedData:
    with (typeshed_path / PYPROJECT).open("rb") as f:
        pyproject = toml_load(f)
    with (typeshed_path / REQUIREMENTS).open() as f:
        requirements = parse_requirements(f)
    typeshed_table = pyproject["tool"]["typeshed"]
    if not re.match(r"^\d+\.\d+$", typeshed_table["oldest_supported_python"]):
        raise ValueError("Invalid oldest_supported_python in pyproject.toml")
    return TypeshedData(
        typeshed_path=typeshed_path,
        mypy_version=Version(requirements["mypy"]),
        pyright_version=Version(requirements["pyright"]),
        pytype_version=Version(requirements["pytype"]),
        oldest_supported_python=typeshed_table["oldest_supported_python"],
    )


def parse_requirements(stream: Iterable[str]) -> dict[str, str]:
    """Parse all exact requirements from a requirements.txt file.

    Only requirements that are pinned to a specific version are returned.
    """
    requirements = {}
    for line in stream:
        line = line.strip()
        line = line.split("#")[0]  # strip comments
        if not line.strip():  # skip empty lines
            continue
        req = Requirement(line.strip())
        if len(req.specifier) != 1:
            continue
        spec = next(iter(req.specifier))
        if spec.operator != "==":
            continue
        requirements[req.name] = spec.version
    return requirements


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    args = parser.parse_args()
    data = read_typeshed_data(Path(args.typeshed_dir))
    for field in fields(data):
        print(f"{field.name}: {getattr(data, field.name)}")
