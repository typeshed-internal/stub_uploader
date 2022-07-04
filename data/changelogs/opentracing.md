## 2.4.10 (2022-07-04)

Third-party stubs: audit more `Callable[<parameters>, Any]` annotations (#8233)

## 2.4.9 (2022-05-21)

Simplify and correct many numeric unions (#7906)

Unblocks PyCQA/flake8-pyi#222

## 2.4.8 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.4.7 (2022-01-10)

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

## 2.4.6 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 2.4.4 (2021-12-10)

Add missing context proptery to MockSpan (#6549)

The property context should return a mocked context and not a regular one

## 2.4.3 (2021-12-08)

Adjust opentracing return types for mocks (#6527)

## 2.4.2 (2021-12-03)

Fix minor issues in opentracing (#6482)

## 2.4.1 (2021-12-03)

Annotate remaining opentracing fields, arguments, and return types (#6476)

## 2.4.0 (2021-12-02)

Add opentracing stubs (#6473)

