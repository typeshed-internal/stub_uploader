## 70.2.0.20240704 (2024-07-04)

Bump setuptools to 70.2.* (#12261)

## 70.1.0.20240627 (2024-06-27)

Update setuptools to v70.1.1 (#12215)

## 70.1.0.20240625 (2024-06-25)

[setuptools] Update to 71.1.* (#12176)

## 70.0.0.20240524 (2024-05-24)

Small fix for pkg_resources StrPath (#12015)

## 70.0.0.20240523 (2024-05-23)

Make `shutil.rmtree.onexc` parameter optional (#12002)

Bump setuptools to 70.0 (#11994)

## 69.5.0.20240522 (2024-05-22)

`distutils` & `setuptools`: Relax path related params (#11948)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 69.5.0.20240519 (2024-05-19)

Make `distutils.dist.Distribution.get_command_obj` not return `None` by default (#11950)

`distutils` & `setuptools`: Complete `sub_commands` `ClassVar` typing (#11951)

## 69.5.0.20240518 (2024-05-18)

`distutils`: improve boolean parameters with int defaults (#11928)

## 69.5.0.20240513 (2024-05-13)

Avoid using new `_typeshed` protocol in `pkg_resources` for now (#11909)

Use protocols instead of `importlib.abc.Loader/MetaPathFinder/PathEntryFinder` (#11890)

## 69.5.0.20240423 (2024-04-23)

Add precise values for enum members where possible (#11299)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Alex Waygood <alex.waygood@gmail.com>

## 69.5.0.20240415 (2024-04-15)

Ensure that distutils and setuptools._distutils stay consistent (#11758)

Update setuptools to 69.5.* (#11756)

## 69.2.0.20240317 (2024-03-17)

Add `distutils` as a top-level package included with `types-setuptools` (#10948)

`setuptools`&`distutils`: `setup` returns a `Distribution` (#11617)

`setup` returns a `Distribution`

## 69.2.0.20240316 (2024-03-16)

Bump setuptools to 69.2.* (#11603)

## 69.1.0.20240310 (2024-03-10)

`pkg_resources`: Make `_InstallerType` stricter and generic (#11527)

Bump mypy to 1.9, add to json.encoder, small fixups (#11549)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 69.1.0.20240309 (2024-03-09)

Use strict pyright configs for `pkg_resources` (#11538)

`pkg_resources`: Updates from upstream typing merge (#11455)

## 69.1.0.20240308 (2024-03-08)

`pkg_resources`: Remove stray `Any`s and use more `Self` & `NoReturn` types (#11528)

## 69.1.0.20240302 (2024-03-02)

`pkg_resources`: Remove type-only `_Importer` class (#11512)

`pkg_resources`: Types from assignments and aliases (#11511)

Override `pkg_resources.ZipProvider.loader` type (#11514)

## 69.1.0.20240301 (2024-03-01)

`setuptools` & `pkg_resources`: Complete `VendorImporter` class (#11495)

`pkg_resources`: don't ignore "missing symbol from stub" in stubtest (#11494)

Fix invalid noqa comments and poorly formatted type ignores (#11497)

## 69.1.0.20240229 (2024-02-29)

`pkg_resources`: Reorder names to be closer to implementation (#11493)

## 69.1.0.20240223 (2024-02-23)

Improve typing of `sysconfig.get_config_var(s)` (#11454)

## 69.1.0.20240217 (2024-02-17)

fix: typo on setuptools (#11432)

## 69.1.0.20240215 (2024-02-15)

Bump setuptools to 69.1.* (#11423)

## 69.0.0.20240125 (2024-01-25)

Add missing `long_description_content_type` kwarg to setuptools (#11309)

## 69.0.0.20240115 (2024-01-15)

Fix types for `setuptools._distutils.ccompiler.CCompiler.compile` (#11275)

## 69.0.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 69.0.0.0 (2023-11-29)

Bump setuptools to 69.0.* (#11069)

Co-authored-by: Avasam <samuel.06@hotmail.com>

## 68.2.0.2 (2023-11-24)

Third-party stubs: remove unused `type: ignore`s (#11063)

## 68.2.0.1 (2023-11-09)

Bump flake8-pyi to 23.11.0 (#10997)

## 68.2.0.0 (2023-09-07)

[stubsabot] Bump setuptools to 68.2.* (#10674)

Release: https://pypi.org/pypi/setuptools/68.2.0
Homepage: https://github.com/pypa/setuptools
Repository: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v68.1.2...v68.2.0

Stubsabot analysis of the diff between the two releases:
 - 1 public Python file has been added: `setuptools/tests/test_core_metadata.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 7 files included in typeshed's stubs have been modified or renamed: `setuptools/__init__.py`, `setuptools/command/editable_wheel.py`, `setuptools/command/egg_info.py`, `setuptools/depends.py`, `setuptools/dist.py`, `setuptools/monkey.py`, `setuptools/namespaces.py`.
 - Total lines of Python code added: 1051.
 - Total lines of Python code deleted: 682.

## 68.1.0.1 (2023-08-30)

setuptools: add various missing objects and annotations (#10639)

## 68.1.0.0 (2023-08-16)

[stubsabot] Bump setuptools to 68.1.* (#10588)

Release: https://pypi.org/pypi/setuptools/68.1.0
Homepage: https://github.com/pypa/setuptools
Repository: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v68.0.0...v68.1.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 42 files included in typeshed's stubs have been modified or renamed.
 - Total lines of Python code added: 3401.
 - Total lines of Python code deleted: 2264.

## 68.0.0.3 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 68.0.0.2 (2023-07-15)

Add stubs for `pkg_resources._vendor.packaging` (#10423)

## 68.0.0.1 (2023-07-04)

Bring back a few setuptools._distutils files (#10401)

## 68.0.0.0 (2023-06-21)

Bump setuptools to 68.0 (#10339)

* Any -> Incomplete in a few files
* Bump setuptools to 68.0.*

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 67.8.0.0 (2023-05-20)

[stubsabot] Bump setuptools to 67.8.* (#10194)

Release: https://pypi.org/pypi/setuptools/67.8.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v67.7.2...v67.8.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 2 files included in typeshed's stubs have been modified or renamed: `setuptools/command/easy_install.py`, `setuptools/version.py`.
 - Total lines of Python code added: 425.
 - Total lines of Python code deleted: 215.

---------

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 67.7.0.3 (2023-05-19)

Don't ignore missing stubs in setuptools (#10058)

## 67.7.0.2 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 67.7.0.1 (2023-05-01)

Avoid unnecessary forward refs in class definitions (#10124)

## 67.7.0.0 (2023-04-22)

setuptools: bump to 67.7 (#10069)

Fixes #10067

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 67.6.0.8 (2023-04-17)

Add missing exception classes in `setuptools.errors` (#10057)

Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 67.6.0.7 (2023-04-04)

`google-cloud-ndb`, `paramiko`, `setuptools`: remove unnecessary `= ...`s (#10011)

## 67.6.0.6 (2023-03-28)

Add defaults for third-party stubs Q-T (#9959)

## 67.6.0.5 (2023-03-17)

distutils/setuptools: Don't use wildcards for allowlist entries (#9900)

Fill out more annotations for `distutils` & `setuptools` dist (#9895)

Signed-off-by: Henry Schreiner <henryschreineriii@gmail.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 67.6.0.4 (2023-03-17)

[setuptools] Fully annotate Extension.__init__ (#9899)

Add defaults to distutils.Extension.__init__

## 67.6.0.3 (2023-03-17)

[distutils] Add generated methods to Distribution (#9896)

## 67.6.0.2 (2023-03-16)

`distutils.command.build_ext`: add more annotations to `get_ext_*` methods (#9894)

Signed-off-by: Henry Schreiner <henryschreineriii@gmail.com>

Add missing `distribution` attribute to `distutils.cmd.Command` (#9893)

Signed-off-by: Henry Schreiner <henryschreineriii@gmail.com>

## 67.6.0.1 (2023-03-16)

Add remaining types to setuptools.build_meta (#9890)

Signed-off-by: Henry Schreiner <henryschreineriii@gmail.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 67.6.0.0 (2023-03-09)

[stubsabot] Bump setuptools to 67.6.* (#9858)

Release: https://pypi.org/pypi/setuptools/67.6.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v67.5.1...v67.6.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 1 file included in typeshed's stubs has been modified or renamed: `setuptools/wheel.py`.
 - Total lines of Python code added: 38.
 - Total lines of Python code deleted: 19.

## 67.5.0.0 (2023-03-06)

Update pkg_resources-stubs for use in pytype_test (#9747)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

[stubsabot] Bump setuptools to 67.5.* (#9841)

Release: https://pypi.org/pypi/setuptools/67.5.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v67.4.0...v67.5.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 1 file included in typeshed's stubs has been modified or renamed: `pkg_resources/__init__.py`.
 - Total lines of Python code added: 28.
 - Total lines of Python code deleted: 23.

## 67.4.0.3 (2023-02-26)

Remove most of `setuptools._distutils` (#9795)

## 67.4.0.2 (2023-02-26)

Improve many `__(a)exit__` annotations (#9696)

## 67.4.0.1 (2023-02-22)

Update `Unused` parameters in `stubs/` (#9704)

* Update _Unused TypeAlias

* Update `object | None` params

* Replace unused `object` parameters with `Unused` alias

## 67.4.0.0 (2023-02-22)

[stubsabot] Bump setuptools to 67.4.* (#9794)

Release: https://pypi.org/pypi/setuptools/67.4.0
Homepage: https://github.com/pypa/setuptools
Changelog: https://setuptools.pypa.io/en/stable/history.html
Diff: https://github.com/pypa/setuptools/compare/v67.3.3...v67.4.0

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 877.
 - Total lines of Python code deleted: 433.

## 67.3.0.2 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 67.3.0.1 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 67.3.0.0 (2023-02-15)

[stubsabot] Bump setuptools to 67.3.* (#9738)

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

