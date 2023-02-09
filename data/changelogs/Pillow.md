## 9.4.0.10 (2023-02-09)

Pillow: Add missing enums from 9.1.0 (#9698)

## 9.4.0.9 (2023-02-09)

Use `_typeshed.FileDescriptorOrPath` in stubs (#9695)

## 9.4.0.8 (2023-02-07)

Enable flake8-pyi's Y037 (#9686)

## 9.4.0.7 (2023-02-06)

Use `OSError` instead of `IOError` (#9683)

## 9.4.0.6 (2023-02-01)

Bump black to 23.1.0 (#9647)

## 9.4.0.5 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9565)

## 9.4.0.4 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 9.4.0.3 (2023-01-17)

`types-Pillow`: Allow stubtest to validate `PIL.FpxImagePlugin` and `PIL.MicImagePlugin` (#9531)

## 9.4.0.2 (2023-01-14)

Update various comments now non-types dependencies are allowed (#9527)

## 9.4.0.1 (2023-01-13)

Allowlist-only fixes for stubtest on Windows (#9522)

## 9.4.0.0 (2023-01-05)

Bump Pillow to 9.4 (#9453)

Closes #9448

## 9.3.0.4 (2022-12-05)

PIL: fix image convert palette type (#9331)

## 9.3.0.3 (2022-12-05)

PIL: add optimize param to save (#9328)

## 9.3.0.2 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 9.3.0.1 (2022-11-09)

Annotate known magic-method return types (#9131)

## 9.3.0.0 (2022-10-30)

[stubsabot] Bump Pillow to 9.3.* (#9039)

Release: https://pypi.org/pypi/Pillow/9.3.0
Homepage: https://python-pillow.org
Changelog: https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst
Diff: https://github.com/python-pillow/Pillow/compare/9.2.0...9.3.0

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 4163.
 - Total lines of Python code deleted: 3435.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 9.2.2.2 (2022-10-15)

Use `Incomplete` instead of `Any` in `__getattr__` (#8903)

## 9.2.2.1 (2022-10-10)

Allow PIL.Image.MAX_IMAGE_PIXELS to be None (#8876)

`_decompression_bomb_check()` explicitly checks for `None` and handles it as "unlimited".

## 9.2.2 (2022-09-20)

fix: pillow.ImageDraw.textlength may return float (#8773)

## 9.2.1 (2022-07-29)

[pillow] add new `PIL.Image` enums (#8419)

Co-authored-by: Shantanu <12621235+hauntsaninja@users.noreply.github.com>

## 9.2.0 (2022-07-04)

[stubsabot] Bump Pillow to 9.2.* (#8226)

Improve`_Color` type alias of `PIL.Image` (#8210)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 9.0.20 (2022-06-17)

Fix `box` parameter type of `Pillow.PIL.Image.paste` (#8090)

When executing `img.paste(cropped, box=(10.5, 10.5))`:
TypeError: 'float' object cannot be interpreted as an integer

So the `box` parameter's type should be not `tuple[float, float]` but `tuple[int, int]`. (same as `_Box`)

## 9.0.19 (2022-05-27)

Pillow: change `_Mode` type alias to `str` (#7967)

## 9.0.18 (2022-05-26)

Pillow: Add missing image modes to `_Mode` type alias in `Image.pyi` stub (issue #7956) (#7960)

## 9.0.17 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 9.0.16 (2022-05-25)

`Pillow`: use union type for `Image.paste` (#7893)

## 9.0.15 (2022-05-08)

#7805: Ensure all references to mode are Literals, not str. (#7807)

## 9.0.14 (2022-04-27)

Add various missing generic arguments (#7702)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 9.0.13 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 9.0.12 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 9.0.11 (2022-04-05)

Replace Union with union operator (#7596)

## 9.0.10 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 9.0.9 (2022-04-01)

Third-party stubs: Improve several `__exit__` methods (#7575)

## 9.0.8 (2022-03-19)

Use PEP 604 syntax wherever possible, part II (#7514)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

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

