## 1.4.53.27 (2023-01-29)

[stubsabot] Mark SQLAlchemy as obsolete since 2.0.0 (#9595)

Release: https://pypi.org/pypi/SQLAlchemy/2.0.0
Homepage: https://www.sqlalchemy.org

## 1.4.53.26 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9565)

## 1.4.53.25 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 1.4.53.24 (2023-01-14)

Fix stubtest for sqlalchemy.testing.plugin.pytestplugin (#9533)

## 1.4.53.23 (2023-01-11)

SQLAlchemy: Annotate text() (#9498)

## 1.4.53.22 (2023-01-11)

`SQLAlchemy`: Remove some implementation details (#9492)

Stubs for the mypy plugin, which aren't useful if you're using typeshed's SQLAlchemy stubs, have been removed.

## 1.4.53.21 (2023-01-05)

Update SQLAlchemy stubs to 1.4.46 (#9464)

Replace `Any` with `Incomplete` where applicable

## 1.4.53.20 (2022-12-28)

Check for unused `pyright: ignore` and differentiate from mypy ignores (#9397)

## 1.4.53.19 (2022-12-14)

Update to SQLAlchemy 1.4.45 (#9359)

Use Incomplete in touched files

## 1.4.53.18 (2022-11-28)

sqlalchemy: add return types for known magic methods (#9290)

## 1.4.53.17 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 1.4.53.8 (2022-11-16)

Always use `bool` and `Literal` for Python compat code (#9213)

## 1.4.53.7 (2022-11-13)

[stubsabot] Bump SQLAlchemy to 1.4.44 (#9182)

Release: https://pypi.org/pypi/SQLAlchemy/1.4.44
Homepage: https://www.sqlalchemy.org

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 1.4.53.6 (2022-11-09)

All `__nonzero__` are methods that return `bool` (#9139)

## 1.4.53.5 (2022-11-09)

Annotate known magic-method return types (#9131)

## 1.4.53.4 (2022-11-08)

Fix and allow classes with missing metaclasses (#9136)

## 1.4.53.3 (2022-11-05)

[stubsabot] Bump SQLAlchemy to 1.4.43 (#9092)

Release: https://pypi.org/pypi/SQLAlchemy/1.4.43
Homepage: https://www.sqlalchemy.org

## 1.4.53.2 (2022-10-17)

Fix stubtest failures on `SQLAlchemy` (#8914)

## 1.4.53.1 (2022-10-16)

Remove empty `__init__` methods from classes with 0 parents (#8907)

## 1.4.53 (2022-09-27)

Bump mypy to 0.981 (#8796)

## 1.4.52 (2022-09-22)

Reexport NoResultFound in orm/exc (#8782)

## 1.4.51 (2022-09-10)

`SQLAlchemy`: Use `ParamSpec` for `Engine.transaction()` and `Engine.run_callable()` (#8718)

## 1.4.50 (2022-08-10)

Fix stubtest failures on `SQLAlchemy` (#8524)

## 1.4.49 (2022-07-30)

Remove or move several `TypeAlias` declarations (#8444)

## 1.4.48 (2022-07-28)

Fix TODO RE: Use of `Concatenate` and `ParamSpec` in sqlalchemy (#8415)

## 1.4.47 (2022-07-26)

SQLAlchemy: Fix annotations for Query.{update,delete} (#8388)

Closes: #8387

## 1.4.46 (2022-07-19)

Third-party stubs: enforce CamelCase for type alias names (#8256)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.4.45 (2022-07-12)

Use error codes for type ignores (#8280)

Disable reportSelfClsParameterName for pytype as this is out of typeshed's
control

Closes: #7497

## 1.4.44 (2022-07-11)

Remove Python 3.6 branches from typeshed (#8269)

## 1.4.43 (2022-07-08)

Add Session annotation for sessionmaker call (#8257)

## 1.4.42 (2022-07-07)

Improve `SQLAlchemy` type aliases (#8252)

* Remove `sqlalchemy.dbapi` (in favor of `_typeshed.dbapi`).
* Don't re-export mypy imports from `sqlalchemy.ext.mypy.*`.

## 1.4.41 (2022-06-25)

Fix stubtest failures on `SQLAlchemy` (#8148)

## 1.4.40 (2022-06-22)

Improve several `__hash__` methods (#8128)

## 1.4.39 (2022-06-16)

Upgrade pyright, improve pyright config files (#8072)

Fix `TypeVar`s in `beautifulsoup` and `SQLAlchemy` (#8087)

## 1.4.38 (2022-06-06)

Always use `TypeAlias` when assigning to `Any` (#8021)

## 1.4.37 (2022-06-01)

SQLAlchemy 1.4.37 fixes (#8003)

Closes: #8001

## 1.4.36 (2022-05-27)

constructors: Fix defaulted TypeVars (#7965)

From the list in https://github.com/microsoft/pyright/issues/3501

## 1.4.35 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 1.4.34 (2022-05-10)

Update testing_engine() annotations (#7818)

## 1.4.33 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 1.4.32 (2022-04-27)

Add various missing generic arguments (#7702)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 1.4.31 (2022-04-20)

Add typing for __iter__ in sqlalchemy.orm.Query (#7666)

## 1.4.30 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 1.4.29 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 1.4.28 (2022-04-07)

SQLAlchemy improvements for Operators (#7604)

## 1.4.27 (2022-04-07)

SQLAlchemy improvements for generative methods (#7603)

## 1.4.26 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 1.4.25 (2022-04-01)

Update SQLalchemy to 1.4.34 (#7573)

Closes: #7572

## 1.4.24 (2022-03-29)

Remove unneeded `# noqa` comments, fix broken `# noqa` comments (#7561)

## 1.4.23 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.4.22 (2022-03-16)

pyright: Don't report incompatible overrides (#7498)

These overrides are inherited from the implementation and are out of
typeshed's control.

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

