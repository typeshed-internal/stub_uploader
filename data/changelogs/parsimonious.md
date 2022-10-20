## 0.10.0.1 (2022-10-20)

Mark `parsimonious` as completed (#8934)

## 0.10.0 (2022-09-13)

Update parsimonious to 0.10.0 (#8730)

## 0.9.1 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 0.9.0 (2022-06-21)

Bump parsimonious to 0.9.* (#8117)

## 0.8.5 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 0.8.4 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 0.8.3 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 0.8.2 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 0.8.1 (2022-03-13)

parsimonious: `re.Match` does not exist in Python 3.6 (#7482)

It has to be imported from `typing` in <3.7.
Refs https://github.com/python/typeshed/pull/7478.

## 0.8.0 (2022-03-13)

Stubs for parsimonious (#7477)

