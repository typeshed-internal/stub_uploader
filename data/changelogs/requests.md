## 2.32.4.20250611 (2025-06-11)

[requests] Update to 2.32.4 (#14254)

## 2.32.0.20250602 (2025-06-02)

Update mypy to 1.16.0 (#14194)

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.32.0.20250515 (2025-05-15)

[requests] Add a _JSON type alias (#14064)

## 2.32.0.20250328 (2025-03-28)

[requests] Remove Session.redirect_cache (#13723)

## 2.32.0.20250306 (2025-03-06)

Update tools versions in `stubtest` workflow (#13582)

## 2.32.0.20250301 (2025-03-01)

Fix conflicting imports (#13561)

## 2.32.0.20241016 (2024-10-16)

remove unneeded Iterable base class from CookieJar (#12812)

## 2.32.0.20240914 (2024-09-14)

Correct requests `cookies` argument (#12654)

## 2.32.0.20240907 (2024-09-07)

requests: Session.adapters is a mapping of Adapters (#12473)

Signed-off-by: Stephen Finucane <stephen@that.guru>

## 2.32.0.20240905 (2024-09-05)

Add hint for requests.models.Response.raw (#12616)

## 2.32.0.20240712 (2024-07-12)

requests: Add connection property (type HTTPAdapter) to the Response class (#12279)

The `Response` instance is built by `HTTPAdapter`. When built, a property called `connection` is added to the `Response` that points back to the `HTTPAdapter` that created it. For example, this is used in the `requests` library's `HTTPDigestAuth` class to remake requests with credentials after authorization is requested by a server.

## 2.32.0.20240622 (2024-06-22)

requests: Fix Response.content return type to include None (#12180)

## 2.32.0.20240602 (2024-06-02)

[requests] Update to 2.32.3 (#12060)

## 2.32.0.20240523 (2024-05-23)

[requests] Update to 2.32.2 (#12000)

Also replace some `Any` annotations with `Incomplete` and use `Final` in `requests.__version__`.

## 2.32.0.20240521 (2024-05-21)

[stubsabot] Bump requests to 2.32.* (#11991)

Release: https://pypi.org/pypi/requests/2.32.1
Homepage: https://requests.readthedocs.io
Repository: https://github.com/psf/requests
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/requests
Diff: https://github.com/psf/requests/compare/v2.31.0...v2.32.1

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 486.
 - Total lines of Python code deleted: 131.

## 2.31.0.20240406 (2024-04-06)

requests: export `packages` and `utils` (#11723)

## 2.31.0.20240403 (2024-04-03)

requests: remove a `type: ignore` (#11704)

## 2.31.0.20240402 (2024-04-02)

requests: annotate RequestsCookieJar (#11656)

## 2.31.0.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 2.31.0.20240310 (2024-03-10)

Bump mypy to 1.9, add to json.encoder, small fixups (#11549)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.31.0.20240218 (2024-02-18)

requests: Allow passing None header values (#11370)

https://github.com/python/typeshed/pull/7773 changed
`requests.session.Session` methods to accept None for header values, but
didn't do quite the same for the functions in `requests.api`.  I think
this was a mistake.  The functions in `requests.api` just pass through
the `headers` argument without doing anything in particular to it.

Furthermore, it's useful to be able to pass None as a header value:
because `requests.utils.default_headers` sets an `Accept-Encoding`
header by default, the easiest way to send a request with no
`Accept-Encoding` header is something like `requests.get(url,
headers={"Accept-Encoding": None})`.  It's annoying to have to construct
a `Session` just to pass type-checking.

It's a little confusing for the type alias to be called
`_HeadersUpdateMapping` in `requests.sessions` but `_HeadersMapping` in
`requests.api`; this is because the latter name was already used in
other type stubs (`tensorflow.keras.callbacks`), so it seemed best to
avoid breaking API.

## 2.31.0.20240125 (2024-01-25)

Add parameter type to PreparedRequest.prepare_content_length (#11304)

## 2.31.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 2.31.0.20231231 (2023-12-31)

requests: Use the `Any` trick in `HTTPError` (#11207)

## 2.31.0.10 (2023-10-18)

requests: annotate `utils.get_encoding_from_headers()` (#10901)

## 2.31.0.9 (2023-10-13)

[requests] Allow HTTPError.response to be None (#10875)

This aligns with the definition in requests, but means that user code might
need additional assertions to ensure that `HTTPError.response` is not `None`.

## 2.31.0.8 (2023-10-05)

`types-requests`, `types-influxdb-client`: add note to the PyPI readme about the `urllib3` pin (#10839)

## 2.31.0.7 (2023-10-01)

Remove stubs for `urllib3` (#10812)

Both types-requests and types-influxdb-client now depend on urllib3>=2 instead of types-urllib3. That in turn means that types-caldav, types-slumber and types-requests-oauthlib all depend indirectly on urllib3>=2, since all three stubs packages depend on types-requests.

## 2.31.0.6 (2023-09-27)

[requests] loosen HTTPError constructor (#10776)

## 2.31.0.5 (2023-09-25)

[requests] Allow PreparedRequest for RequestException(request=...) (#10767)

## 2.31.0.4 (2023-09-23)

[requests] Improve exception class constructors (#10740)

## 2.31.0.3 (2023-09-20)

requests: type RequestException members (not Any) (#8989)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.31.0.2 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 2.31.0.1 (2023-05-29)

Allowlist requests.compat.bytes.__buffer__ (#10231)

## 2.31.0.0 (2023-05-23)

[stubsabot] Bump requests to 2.31.* (#10199)

Release: https://pypi.org/pypi/requests/2.31.0
Homepage: https://requests.readthedocs.io
Diff: https://github.com/psf/requests/compare/v2.30.0...v2.31.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 2 files included in typeshed's stubs have been modified or renamed: `requests/__version__.py`, `requests/sessions.py`.
 - Total lines of Python code added: 26.
 - Total lines of Python code deleted: 4.

## 2.30.0.0 (2023-05-05)

[requests] Update stubs to 2.30 (#10141)

## 2.29.0.0 (2023-04-29)

Update `requests` for v2.29 (#10097)

## 2.28.11.17 (2023-03-28)

Add defaults for third-party stubs Q-T (#9959)

## 2.28.11.16 (2023-03-22)

Add type to requests.models.RequestEncodingMixin.path_url (#9923)

We can see at https://github.com/psf/requests/blob/7f694b79e114c06fac5ec06019cada5a61e5570f/requests/models.py#L104 that this always returns a string.

## 2.28.11.15 (2023-02-26)

Improve many `__(a)exit__` annotations (#9696)

## 2.28.11.14 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 2.28.11.13 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 2.28.11.12 (2023-02-07)

Improve pyright verification of third-party test cases in CI (#9650)

Co-authored-by: Avasam <samuel.06@hotmail.com>

## 2.28.11.11 (2023-02-07)

Enable flake8-pyi's Y037 (#9686)

## 2.28.11.10 (2023-02-07)

Bump mypy to 1.0 (#9684)

## 2.28.11.9 (2023-02-06)

Use `OSError` instead of `IOError` (#9683)

## 2.28.11.8 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 2.28.11.7 (2022-12-22)

`requests`: set `session.headers` to `MutableMapping` (#9395)

## 2.28.11.6 (2022-12-21)

requests: types for auth username and password (#9389)

## 2.28.11.5 (2022-11-16)

Always use `bool` and `Literal` for Python compat code (#9213)

## 2.28.11.4 (2022-11-09)

Annotate known magic-method return types (#9131)

## 2.28.11.3 (2022-11-08)

Fix and allow classes with missing metaclasses (#9136)

## 2.28.11.2 (2022-10-07)

Mark `requests` stubs as complete (#8858)

Co-authored-by: Kevin Kirsche <kevin.kirsche@one.verizon.com>

## 2.28.11.1 (2022-10-04)

`requests`: Add regression test for #8762 (#8835)

The final mypy_primer report for #8762 was an empty diff. Considering the number of issues we've had with our requests stubs over the last year, it feels like it makes sense to add a test case to make sure that it doesn't regress.

## 2.28.11 (2022-09-22)

`requests`: improve `_Data` type (#8762)

requests: improve _Data type

This allows to pass an Iterable[bytes] for streaming request data.

## 2.28.10 (2022-09-08)

Add infrastructure allowing for test cases for third-party stubs (#8700)

- Move the logic for running mypy on the test cases from `tests/mypy_test.py` to a separate script, `tests/regr_test.py`.
- Add the necessary logic in order to be able to have test cases for third-party stubs.
- Move logic common to `tests/mypy_test.py` and `tests/regr_test.py` into `tests/colors.py`, and rename `tests/colors.py` to `tests/utils.py`.
- Add a new check to `tests/check_consistent.py`, to enforce the use of `# pyright: reportUnnecessaryTypeIgnoreComment=true` comments in third-party test cases. These are essential if we want to have our tests against false-negatives work with pyright.
- Update the relevant documentation to account for the new test file.
- Add a new job to the `tests.yml` GitHub workflow, to run the new test in CI.
- Add a simple proof-of-concept test case for `requests`, as a regression test for #7998.

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

## 2.28.9 (2022-08-18)

Support extras in stubtest_third_party.py (#8467)

## 2.28.8 (2022-08-05)

`requests.adapters`: use re-exports rather than assignments (#8485)

Add `requests.help` submodule (#8486)

Add `requests.__version__`; improve `requests.__init__` (#8484)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.28.7 (2022-08-02)

requests: fix stubtest (#8463)

## 2.28.6 (2022-07-30)

Remove or move several `TypeAlias` declarations (#8444)

## 2.28.5 (2022-07-26)

requests: add type hints to requests.utils (#8395)

Co-authored-by: Shantanu <12621235+hauntsaninja@users.noreply.github.com>

## 2.28.4 (2022-07-25)

Add missing re-exports and vars to requests.compat (#8396)

## 2.28.3 (2022-07-21)

requests: add annotation for `parse_header_links` (#8349)

In the requests package the function `utils.parse_header_links()`
takes a str as input and returns a list of dictionaries.

This can be seen in the unit tests that are used:
https://github.com/psf/requests/blob/786255613bd92f87c9c8f066c4271aab1b9eeaad/tests/test_utils.py#L644-L664

## 2.28.2 (2022-07-18)

`requests`: Annotate `Session.merge_environment_settings` (#8313)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.28.1 (2022-07-12)

Turn requests.requests.packages into a module (#8281)

Remove obsolete class VendorAlias

## 2.28.0 (2022-06-25)

[stubsabot] Bump requests to 2.28.* (#8152)

Co-authored-by: hauntsaninja <>

## 2.27.31 (2022-06-21)

`requests`, `regex`: use re-exports instead of assignments in a few places (#8127)

## 2.27.30 (2022-06-01)

requests: expand types for files (#7999)

## 2.27.29 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 2.27.28 (2022-05-26)

requests: allow immutable headers (#7932)

## 2.27.27 (2022-05-19)

Fix requests.Session().hooks (#7871)

Fixes #7776

Mutating hooks, as in `session.hooks['response'] = ...`, should work. Reassigning it like `session.hooks = ...` is probably a bad idea, so it will always be a `dict`.

## 2.27.26 (2022-05-16)

`requests`: Fix type of request headers (#7773)

Allow bytes values. In `Session` methods, `None` can be used to ignore the session's headers.

## 2.27.25 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 2.27.24 (2022-04-28)

requests: allow non-mutable Mapping for files/hooks parameters (#7732)

## 2.27.23 (2022-04-28)

requests: allow str and bytes for fileobj in files parameter (#7728)

* requests: allow str and bytes for fileobj in files parameter

* requests: Use SupportsRead instead of IO for files

## 2.27.22 (2022-04-27)

requests: Add None to a type alias (#7721)

Fixes #7720

## 2.27.21 (2022-04-27)

Add more typing hints for requests (#7696)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.27.20 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 2.27.19 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.27.18 (2022-04-16)

Use imports instead of TypeAliases in a couple places (#7634)

Fixes #7632

## 2.27.17 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

Use str instead of typing.Text (#7629)

## 2.27.16 (2022-04-01)

Third-party stubs: Improve several `__exit__` methods (#7575)

## 2.27.15 (2022-03-27)

requests: Update adapters.pyi (#7544)

The cert can be
* A string / bytes which is a path to a certfile
* A tuple with two string / bytes, where the first is the certfile and the second is a keyfile
* None (optional)

The tuple could be anything indexable, but there are strict requirement to actualle have two items, don't know if there is something more generic

See https://github.com/psf/requests/blob/main/requests/adapters.py#L242-L248

## 2.27.14 (2022-03-19)

PEP 604: Remove some more uses of Union/Optional (#7515)

The following patterns still break mypy:

1. `type[]` at top level fails
2. `tuple[T1, T2]` at top level fails (but `tuple[T1, ...]` is fine)
3. `T1 | Callable[..., T2 | T3]` fails, but only <=3.9

This PR cleans up usage of `Union` and `Optional` outside these patterns.

## 2.27.13 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 2.27.12 (2022-03-13)

`requests` stubs are not Python 2-compatible (#7483)

## 2.27.11 (2022-02-22)

Correct several positional-only differences in third-party stubs (#7352)

## 2.27.10 (2022-02-16)

Remove unused allowlist entries in `babel` and `requests` (#7233)

## 2.27.9 (2022-02-09)

Added missing import for JSONDecodeError (#7171)

Co-authored-by: DataGhost <git@dataghost.com>

## 2.27.8 (2022-01-31)

requests.Session: Accept hooks and lists of hooks (#7094)

## 2.27.7 (2022-01-13)

requests: remove an unused allowlist entry (#6911)

## 2.27.6 (2022-01-12)

requests: Remove an unused allowlist entry (#6897)

## 2.27.5 (2022-01-10)

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

## 2.27.4 (2022-01-10)

Remove unused `requests` allowlist entry (#6882)

## 2.27.3 (2022-01-08)

Use lowercase `type` everywhere (#6853)

Use types-urllib3 for requests (#6859)

## 2.27.2 (2022-01-07)

Update pyright (#6840)

## 2.27.0 (2022-01-07)

requests: Add JSONDecodeError (#6838)

## 2.26.3 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.26.2 (2021-12-17)

Use stubtest 0.920 (#6589)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.26.1 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 2.26.0 (2021-11-10)

Add some kwonly arguments to Session.send() (#6266)

Bump version to 2.26

## 2.25.12 (2021-11-09)

Remove BaseAdapter from requests.sessions (#6264)

## 2.25.11 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.25.10 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.25.9 (2021-09-25)

requests: Response.encoding can be None (#6067)

The type of the `encoding` attribute was previously typed as `str`, even though it can be `None` at runtime.

## 2.25.8 (2021-09-21)

Update Session.prepare_request, .get_adapter (#6058)

## 2.25.7 (2021-09-20)

Support name, content-type and headers in file upload (#6052)

`requests` supports not only passing binary file-like objects for multi-part file uploads but also additionally passing a name,  content-type and headers. This adds type hints for those options.

See https://docs.python-requests.org/en/master/user/quickstart/#post-a-multipart-encoded-file.

