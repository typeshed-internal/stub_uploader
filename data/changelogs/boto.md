## 2.49.18.1 (2022-10-15)

Use `Incomplete` instead of `Any` in `__getattr__` (#8903)

## 2.49.18 (2022-09-26)

boto: drop dependency on types-six (#8792)

## 2.49.17 (2022-07-19)

Third-party stubs: enforce CamelCase for type alias names (#8256)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.49.16 (2022-06-28)

Improve `boto` callbacks (#8201)

## 2.49.15 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 2.49.14 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 2.49.13 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.49.12 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 2.49.11 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 2.49.10 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.49.9 (2022-03-10)

Modernize syntax in various stubs (#7469)

Use `str` and `contextlib.AbstractContextManager` instead of `typing.Text` and `typing.ContextManager`.

## 2.49.8 (2022-03-09)

Remove Python 2 support from some third-party distributions (#7466)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.49.7 (2022-01-30)

Reduce use of `Any` in equality methods (#7081)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.49.6 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 2.49.5 (2022-01-07)

Update pyright (#6840)

## 2.49.3 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.49.2 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.49.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.49.0 (2021-09-19)

Update third-party package versions (#5996)

