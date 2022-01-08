## 3.2.3 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 3.2.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 3.2.0 (2021-09-30)

Unbreak CI (#6093)

* Temporarily remove `cachetools` stubs. They will be added back soon, and meanwhile they will continue to be available on pypi.

* Remove `filelock.logger()` (no longer exists in filelock 3.2)

* Delete `OpenSSL.crypto` from stubtest whitelist

Co-authored-by: Akuli <akuviljanen17@gmail.com>

