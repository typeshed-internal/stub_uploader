import os
from typing import Any, Dict

import toml

from scripts import get_version

from .const import META, THIRD_PARTY_NAMESPACE


Metadata = Dict[str, Any]


def read_metadata(typeshed_dir: str, distribution: str) -> Metadata:
    """Parse metadata from file."""
    file = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution, META)
    with open(file) as f:
        return dict(toml.loads(f.read()))


def determine_version(typeshed_dir: str, distribution: str) -> str:
    metadata = read_metadata(typeshed_dir, distribution)
    version: str = metadata["version"]
    # Setting base version to None, so it will be read from current METADATA.toml.
    increment = get_version.main(typeshed_dir, distribution, None)
    if increment >= 0:
        print(f"Existing version found for {distribution}")
    increment += 1
    return f"{version}.{increment}"
