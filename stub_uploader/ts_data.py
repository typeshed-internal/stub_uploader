"""
Information about typeshed.
"""

from __future__ import annotations
import argparse
from collections.abc import Iterable
from dataclasses import dataclass, fields
from packaging.requirements import Requirement
from pathlib import Path
from tomli import load as toml_load


REQUIREMENTS = "requirements-tests.txt"
PYPROJECT = "pyproject.toml"


@dataclass
class TypeshedData:
    mypy_version: str
    pyright_version: str
    pytype_version: str


def read_typeshed_data(typeshed_dir: Path) -> TypeshedData:
    with (typeshed_dir / PYPROJECT).open("rb") as f:
        pyproject = toml_load(f)
    with (typeshed_dir / REQUIREMENTS).open() as f:
        requirements = parse_requirements(f)
    return TypeshedData(
        mypy_version=requirements["mypy"],
        pyright_version=pyproject["tool"]["typeshed"]["pyright_version"],
        pytype_version=requirements["pytype"],
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
        if len(req.specifier) != 1 or not str(req.specifier).startswith("=="):
            continue
        requirements[req.name] = str(req.specifier)[2:]
    return requirements


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    args = parser.parse_args()
    data = read_typeshed_data(Path(args.typeshed_dir))
    for field in fields(data):
        print(f"{field.name}: {getattr(data, field.name)}")
