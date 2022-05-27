## 2.8.17 (2022-05-27)

dateutil: Add dateutil.rrule.weekdays (#7968)

Closes: #7946

## 2.8.16 (2022-05-19)

Add return type for `dateutil.rrule._rrulestr.__call__`. (#7868)

## 2.8.15 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 2.8.14 (2022-04-27)

dateutil.tz.tz: Replace IO with protocols (#7717)

## 2.8.13 (2022-04-27)

Drop Python 2 support from python-dateutil (#7715)

## 2.8.12 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 2.8.11 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

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

