import os
from typing import Any, Dict, List, Optional

import tomli

from .const import META, THIRD_PARTY_NAMESPACE, TYPES_PREFIX


class Metadata:
    def __init__(self, distribution: str, data: Dict[str, Any]):
        self.upstream_distribution = distribution
        self.data = data

    @property
    def stub_distribution(self) -> str:
        return TYPES_PREFIX + self.upstream_distribution

    @property
    def version_spec(self) -> str:
        # The "version" field in METADATA.toml isn't actually a version, it's more
        # like a specifier, e.g. we allow it to contain wildcards.
        version = self.data["version"]
        assert isinstance(version, str)
        return version

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
    with open(path, "rb") as f:
        data = tomli.load(f)
    return Metadata(distribution=distribution, data=data)
