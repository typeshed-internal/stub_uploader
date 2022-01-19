## 1.4.11 (2022-01-19)

Use PEP 585 syntax in `@python2/_ast`, convert more `TypeVar`s to `_typeshed.Self`, & `# noqa` a `SQLAlchemy` line (#6954)

* Manual fixes for `_ast` and `SQLAlchemy`

* Change more `TypeVar`s to `Self`, using script

## 1.4.9 (2022-01-10)

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

## 1.4.8 (2022-01-09)

Further annotate sqlalchemy.engine and collections (#6680)

## 1.4.7 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 1.4.6 (2022-01-07)

Update pyright (#6840)

## 1.4.4 (2021-12-23)

Add execution_options to Session.get() (#6656)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.4.3 (2021-12-23)

Fix third-party issues found by stubtest (#6667)

## 1.4.2 (2021-12-22)

Various small SQLAlchemy type improvements (#6623)

## 1.4.1 (2021-12-21)

SQLAlchemy: Partly annotate declarative API (#6647)

## 1.4.0 (2021-12-17)

Create SQLalchemy stubs using stubgen (#6585)

