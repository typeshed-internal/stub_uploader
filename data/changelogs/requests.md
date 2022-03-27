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

