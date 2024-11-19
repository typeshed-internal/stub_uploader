import pathlib

THIRD_PARTY_NAMESPACE = "stubs"
TESTS_NAMESPACE = "@tests"
META = "METADATA.toml"
TYPES_PREFIX = "types-"

_ROOT = pathlib.Path(__file__).parent.parent
CHANGELOG_PATH = (_ROOT / "data" / "changelogs").resolve()
UPLOADED_PATH = str((_ROOT / "data" / "uploaded_packages.txt").resolve())
