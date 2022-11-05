## 22.1.0.2 (2022-11-05)

isort: Add more to extra_standard_library (#9098)

## 22.1.0.1 (2022-10-15)

Use `Incomplete` instead of `Any` in `__getattr__` (#8903)

## 22.1.0.0 (2022-10-04)

Update pyOpenSSL stubs to 22.1.* (#8838)

## 22.0.10 (2022-07-29)

Add `pyopenssl.rand` module (#8435)

## 22.0.9 (2022-07-25)

Add `pyopenssl.version` module (#8384)

## 22.0.8 (2022-07-24)

Add missing methods to `OpenSSL.SSL.Connection` (#8374)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 22.0.7 (2022-07-23)

`pyopenssl`: `data` argument for `set_ocsp_server_callback`/`set_ocsp_client_callback` can be non-`bytes` (#8371)

## 22.0.6 (2022-07-22)

Add `ocsp` callback setters to `OpenSSL.SSL` (#8367)

## 22.0.5 (2022-07-22)

Add `proto_version` setters to `OpenSSL.SSL` (#8363)

## 22.0.4 (2022-06-26)

Third-party stubs: audit `Callable[<parameters>, None]` annotations (#8175)

## 22.0.3 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 22.0.2 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

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

