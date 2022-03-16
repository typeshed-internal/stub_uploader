## 1.0.14 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 1.0.13 (2022-01-28)

Add __enter__/__exit__ to pymysql.Connection (#7069)

## 1.0.11 (2022-01-10)

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

## 1.0.10 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 1.0.8 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 1.0.7 (2021-12-17)

Use stubtest 0.920 (#6589)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 1.0.6 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 1.0.5 (2021-11-09)

Improve pymysql.converters stubs (#6267)

I spent far too much time being confused about why pyanalyze thought `pymysql.converters.escape_dict` only takes two arguments.

I rewrote the stubs from scratch using the implementation: https://github.com/PyMySQL/PyMySQL/blob/main/pymysql/converters.py.

The "charset" argument is ignored as far as I can tell; it gets passed to other functions but no function actually uses it.

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

## 1.0.4 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 1.0.3 (2021-10-12)

Add star to all non-0.1 versions (#6146)

