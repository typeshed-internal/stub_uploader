## 4.26.0.20260109 (2026-01-09)

[stubsabot] Bump jsonschema to ~=4.26.0 ([#15231](https://github.com/python/typeshed/pull/15231))

Release: https://pypi.org/pypi/jsonschema/4.26.0
Homepage: https://github.com/python-jsonschema/jsonschema
Repository: https://github.com/python-jsonschema/jsonschema
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/jsonschema
Changelog: https://github.com/python-jsonschema/jsonschema/blob/main/CHANGELOG.rst
Diff: https://github.com/python-jsonschema/jsonschema/compare/v4.25.1...v4.26.0

Stubsabot analysis of the diff between the two releases:
 - 1 public Python file has been added: `jsonschema/benchmarks/import_benchmark.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 4 files included in typeshed's stubs have been modified or renamed: `jsonschema/_format.py`, `jsonschema/_types.py`, `jsonschema/_typing.py`, `jsonschema/validators.py`.
 - Total lines of Python code added: 48.
 - Total lines of Python code deleted: 26.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 4.25.1.20251009 (2025-10-09)

[jsonschema] _Error.context cannot be None ([#14853](https://github.com/python/typeshed/pull/14853))

## 4.25.1.20251008 (2025-10-08)

Stubtest: Ignore attrs-generated props ([#14845](https://github.com/python/typeshed/pull/14845))

## 4.25.1.20250822 (2025-08-22)

Add __slots__ to third-party packages using stubdefaulter ([#14619](https://github.com/python/typeshed/pull/14619))

## 4.25.1.20250821 (2025-08-21)

Update jsonschema stubs to track latest changes ([#14591](https://github.com/python/typeshed/pull/14591))

## 4.25.0.20250809 (2025-08-09)

Mark stub-only private symbols as `@type_check_only` in third-party stubs (#14545)

## 4.25.0.20250720 (2025-07-20)

[stubsabot] Bump jsonschema to 4.25.* (#14430)

## 4.24.0.20250708 (2025-07-08)

[jsonschema] Add missing stubs (#14264)

Update `jsonschema.protocols.Validator.__init__` (#14327)

## 4.24.0.20250528 (2025-05-28)

Bump jsonschema to 4.24.* (#14166)

## 4.23.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 4.23.0.20241208 (2024-12-08)

Unpin webcolors in jsonschema (#13215)

## 4.23.0.20240813 (2024-08-13)

Use Generator instead of Iterator for 3rd-party context managers (#12481)

## 4.23.0.20240712 (2024-07-12)

[jsonschema] Update to 4.23.* (#12301)

## 4.22.0.20240610 (2024-06-10)

Ensure stubtest gets an older version of `webcolors` when testing `jsonschema` in CI (#12115)

## 4.22.0.20240501 (2024-05-01)

[stubsabot] Bump jsonschema to 4.22.* (#11850)

Release: https://pypi.org/pypi/jsonschema/4.22.0
Homepage: https://github.com/python-jsonschema/jsonschema
Repository: https://github.com/python-jsonschema/jsonschema
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/jsonschema
Changelog: https://github.com/python-jsonschema/jsonschema/blob/main/CHANGELOG.rst
Diff: https://github.com/python-jsonschema/jsonschema/compare/v4.21.1...v4.22.0

Stubsabot analysis of the diff between the two releases:
 - 3 public Python files have been added: `jsonschema/benchmarks/const_vs_enum.py`, `jsonschema/benchmarks/useless_applicator_schemas.py`, `jsonschema/benchmarks/useless_keywords.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 6 files included in typeshed's stubs have been modified or renamed: `jsonschema/_format.py`, `jsonschema/_types.py`, `jsonschema/_utils.py`, `jsonschema/exceptions.py`, `jsonschema/protocols.py`, `jsonschema/validators.py`.
 - Total lines of Python code added: 313.
 - Total lines of Python code deleted: 21.

## 4.21.0.20240331 (2024-03-31)

Remove bare Incomplete annotations in third-party stubs (#11671)

## 4.21.0.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 4.21.0.20240118 (2024-01-18)

[stubsabot] Bump jsonschema to 4.21.* (#11281)

## 4.20.0.20240105 (2024-01-05)

Drop support for Python 3.7 (#11234)

## 4.20.0.0 (2023-11-18)

[jsonschema] Bump to 4.20.* (#11036)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 4.19.0.4 (2023-10-31)

jsonschema: move addionalItems (#10955)

https://github.com/python-jsonschema/jsonschema/commit/daa40b3eaf55f72f6154f9a48e557d895617b24a

Fixes #10953

## 4.19.0.3 (2023-09-25)

Declare that `types-jsonschema` requires Python 3.8+ (#10775)

## 4.19.0.0 (2023-09-23)

Bump jsonschema to 4.19.* (#10583)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 4.17.0.10 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 4.17.0.9 (2023-07-13)

[jsonschema] Use `Incomplete` instead of `Any` (#10451)

Replace `Any` with `Incomplete`

## 4.17.0.8 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 4.17.0.7 (2023-03-27)

Add defaults for third-party stubs I-L (#9955)

## 4.17.0.6 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 4.17.0.5 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 4.17.0.4 (2023-02-07)

Enable flake8-pyi's Y037 (#9686)

## 4.17.0.3 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 4.17.0.2 (2022-12-06)

Update jsonschema protocols.pyi (#9295)

These take in an instance, which need not be a JSON object.
They could for example be arrays.
See [this example](https://python-jsonschema.readthedocs.io/en/stable/api/jsonschema/protocols/#jsonschema.protocols.Validator.iter_errors) on the jsonschema docs.

```python
>>> schema = {"maxItems" : 2}
>>> Draft202012Validator(schema).is_valid([2, 3, 4])
False
```

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

