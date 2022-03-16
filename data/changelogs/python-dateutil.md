## 2.8.10 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 2.8.9 (2022-01-31)

Upgrade black version (#7089)

## 2.8.8 (2022-01-20)

Remove nearly all `__str__` and `__repr__` methods from typeshed (#6968)

## 2.8.7 (2022-01-17)

Use `_typeshed.Self` in Python 2, too (#6932)

## 2.8.6 (2022-01-10)

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

## 2.8.4 (2021-12-25)

python-datetutil: WEEKDAYS and MONTHS can have arbitrary length tuples (#6689)

## 2.8.3 (2021-11-23)

Add tz{utc,offset}.fromutc() (#6360)

## 2.8.2 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.8.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

Annotate rruleset.rrule(rrule) argument (#6149)

## 2.8.0 (2021-09-02)

dateutil.parser: Complete the isoparser module (#5983)

