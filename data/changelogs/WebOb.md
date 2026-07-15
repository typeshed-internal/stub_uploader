## 1.8.0.20260712 (2026-07-12)

Avoid class-scope name collisions in stubs ([#15994](https://github.com/python/typeshed/pull/15994))

Class members such as list, type, cursor, Model, and datetime shadow the builtins, classes, or modules referenced by nearby annotations. ty then resolves those annotations to Unknown, which can hide invalid calls in APIs including docker, sqlite3, psycopg2, Markdown, and requests.

Qualify shadowed builtins and use private aliases for colliding imports and classes. This removes 15 stdlib and 120 third-party collision diagnostics under ty 0.0.58, restores the affected public types, and fixes four existing psycopg2 type assertions.

## 1.8.0.20260518 (2026-05-18)

Upgrade black to 26.5.0 ([#15801](https://github.com/python/typeshed/pull/15801))

## 1.8.0.20260509 (2026-05-09)

Reenable ruff rules UP035, UP036, remove RUF100 ([#15715](https://github.com/python/typeshed/pull/15715))

## 1.8.0.20260508 (2026-05-08)

Import some items from typing instead of typing_extensions ([#15711](https://github.com/python/typeshed/pull/15711))

Part of #13782

## 1.8.0.20260408 (2026-04-08)

Use dashes instead of underscores for METADATA.toml field names ([#15614](https://github.com/python/typeshed/pull/15614))

## 1.8.0.20260402 (2026-04-02)

Update most test/lint dependencies ([#15582](https://github.com/python/typeshed/pull/15582))

Update mypy to 1.20.0 ([#15588](https://github.com/python/typeshed/pull/15588))

## 1.8.0.20260322 (2026-03-22)

Add `@type_check_only` to stub-only private classes in various third-party stubs ([#15535](https://github.com/python/typeshed/pull/15535))

## 1.8.0.20260223 (2026-02-23)

Add missing __slots__ to third-party packages ([#15454](https://github.com/python/typeshed/pull/15454))

## 1.8.0.20250822 (2025-08-22)

Add __slots__ to third-party packages using stubdefaulter ([#14619](https://github.com/python/typeshed/pull/14619))

Add missing defaults to third-party stubs ([#14617](https://github.com/python/typeshed/pull/14617))

## 1.8.0.20250820 (2025-08-20)

Loosen `Mapping.update()` overloads a little ([#14593](https://github.com/python/typeshed/pull/14593))

## 1.8.0.20250809 (2025-08-09)

Mark stub-only private symbols as `@type_check_only` in third-party stubs ([#14545](https://github.com/python/typeshed/pull/14545))

## 1.8.0.20250703 (2025-07-03)

Make Mapping.get(default) more constrained ([#14360](https://github.com/python/typeshed/pull/14360))

## 1.8.0.20250522 (2025-05-22)

[webob-stubs] Fix _Serializer protocol  ([#14116](https://github.com/python/typeshed/pull/14116))

## 1.8.0.20250319 (2025-03-19)

[WebOb] Add cgi_FieldStorage.make_file on Python 3.13+ ([#13654](https://github.com/python/typeshed/pull/13654))

## 1.8.0.20250226 (2025-02-26)

WebOb: Fix various issues and refactor some things ([#13487](https://github.com/python/typeshed/pull/13487))

## 1.8.0.20241221 (2024-12-21)

Update to mypy 1.14 ([#13272](https://github.com/python/typeshed/pull/13272))

## 1.8.0.20241205 (2024-12-05)

WebOb: Fixes `webob.exc.status_map` ([#13195](https://github.com/python/typeshed/pull/13195))

## 1.8.0.20240822 (2024-08-22)

Using precise code for `pyright: ignore` and re-enabling various pyright tests ([#12576](https://github.com/python/typeshed/pull/12576))

## 1.8.0.20240520 (2024-05-20)

Add 3.13 to our CI ([#11926](https://github.com/python/typeshed/pull/11926))

## 1.8.0.20240425 (2024-04-25)

Bump pyright to v1.1.360 ([#11810](https://github.com/python/typeshed/pull/11810))

## 1.8.0.20240311 (2024-03-11)

Replace Flake8 checks with Ruff (except for flake8-pyi) ([#11496](https://github.com/python/typeshed/pull/11496))

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

Use PEP 570 syntax in third party stubs ([#11554](https://github.com/python/typeshed/pull/11554))

## 1.8.0.20240301 (2024-03-01)

WebOb: Complete the stubs and activate stricter pyright config ([#11460](https://github.com/python/typeshed/pull/11460))

Fix invalid noqa comments and poorly formatted type ignores ([#11497](https://github.com/python/typeshed/pull/11497))

## 1.8.0.20240128 (2024-01-28)

WebOb: CacheControl descriptors are always allowed to accept `None` ([#11288](https://github.com/python/typeshed/pull/11288))

## 1.8.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs ([#11245](https://github.com/python/typeshed/pull/11245))

## 1.8.0.5 (2023-11-24)

Fix typos in docs and comments ([#11064](https://github.com/python/typeshed/pull/11064))

Third-party stubs: remove unused `type: ignore`s ([#11063](https://github.com/python/typeshed/pull/11063))

## 1.8.0.4 (2023-11-11)

third-party: make some protocol params pos-only ([#11006](https://github.com/python/typeshed/pull/11006))

## 1.8.0.3 (2023-10-27)

Finish stubs for `webob.cookies` and improve `samesite` type ([#10927](https://github.com/python/typeshed/pull/10927))

## 1.8.0.2 (2023-08-13)

Fill in all missing `upstream_repository` fields ([#10571](https://github.com/python/typeshed/pull/10571))

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 1.8.0.1 (2023-06-27)

Fixes incorrect return value for `MultiDict.get` without `default` param ([#10367](https://github.com/python/typeshed/pull/10367))

## 1.8.0.0 (2023-06-18)

Add stubs for WebOb ([#9874](https://github.com/python/typeshed/pull/9874))

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

