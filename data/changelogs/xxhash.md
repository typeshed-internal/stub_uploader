## 3.0.4 (2022-07-20)

Allowlist useless modules (#8340)

These are the ones I chose not to add from #8321

Fixes most of #8339

## 3.0.3 (2022-07-19)

Add missing third party modules (#8321)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: hauntsaninja <>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 3.0.2 (2022-07-17)

Make xxhash, editdistance into packages (#8320)

This matches the runtime. Also see #8319

## 3.0.1 (2022-06-21)

stubtest: per project --ignore-missing-stub (#8122)

## 3.0.0 (2022-06-08)

Update xxhash (#8034)

Co-authored-by: hauntsaninja <>

## 2.0.5 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 2.0.4 (2022-04-27)

Drop Python 2 support in third-party stubs (#7703)

## 2.0.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.0.1 (2021-09-14)

Update the `xxhash` and `hashlib` stubs (#6031)

* `name`, `block_size`, `digest_size` and `digestsize` attributes of hash objects were made read-only.
* It is now a type-checking error to subclass `xxhash` classes, such as `xxhash.xxh32`. Previously it was an error only at runtime.
* `xxhash` functions now accept strings as input and any object with `__index__()` method for `seed` (instead of requiring an integer). They also fail the type checking if no arguments are given.

