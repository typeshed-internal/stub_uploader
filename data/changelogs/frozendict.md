## 2.0.9 (2022-06-09)

frozendict: mark as obsolete since 2.2.0 (#8044)

It has shipped with a py.typed file since v.2.2.0 in January: https://github.com/Marco-Sulla/python-frozendict/commit/7fcdd3aa990aa323fbcecea4b33733468c97cc27

It can be removed come July 15

Co-authored-by: hauntsaninja <>

## 2.0.8 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.0.7 (2022-03-06)

Upgrade to stubtest with dunder pos only reverted (#7442)

## 2.0.6 (2022-02-22)

Correct several positional-only differences in third-party stubs (#7352)

## 2.0.5 (2022-01-20)

Remove nearly all `__str__` and `__repr__` methods from typeshed (#6968)

## 2.0.4 (2022-01-10)

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

## 2.0.3 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 2.0.1 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.0.0 (2021-10-12)

Update remaining versions for third-party stubs (#6094)

Also remove the python2 markers of packages that don't list Python 2
as supported in the latest version.

Don't special case version '0.1'

Co-authored-by: Akuli <akuviljanen17@gmail.com>

