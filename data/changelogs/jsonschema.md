## 4.17.0.1 (2022-11-09)

Annotate known magic-method return types (#9131)

## 4.17.0.0 (2022-11-02)

Bump jsonschema to 4.17.* (#9066)

## 4.16.1.1 (2022-10-14)

Fix RefResolver's context manager return types (#8898)

## 4.16.1 (2022-09-27)

Bump mypy to 0.981 (#8796)

## 4.16.0 (2022-09-16)

[stubsabot] Bump jsonschema to 4.16.* (#8748)

Release: https://pypi.org/project/jsonschema/4.16.0/
Homepage: https://github.com/python-jsonschema/jsonschema
Changelog: https://github.com/python-jsonschema/jsonschema/blob/main/CHANGELOG.rst
Diff: https://github.com/python-jsonschema/jsonschema/compare/v4.15.0...v4.16.0

## 4.15.1 (2022-09-03)

`jsonschema._format`: update some annotations to match upstream (#8673)

## 4.15.0 (2022-09-02)

[stubsabot] Bump jsonschema to 4.15.* (#8665)

Co-authored-by: stubsabot <>

## 4.14.0 (2022-08-26)

[stubsabot] Bump jsonschema to 4.14.* (#8619)

## 4.12.1 (2022-08-25)

Improve annotation of jsonschema.validators.create (#8608)

## 4.12.0 (2022-08-19)

[stubsabot] Bump jsonschema to 4.12.* (#8560)

Co-authored-by: stubsabot <>

## 4.9.0 (2022-08-05)

[stubsabot] Bump jsonschema to 4.9.* (#8491)

* [stubsabot] Bump jsonschema to 4.9.*

* Remove jsonschema._reflect

Co-authored-by: stubsabot <>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

## 4.7.0 (2022-07-15)

[stubsabot] Bump jsonschema to 4.7.* (#8299)

## 4.6.0 (2022-06-26)

Bump jsonschema to 4.6.* (#8161)

Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 4.4.9 (2022-06-07)

`jsonschema`: mark type alias explicitly (#8024)

## 4.4.8 (2022-05-30)

Fix exception types for jsonschema._format (#7990)

The annotated type for the `raises` argument on format checkers was

    Exception | tuple[Exception, ...]

when it should read

    type[Exception] | tuple[type[Exception], ...]

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

## 4.4.7 (2022-05-30)

Fix jsonschema exception str|int containers (#7981)

schema_path, relative_schema_path, and absolute_schema_path are all
(related) attributes of `jsonschema` errors which contain `str | int`
but were accidentally annotated as containing `str`. Fix them for
accuracy.

## 4.4.6 (2022-05-29)

jsonschema: {relative,absolute}_path can hold ints (#7980)

## 4.4.5 (2022-05-27)

Flesh out more of jsonschema stubs (#7950)

Apply more detailed annotations to the format module and most of the
exceptions module.

## 4.4.4 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 4.4.3 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 4.4.2 (2022-03-14)

jsonschema: mark schemas as Mapping[str, Any] (#7489)

jsonschema: `RefResolver.referrer` is a `dict[str, Any]` (#7487)

## 4.4.1 (2022-01-25)

Treat validators as classes (#7035)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 4.4.0 (2022-01-24)

Annotate parts of jsonschema.validators and URIDict (#7025)

## 4.3.2 (2022-01-16)

Cleanup: do not quote types unnecessarily (#6931)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 4.3.0 (2021-12-17)

Add `jsonschema.protocols` to library stubs (#6614)

`jsonschema.protocols.Validator` was introduced in `jsonschema` v4.3.0
It's also available under the name `jsonschema.Validator`.

## 4.2.0 (2021-12-06)

Updated stubs to jsonschema 4.2 (#6486)

## 3.2.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

