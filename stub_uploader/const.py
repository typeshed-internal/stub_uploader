import pathlib

THIRD_PARTY_NAMESPACE = "stubs"
TESTS_NAMESPACE = "@tests"
META = "METADATA.toml"
TYPES_PREFIX = "types-"

_ROOT = pathlib.Path(__file__).parent.parent
CHANGELOG_PATH = (_ROOT / "data" / "changelogs").resolve()
UPLOADED_PATH = str((_ROOT / "data" / "uploaded_packages.txt").resolve())

REQUIREMENTS = "requirements-tests.txt"
PYPROJECT = "pyproject.toml"

TYPE_CHECKERS = [
    ("mypy", "https://www.mypy-lang.org/"),
    ("pyrefly", "https://pyrefly.org/"),
    ("pyright", "https://microsoft.github.io/pyright/"),
    ("ty", "https://docs.astral.sh/ty/"),
]

# The following non-typeshed packages are allowed to appear in the
# `dependencies` or `optional-dependencies` dependencies field of a package.
#
# Be conservative on what to add here. typeshed packages are generally
# trusted by users and should not depend on packages with a low trust
# level. Presence in the top 1000 PyPI packages could be a necessary but not
# sufficient criterion for inclusion in this allowlist.
#
# Note we could loosen our criteria once we address:
# https://github.com/typeshed-internal/stub_uploader/pull/61#discussion_r979327370
EXTERNAL_REQ_ALLOWLIST = {
    "Flask",
    "Flask-SQLAlchemy",
    "MarkupSafe",
    "Pillow",
    "Werkzeug",
    "affine",
    "arrow",
    "asgiref",
    "beautifulsoup4",
    "click",
    "cryptography",
    "django-stubs",
    "djangorestframework-stubs",
    "httpx",
    "matplotlib",
    "numpy",
    "pandas-stubs",
    "pygobject-stubs",
    "pynacl",
    "pyproj",
    "pytest",
    "referencing",
    "requests",
    "setuptools",
    "torch",
    "tree-sitter",
    "urllib3",
    "websockets",
    "wsproto",
}

# Map of external stub packages to their runtime equivalent.
# We check that the stubs actually depend on their runtime package.
EXTERNAL_RUNTIME_REQ_MAP = {
    "django-stubs": "django",
    "djangorestframework-stubs": "djangorestframework",
    "pandas-stubs": "pandas",
    "pygobject-stubs": "pygobject",
}
