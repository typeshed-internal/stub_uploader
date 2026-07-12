## 0.5.0.20260712 (2026-07-12)

Avoid class-scope name collisions in stubs ([#15994](https://github.com/python/typeshed/pull/15994))

Class members such as list, type, cursor, Model, and datetime shadow the builtins, classes, or modules referenced by nearby annotations. ty then resolves those annotations to Unknown, which can hide invalid calls in APIs including docker, sqlite3, psycopg2, Markdown, and requests.

Qualify shadowed builtins and use private aliases for colliding imports and classes. This removes 15 stdlib and 120 third-party collision diagnostics under ty 0.0.58, restores the affected public types, and fixes four existing psycopg2 type assertions.

## 0.5.0.20260518 (2026-05-18)

Upgrade black to 26.5.0 ([#15801](https://github.com/python/typeshed/pull/15801))

## 0.5.0.20260508 (2026-05-08)

Import some items from typing instead of typing_extensions ([#15711](https://github.com/python/typeshed/pull/15711))

Part of #13782

## 0.5.0.20260408 (2026-04-08)

Use dashes instead of underscores for METADATA.toml field names ([#15614](https://github.com/python/typeshed/pull/15614))

## 0.5.0.20251108 (2025-11-08)

Initial colorful stubs ([#14939](https://github.com/python/typeshed/pull/14939))

