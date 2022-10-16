## 2.1.4.1 (2022-10-16)

Remove empty `__init__` methods from classes with 0 parents (#8907)

## 2.1.4 (2022-07-19)

Third-party stubs: enforce CamelCase for type alias names (#8256)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.1.3 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 2.1.2 (2022-07-04)

Third-party stubs: audit more `Callable[<parameters>, Any]` annotations (#8233)

## 2.1.1 (2022-06-26)

Third-party stubs: audit `Callable[<parameters>, None]` annotations (#8175)

## 2.1.0 (2022-06-21)

Bump waitress to 2.1.* (#8113)

## 2.0.9 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 2.0.8 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 2.0.7 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.0.5 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.0.4 (2021-12-17)

Use stubtest 0.920 (#6589)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.0.3 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 2.0.2 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 2.0.1 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.0.0 (2021-10-12)

Update remaining versions for third-party stubs (#6094)

Also remove the python2 markers of packages that don't list Python 2
as supported in the latest version.

Don't special case version '0.1'

Co-authored-by: Akuli <akuviljanen17@gmail.com>

