import os
from typing import Any, Dict

import toml

from stub_uploader import get_version

from .const import META, THIRD_PARTY_NAMESPACE


Metadata = Dict[str, Any]


def read_metadata(typeshed_dir: str, distribution: str) -> Metadata:
    """Parse metadata from file."""
    file = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution, META)
    with open(file) as f:
        return dict(toml.loads(f.read()))


def determine_version(typeshed_dir: str, distribution: str) -> str:
    version = get_version.read_base_version(typeshed_dir, distribution)
    increment = get_version.main(typeshed_dir, distribution, version)
    if increment >= 0:
        print(f"Existing version found for {distribution}")
    increment += 1
    return f"{version}.{increment}"
