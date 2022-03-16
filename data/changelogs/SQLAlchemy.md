## 1.4.21 (2022-03-16)

Use pyright 1.1.230 in CI, temporarily pin pyright-action to 1.0.4 (#7495)

* Upgrade pyright to 1.1.230
* Add `type: ignore`s for new pyright checks regarding multiple inheritance
* Temporarily pin pyright-action to 1.0.4, as changes made in 1.0.5 break typeshed's CI

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.4.20 (2022-03-14)

sqlalchemy: Annotate `(Async)Session.__(a)enter__` (#7488)

## 1.4.19 (2022-03-09)

Re-enable stubtest on SQLAlchemy (#7456)

## 1.4.18 (2022-02-22)

Re-introduce the 'stubtest' key for third-party packages (#7351)

Some distributions can't be tested with stubtest for a variety of
reasons or because of bugs in stubtest. This key:

* let's us keep metadata about a distribution in one place,
* prevents us from modifying the scripts because of issues with a
  specific distribution, and
* will trigger tests if only the key is changed.

## 1.4.17 (2022-02-17)

Annotate Session.execute() and Result (#7252)

* Annotate return type of Session.execute()

* Annotate Result return types

* Remove sub-class overrides with identical signatures

## 1.4.16 (2022-02-17)

Various SQLalchemy type improvements (#7238)

* Make ColumnOperators and ColumnElement generic
* Overload Session.query() return type
* Annotate ColumnOperators methods

## 1.4.15 (2022-02-16)

Various SQLalchemy fixes and improvements (#7237)

## 1.4.14 (2022-01-31)

Upgrade black version (#7089)

## 1.4.13 (2022-01-22)

Update SQLAlchemy stubs for 1.4.31 (#6990)

## 1.4.12 (2022-01-20)

Update SQLAlchemy stubs for 1.4.30 (#6973)

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

