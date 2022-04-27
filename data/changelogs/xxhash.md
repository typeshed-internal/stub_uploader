## 2.0.4 (2022-04-27)

Drop Python 2 support in third-party stubs (#7703)

## 2.0.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.0.1 (2021-09-14)

Update the `xxhash` and `hashlib` stubs (#6031)

* `name`, `block_size`, `digest_size` and `digestsize` attributes of hash objects were made read-only.
* It is now a type-checking error to subclass `xxhash` classes, such as `xxhash.xxh32`. Previously it was an error only at runtime.
* `xxhash` functions now accept strings as input and any object with `__index__()` method for `seed` (instead of requiring an integer). They also fail the type checking if no arguments are given.

