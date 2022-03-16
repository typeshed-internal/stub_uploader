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

