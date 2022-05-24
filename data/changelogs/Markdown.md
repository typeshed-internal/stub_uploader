## 3.3.22 (2022-05-24)

markdown: Annotate methods of `Registry` (#7926)

Co-authored-by: Shantanu <12621235+hauntsaninja@users.noreply.github.com>

## 3.3.21 (2022-05-19)

markdown: Annotate `parseBoolValue()` (#7875)

## 3.3.20 (2022-05-18)

markdown: Annotate `code_escape()`. (#7857)

## 3.3.19 (2022-05-17)

Markdown: use I/O protocols (#7851)

## 3.3.18 (2022-05-17)

markdown: Annotate `Registry.get_index_for_name()` (#7848)

## 3.3.17 (2022-05-16)

markdown: `isBlockLevel()` returns a bool value. (#7839)

## 3.3.16 (2022-05-13)

markdown: `@deprecated` argument of `message` is a str. (#7835)

## 3.3.15 (2022-05-12)

markdown: PY37 is a bool (#7831)

## 3.3.14 (2022-04-27)

Add various missing generic arguments (#7702)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 3.3.13 (2022-04-16)

Python 3 stubs: use `str` instead of `typing.Text` (#7638)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 3.3.12 (2022-01-10)

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

## 3.3.10 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 3.3.9 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 3.3.8 (2021-11-16)

Add hilite(shebang) argument and return type (#6316)

## 3.3.7 (2021-11-09)

Add markdown.blockprocessors.ReferenceProcessor (#6270)

## 3.3.6 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 3.3.5 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 3.3.4 (2021-10-05)

markdown: fix type of Pattern (#6115)

Surfaced weirdly by #6109

Co-authored-by: hauntsaninja <>

## 3.3.3 (2021-09-20)

Add types to Markdown (#6045)

Most methods and attributes were previously untyped or `Any`-typed.

Co-authored-by: PythonCoderAS <13932583+PythonCoderAS@users.noreply.github.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

