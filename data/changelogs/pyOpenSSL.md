## 22.0.1 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 22.0.0 (2022-01-30)

pyOpenSSL: Adapt to changes in 22.0.0 (#7080)

## 21.0.2 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 21.0.1 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 21.0.0 (2021-11-10)

Add pyOpenSSL 21 constants (#6273)

## 20.0.9 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 20.0.8 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 20.0.7 (2021-09-30)

Unbreak CI (#6093)

* Temporarily remove `cachetools` stubs. They will be added back soon, and meanwhile they will continue to be available on pypi.

* Remove `filelock.logger()` (no longer exists in filelock 3.2)

* Delete `OpenSSL.crypto` from stubtest whitelist

Co-authored-by: Akuli <akuviljanen17@gmail.com>

