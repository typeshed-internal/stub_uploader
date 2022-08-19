import os
from typing import Any, Dict, List, Optional

import tomli

from stub_uploader import get_version

from .const import META, THIRD_PARTY_NAMESPACE


class Metadata:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @classmethod
    def from_file(cls, path: str) -> "Metadata":
        with open(path, "rb") as f:
            return cls(tomli.load(f))

    @property
    def requires(self) -> List[str]:
        return self.data.get("requires", [])

    @property
    def extra_description(self) -> str:
        return self.data.get("extra_description", "")

    @property
    def obsolete_since(self) -> Optional[str]:
        return self.data.get("obsolete_since")

    @property
    def no_longer_updated(self) -> bool:
        return self.data.get("no_longer_updated", False)


def read_metadata(typeshed_dir: str, distribution: str) -> Metadata:
    """Parse metadata from file."""
    path = os.path.join(typeshed_dir, THIRD_PARTY_NAMESPACE, distribution, META)
    return Metadata.from_file(path)


def determine_version(typeshed_dir: str, distribution: str) -> str:
    version = get_version.read_base_version(typeshed_dir, distribution)
    increment = get_version.main(typeshed_dir, distribution, version)
    if increment >= 0:
        print(f"Existing version found for {distribution}")
    increment += 1
    return f"{version}.{increment}"
