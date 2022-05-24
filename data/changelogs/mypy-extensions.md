## 0.4.18 (2022-05-24)

`mypy_extensions`: fix `TypeVar` usage (#7937)

#7928

## 0.4.17 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 0.4.16 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 0.4.15 (2022-04-27)

Drop Python 2 support in third-party stubs (#7703)

## 0.4.14 (2022-01-31)

Upgrade black version (#7089)

## 0.4.13 (2022-01-25)

Improve trait signature in mypy_extensions.pyi (#7027)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>

## 0.4.12 (2022-01-10)

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

## 0.4.11 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 0.4.9 (2021-12-16)

mypy_extensions: fix NoReturn, remove inaccurate comment (#6595)

## 0.4.8 (2021-10-12)

Add star to all non-0.1 versions (#6146)

