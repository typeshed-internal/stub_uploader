## 67.2.0.1 (2023-02-09)

Use `_typeshed.FileDescriptorOrPath` in stubs (#9695)

## 67.2.0.0 (2023-02-08)

[stubsabot] Bump setuptools to 67.2.* (#9691)

Release: https://pypi.org/pypi/setuptools/67.2.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v67.1.0...v67.2.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 33 files included in typeshed's stubs have been modified or renamed.
 - Total lines of Python code added: 152.
 - Total lines of Python code deleted: 111.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 67.1.0.2 (2023-02-07)

Enable flake8-pyi's Y037 (#9686)

## 67.1.0.1 (2023-02-07)

Bump mypy to 1.0 (#9684)

## 67.1.0.0 (2023-02-03)

Update setuptools to 67.1 (#9664)

Replace some instances of `Any` with `Incomplete` or proper types.

## 65.7.0.4 (2023-02-02)

setuptools: add pkg_resources.Requirement.url (#9657)

Co-authored-by: Shantanu <12621235+hauntsaninja@users.noreply.github.com>

## 65.7.0.3 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9565)

## 65.7.0.2 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 65.7.0.1 (2023-01-13)

Fix setuptools stubtest on windows (#9521)

## 65.7.0.0 (2023-01-12)

[stubsabot] Bump setuptools to 65.7.* (#9504)

Release: https://pypi.org/pypi/setuptools/65.7.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v65.6.3...v65.7.0

## 65.6.0.3 (2023-01-05)

Add `types-docutils` as a dependency of `types-setuptools` (#9460)

Remove the need for subclassing `Any`

## 65.6.0.2 (2022-12-06)

More pywin32 stub completion (#9308)

Completed based on usage of the following libraries in mypy_primer:
- apprise
- comtypes
As well as some of the most popular libraries that use both pywin32 and mypy (all over 1k stars on github):
- certbot
- anki
- flexget
- monkey
- twisted
- salt

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 65.6.0.1 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 65.6.0.0 (2022-11-20)

[stubsabot] Bump setuptools to 65.6.* (#9227)

Release: https://pypi.org/pypi/setuptools/65.6.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v65.5.1...v65.6.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 40 files included in typeshed's stubs have been modified or renamed.
 - Total lines of Python code added: 637.
 - Total lines of Python code deleted: 630.

Co-authored-by: stubsabot <>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 65.5.0.3 (2022-11-12)

Remove `setuptools._distutils.command.bdst_msi` (#9174)

It does not exist

## 65.5.0.2 (2022-10-24)

Fix `pkg_resources.split_sections` (#8975)

This function is currently documented as returning a list of lines as
the 2nd pair value.  It does not return plain str here.

## 65.5.0.1 (2022-10-16)

Remove empty `__init__` methods from classes with 0 parents (#8907)

## 65.5.0.0 (2022-10-15)

[stubsabot] Bump setuptools to 65.5.* (#8900)

Release: https://pypi.org/pypi/setuptools/65.5.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v65.4.1...v65.5.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 4 files included in typeshed's stubs have been modified or renamed: `setuptools/build_meta.py`, `setuptools/command/test.py`, `setuptools/monkey.py`, `setuptools/wheel.py`.
 - Total lines of Python code added: 111.
 - Total lines of Python code deleted: 59.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 65.4.0.0 (2022-09-30)

[stubsabot] Bump setuptools to 65.4.* (#8811)

Release: https://pypi.org/pypi/setuptools/65.4.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v65.3.0...v65.4.0

## 65.3.0 (2022-08-26)

[stubsabot] Bump setuptools to 65.3.* (#8620)

## 65.1.0 (2022-08-19)

Update setuptools to 65.1.* (#8565)

Fixes #8563

## 64.0.1 (2022-08-13)

setuptools: fix stubtest (#8540)

Fixes #8539

## 64.0.0 (2022-08-12)

[stubsabot] Bump setuptools to 64.0.* (#8534)

## 63.4.1 (2022-08-11)

setuptools: delete _distutils.command.check.HAS_DOCUTILS (#8529)

Fixes #8527

## 63.4.0 (2022-08-05)

[stubsabot] Bump setuptools to 63.4.* (#8493)

Co-authored-by: stubsabot <>

## 63.2.3 (2022-08-03)

Remove redundant `__str__` methods (#8475)

## 63.2.2 (2022-07-28)

Fix todo in setuptools.command.test (#8416)

With https://github.com/python/mypy/pull/10884 merged and released, this should be safe to re-enable per the todo comment.

https://github.com/pypa/setuptools/blob/main/setuptools/command/test.py#L117

## 63.2.1 (2022-07-20)

Update setuptools stubs (#8345)

setuptools now vendors `distutils` as `setuptools._distutils`.

## 63.2.0 (2022-07-15)

[stubsabot] Bump setuptools to 63.2.* (#8301)

Co-authored-by: hauntsaninja <>

## 62.6.1 (2022-07-11)

Remove Python 3.6 branches from typeshed (#8269)

## 62.6.0 (2022-07-08)

[stubsabot] Bump setuptools to 62.6.* (#8224)

Most of setuptools.config is not included as the module is deprecated.

## 57.4.18 (2022-06-26)

Third-party stubs: audit `Callable[<parameters>, None]` annotations (#8175)

## 57.4.17 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 57.4.16 (2022-05-25)

pkg_resources: Fix unconstrained TypeVars (#7941)

https://github.com/pypa/setuptools/blob/499c468a57d240e5bb450bdb6daedc3e559541dd/pkg_resources/__init__.py#L1049

Part of #7928

## 57.4.15 (2022-05-22)

More setuptools.command.easy_install definitions. (#7145)

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 57.4.14 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 57.4.13 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 57.4.12 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 57.4.11 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 57.4.10 (2022-03-08)

Widen the `cmdclass` parameter of `setuptools.setup` (#7458)

## 57.4.9 (2022-02-07)

Improve some in-place BinOp methods (#7149)

## 57.4.8 (2022-01-30)

Reduce use of `Any` in equality methods (#7081)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 57.4.7 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 57.4.5 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 57.4.4 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 57.4.3 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 57.4.2 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 57.4.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 57.4.0 (2021-09-19)

Add setuptools stubs (#5762)

