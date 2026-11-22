## [0.5.0.20261122](https://pypi.org/project/types-PyMeeus/0.5.0.20261122/) (2026-11-22)

* Replace final `FloatInt` instances ([#16887](https://github.com/python/typeshed/pull/16887))

    - `unittest.mock.ThreadingMixin.DEFAULT_TIMEOUT` was marked as final
    by accident.
    - `jenkins.DEFAULT_TIMEOUT` is a sentinel, not `float`.
    - Reportlab landscape and portrait only accept float arguments if they return only float values.

* Replace float with FloatInt ([#16789](https://github.com/python/typeshed/pull/16789))

## 0.5.0.20260518 (2026-05-18)

Upgrade black to 26.5.0 ([#15801](https://github.com/python/typeshed/pull/15801))

## 0.5.0.20260408 (2026-04-08)

Use dashes instead of underscores for METADATA.toml field names ([#15614](https://github.com/python/typeshed/pull/15614))

## 0.5.0.20250828 (2025-08-28)

[PyMeeus] Add stubs ([#14649](https://github.com/python/typeshed/pull/14649))

