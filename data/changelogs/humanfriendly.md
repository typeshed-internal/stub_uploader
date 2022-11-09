## 10.0.1.1 (2022-11-09)

Annotate known magic-method return types (#9131)

## 10.0.1 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 10.0.0 (2022-06-21)

[stubsabot] Bump humanfriendly to 10.0.* (#8118)

Co-authored-by: hauntsaninja <>

## 9.2.8 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 9.2.7 (2022-04-27)

Add various missing generic arguments (#7702)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 9.2.6 (2022-04-01)

Third-party stubs: Improve several `__exit__` methods (#7575)

## 9.2.5 (2022-04-01)

flake8 config: remove line that exists only for Python-2 checking (#7570)

## 9.2.3 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 9.2.2 (2021-10-28)

Annotate humanfriendly.__init__.pyi (#6209)

## 9.2.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

