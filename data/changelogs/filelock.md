## 3.2.7 (2022-06-09)

filelock: mark as obsolete since 3.3.0 (#8043)

## 3.2.6 (2022-05-21)

Simplify and correct many numeric unions (#7906)

Unblocks PyCQA/flake8-pyi#222

## 3.2.5 (2022-01-20)

Remove nearly all `__str__` and `__repr__` methods from typeshed (#6968)

## 3.2.4 (2022-01-10)

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

