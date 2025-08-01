## 3.5.0.20250801 (2025-08-01)

Split `tool.stubtest.platforms` metadata key (#13746)

Co-authored-by: Avasam <samuel.06@hotmail.com>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 3.5.0.20250708 (2025-07-08)

[paramiko] Add missing stubs (#14363)

## 3.5.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 3.5.0.20240928 (2024-09-28)

paramiko: add `ProxyCommand` to `_SocketLike` (#12697)

## 3.5.0.20240918 (2024-09-18)

Bump paramiko to 3.5.* (#12672)

## 3.4.0.20240423 (2024-04-23)

paramiko: Replace str with FileDescriptorOrPath in many locations (#11800)

## 3.4.0.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 3.4.0.20240205 (2024-02-05)

A new shade of Black (#11362)

## 3.4.0.20240120 (2024-01-20)

Re-export ChannelFile from paramiko (#11290)

## 3.4.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 3.4.0.20240103 (2024-01-03)

Update type hints for paramiko 3.4 (#11218)

## 3.3.0.2 (2023-11-25)

Added paramiko3.2 PKey and PublicBlob methods (#11067)

Addded missing paramiko methods from https://docs.paramiko.org/en/latest/api/keys.html#paramiko.pkey.PKey

## 3.3.0.1 (2023-11-24)

Third-party stubs: remove unused `type: ignore`s (#11063)

## 3.3.0.0 (2023-07-31)

Bump paramiko to 3.3.* (#10522)

## 3.2.0.1 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 3.2.0.0 (2023-06-01)

Bump `paramiko` to 3.2.* (#10237)

## 3.0.0.10 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 3.0.0.9 (2023-05-03)

paramiko: Improve various bytes-related types (#10109)

## 3.0.0.8 (2023-04-25)

`paramiko`: Be more lenient for client parameter types (#10083)

Use Mapping instead of dict for better covariance

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 3.0.0.7 (2023-04-04)

`google-cloud-ndb`, `paramiko`, `setuptools`: remove unnecessary `= ...`s (#10011)

## 3.0.0.6 (2023-03-29)

Remove unnecessary ellipsis expressions (#9976)

Ignore flake8 F821 warnings in stub files

## 3.0.0.5 (2023-03-27)

Add default values for third-party stubs beginning with 'P' (#9957)

## 3.0.0.4 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 3.0.0.3 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 3.0.0.2 (2023-02-07)

Bump mypy to 1.0 (#9684)

## 3.0.0.1 (2023-02-06)

Use `OSError` instead of `IOError` (#9683)

## 3.0.0.0 (2023-02-06)

Update `paramiko` stubs to 3.0.* (#9667)

## 2.12.0.3 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 2.12.0.2 (2023-01-10)

Delete stubs for `cryptography` (#9459)

Typeshed's stubs for `paramiko` and `pyOpenSSL` now depend on the `cryptography` package, which now provides inline types at runtime

## 2.12.0.1 (2022-11-13)

Fix paramiko stubtest on Windows (#9179)

## 2.12.0.0 (2022-11-12)

Bump paramiko to 2.12.* (#9163)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.11.6 (2022-09-11)

Improve `paramiko.win_pageant` stubs (#8671)

## 2.11.5 (2022-09-03)

fix: add missing paramiko.win_openssh (#8672)

## 2.11.4 (2022-08-31)

`paramiko`: Add missing types in `__init__.pyi` and `_version.pyi` (#8651)

## 2.11.3 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 2.11.2 (2022-07-04)

Third-party stubs: audit more `Callable[<parameters>, Any]` annotations (#8233)

## 2.11.1 (2022-06-26)

Third-party stubs: audit `Callable[<parameters>, None]` annotations (#8175)

## 2.11.0 (2022-06-18)

[stubsabot] Bump paramiko to 2.11.* (#8091)

Co-authored-by: hauntsaninja <>

## 2.10.0 (2022-05-02)

Upgrade paramiko (#7766)

## 2.8.21 (2022-04-30)

Fix paramiko `channel.setblocking()` argument (#7758)

Add 0,1 as allowed arguments using `Literal[0,1]`

## 2.8.20 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 2.8.19 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.8.18 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 2.8.17 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 2.8.16 (2022-03-10)

Modernize syntax in various stubs (#7469)

Use `str` and `contextlib.AbstractContextManager` instead of `typing.Text` and `typing.ContextManager`.

## 2.8.15 (2022-03-09)

Remove explicit inheritance from object (#7468)

## 2.8.14 (2022-03-09)

Remove Python 2 support from some third-party distributions (#7466)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.8.13 (2022-02-08)

Improve `sock` typing in Paramiko stub (#7156)

## 2.8.12 (2022-02-03)

Improve classmethods in `paramiko` stubs (#7113)

## 2.8.11 (2022-01-31)

Upgrade black version (#7089)

## 2.8.10 (2022-01-16)

remove "= ..." from top-level values (#6930)

## 2.8.9 (2022-01-10)

Always use `_typeshed.Self`, where applicable (#6880)

* Always use `_typeshed.Self`, where applicable

* Revert changes to `google-cloud-ndb` (ambiguous)

* Remove empty line added by script

* Revert changes to `stubs/python-dateutil/dateutil/relativedelta.pyi`

* Manually add a few more that the script missed

* Improve `filelock` annotation

Source code here: https://github.com/tox-dev/py-filelock/blob/79ec7b2826e33b982fe83b057f359448b9d966ba/src/filelock/_api.py#L207

* Improve `opentracing/scope` annotation

Source code here: https://github.com/opentracing/opentracing-python/blob/3e1d357a348269ef54d67f761302fab93dbfc0f7/opentracing/scope.py#L71

* Improve `redis/client` stub

Source code here: https://github.com/redis/redis-py/blob/15f315a496c3267c8cbcc6d6d9c6005ea4d4a4d5/redis/client.py#L1217

* Improve `redis/lock` annotation

Source code here: https://github.com/redis/redis-py/blob/15f315a496c3267c8cbcc6d6d9c6005ea4d4a4d5/redis/lock.py#L155

* Improve `requests/models` annotation

Source code here: https://github.com/psf/requests/blob/d718e753834b84018014a23d663369ac27d1ab9c/requests/models.py#L653

## 2.8.8 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 2.8.6 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.8.5 (2021-12-17)

Use stubtest 0.920 (#6589)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.8.4 (2021-12-08)

fix: paramiko.HostKeyEntry.hostnames is a list (#6544)

## 2.8.3 (2021-12-04)

paramiko.Channel - mark arguments as also accepting bytes (#6276)

## 2.8.2 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 2.8.1 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 2.8.0 (2021-11-18)

Add `prefetch` argument to paramiko SFTPClient.getfo (#6331)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.7.4 (2021-11-08)

paramiko.ServerInterface: replace str with bytes in some methods (#6254)

## 2.7.3 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.7.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.7.1 (2021-10-05)

Properly export bytes from paramiko.py3compat (#6113)

## 2.7.0 (2021-09-19)

Update third-party package versions (#5996)

