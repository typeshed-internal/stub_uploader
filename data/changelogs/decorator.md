## 5.1.8.1 (2022-10-14)

Mark `decorator` as complete (#8897)

## 5.1.8 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 5.1.7 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 5.1.6 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 5.1.5 (2022-04-16)

Python 3 stubs: use `str` instead of `typing.Text` (#7638)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 5.1.4 (2022-01-27)

Add `ParamSpec` to `decorator.contextmanager` (#7051)

There may be other places in this package where `ParamSpec` could be used, but this one is the most clear-cut.

## 5.1.2 (2022-01-02)

Never explicitly inherit from `object` in Python 3-only stubs (#6777)

## 5.1.1 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 5.1.0 (2021-10-12)

Update remaining versions for third-party stubs (#6094)

Also remove the python2 markers of packages that don't list Python 2
as supported in the latest version.

Don't special case version '0.1'

Co-authored-by: Akuli <akuviljanen17@gmail.com>

