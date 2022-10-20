## 4.0.15.2 (2022-10-20)

Remove `mock` from `pyright`'s exclude (#8942)

## 4.0.15.1 (2022-10-19)

Mark `mock` as completed (#8919)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 4.0.15 (2022-06-06)

Always use `TypeAlias` when assigning to `Any` (#8021)

## 4.0.14 (2022-05-25)

mock: Fix unconstrained TypeVar (#7945)

The first overload covers the case where `new` is not given.

Part of #7928

## 4.0.13 (2022-04-01)

Third-party stubs: Improve several `__exit__` methods (#7575)

## 4.0.12 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 4.0.11 (2022-02-22)

Correct several positional-only differences in third-party stubs (#7352)

## 4.0.10 (2022-02-03)

Improve `__enter__` & constructor methods (#7114)

## 4.0.9 (2022-01-30)

Reduce use of `Any` in equality methods (#7081)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 4.0.8 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 4.0.7 (2022-01-07)

Update pyright (#6840)

## 4.0.5 (2021-12-25)

Fixes for third-party mock package (#6685)

Removed a few unused private classes and methods. They can be re-added if a user reports them missing.

## 4.0.4 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 4.0.3 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 4.0.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

