## 9.0.7 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 9.0.6 (2022-02-03)

Improve `__enter__` & constructor methods (#7114)

## 9.0.5 (2022-01-22)

fix incorrect tuple[T] (#6996)

Found from PyCQA/flake8-pyi#135.

## 9.0.4 (2022-01-10)

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

## 9.0.3 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 9.0.2 (2022-01-07)

Pillow: Image fixes (#6848)

* Fix return type of `Image.transform()`.
* Add animation attributes to `Image`.

## 9.0.0 (2022-01-05)

Upgrade stubs to Pillow 9 (#6795)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 8.3.11 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 8.3.10 (2021-12-23)

Remove PIL.__main__ (#6665)

## 8.3.9 (2021-12-21)

correct border= and fill= kwargs for ImageOps.expand (#6641)

## 8.3.8 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 8.3.7 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 8.3.6 (2021-10-11)

Annotate PIL.ImageColor (#6151)

## 8.3.5 (2021-10-11)

Color arguments also take (r,g,b,a) tuples  (#6148)

## 8.3.4 (2021-09-06)

Fix type of stroke_width parameter in Pillow's ImageDraw.*text* functions (#6008)

