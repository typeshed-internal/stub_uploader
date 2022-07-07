## 3.0.9 (2022-07-07)

Fix various `TypeAlias` issues (#8248)

## 3.0.8 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 3.0.7 (2022-05-06)

`flask-cors.decorator`: allow `re.Pattern` objects to `origins` and `allow_headers` parameters (#7782)

## 3.0.6 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 3.0.5 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 3.0.4 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 3.0.3 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 3.0.2 (2022-02-20)

flask-cors: remove unused allowlist (#7309)

Co-authored-by: hauntsaninja <>

## 3.0.1 (2022-01-22)

Use class-based syntax for `TypedDict` in `Flask-Cors/flask_cors/core.pyi` (#6995)

Refs https://github.com/PyCQA/flake8-pyi/pull/133

Add missing default values to flask-cors cross_origin (#6994)

## 3.0.0 (2022-01-22)

Add stubs for flask-cors (#6939)

