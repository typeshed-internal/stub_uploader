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

