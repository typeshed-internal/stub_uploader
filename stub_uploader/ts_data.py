"""
Information about typeshed.
"""

from __future__ import annotations
import argparse
from dataclasses import dataclass, fields
from pathlib import Path
from tomllib import load as toml_load
from typing import Any


REQUIREMENTS = "requirements-tests.txt"
PYPROJECT = "pyproject.toml"


@dataclass
class TypeshedData:
    mypy_version: str
    pyright_version: str
    pytype_version: str


def read_typeshed_data(typeshed_dir: Path) -> TypeshedData:
    pyproject = _read_pyproject_toml(typeshed_dir / PYPROJECT)
    requirements = _read_requirements(typeshed_dir / REQUIREMENTS)
    return TypeshedData(
        mypy_version=requirements["mypy"],
        pyright_version=pyproject["tool"]["typeshed"]["pyright_version"],
        pytype_version=requirements["pytype"],
    )


def _read_pyproject_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as f:
        return toml_load(f)


def _read_requirements(path: Path) -> dict[str, str]:
    requirements = {}
    with path.open() as f:
        for line in f:
            line = line.strip()
            line = line.split("#")[0]  # strip comments
            line = line.split(";")[0]  # strip extras
            if not line.strip():  # skip empty lines
                continue
            if "==" in line:
                name, version = line.split("==")
            else:
                name = line
                version = ""
            requirements[name.strip()] = version.strip()
    return requirements


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("typeshed_dir", help="Path to typeshed checkout directory")
    args = parser.parse_args()
    data = read_typeshed_data(Path(args.typeshed_dir))
    for field in fields(data):
        print(f"{field.name}: {getattr(data, field.name)}")
