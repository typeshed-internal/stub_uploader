## 2.5.9 (2022-08-22)

`Flask-SQLAlchemy`: `session` should be `scoped_session`, not `Session` (#8589)

## 2.5.8 (2022-08-20)

`Flask-SQLAlchemy`: type `session` as `Session` (#8550)

## 2.5.7 (2022-08-12)

Annotate Model in SQLAlchemy (#8535)

## 2.5.6 (2022-08-10)

`Flask-SQLAlchemy`: Make model query non-generic (#8455)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.5.5 (2022-07-31)

Add type hints to `flask_sqlalchemy.model` (#8389)

## 2.5.4 (2022-07-31)

Annotate flask_sqlalchemy.__init__.Pagination (#8390)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.5.3 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 2.5.2 (2022-05-19)

Import SQLAlchemy types in Flask-SQLAlchemy (#7861)

## 2.5.1 (2022-01-22)

Add __getattr__ to flask-sqlalchemy (#6993)

The SQLAlchemy class exposes dynamically classes of SQLAlchemy. The exact classes depend on used SQLAlchemy version.

## 2.5.0 (2022-01-20)

Add stubs for Flask-SQLAlchemy (#6946)

