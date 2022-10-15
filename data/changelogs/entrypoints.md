## 0.4.1.1 (2022-10-15)

Mark `entrypoints` as complete (#8901)

## 0.4.1 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 0.4.0 (2022-06-25)

[stubsabot] Bump entrypoints to 0.4.* (#8157)

Co-authored-by: hauntsaninja <>

## 0.3.7 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 0.3.6 (2022-04-27)

Remove Python 2 support from entrypoints (#7711)

## 0.3.5 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 0.3.3 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 0.3.2 (2021-10-13)

Cleanup: use lower-case list and dict, add a test (#6161)

## 0.3.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

