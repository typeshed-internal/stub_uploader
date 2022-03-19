## 0.8.2 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 0.8.1 (2022-03-13)

parsimonious: `re.Match` does not exist in Python 3.6 (#7482)

It has to be imported from `typing` in <3.7.
Refs https://github.com/python/typeshed/pull/7478.

## 0.8.0 (2022-03-13)

Stubs for parsimonious (#7477)

