## 2.9.13.7 (2023-01-28)

Bump flake8-pyi to 23.1.1 (#9599)

## 2.9.13.6 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 2.9.13.5 (2023-01-14)

Resolve stubtest allowlist entries for `ldap3` (#9532)

## 2.9.13.4 (2023-01-12)

Overhaul `ldap3` stubs (#9470)

Add a dependency on `types-pyasn1`, removing the need to subclass `Any`. Fill in many missing types. Use `Incomplete` rather than `Any` where applicable.

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.9.13.3 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 2.9.13.2 (2022-11-13)

Make the `ldap3` stubs platform-agnostic (#9180)

## 2.9.13.1 (2022-11-09)

Annotate known magic-method return types (#9131)

## 2.9.13 (2022-08-17)

Add SAFE_RESTARTABLE strategy to ldap3 Connection client_strategy parameter (#8547)

## 2.9.12 (2022-07-07)

Fix various `TypeAlias` issues (#8248)

## 2.9.11 (2022-06-20)

Overhaul `socket` stubs on Windows and MacOS (#8106)

Reduce the `socket` allowlists for these platforms to a handful of missing constants

## 2.9.10 (2022-06-06)

Always use `TypeAlias` when assigning to `Any` (#8021)

## 2.9.9 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 2.9.8 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 2.9.7 (2022-03-06)

Upgrade to stubtest with dunder pos only reverted (#7442)

## 2.9.6 (2022-02-02)

Add iterable and ServerPool types to ldap3 Connection.server parameter  (#7101)

## 2.9.5 (2022-01-31)

Upgrade black version (#7089)

## 2.9.4 (2022-01-10)

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

## 2.9.3 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 2.9.1 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.9.0 (2021-12-10)

Add stubs for ldap3 (#6561)

