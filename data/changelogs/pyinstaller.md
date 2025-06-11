## 6.14.0.20250611 (2025-06-11)

[stubsabot] Bump pyinstaller to 6.14.* (#14217)

Co-authored-by: stubsabot <>

## 6.13.0.20250417 (2025-04-17)

Bump pyinstaller to 6.13.* (#13843)

Add all classes in `stubs/pyinstaller/PyInstaller/utils/win32/versioninfo.pyi` (#13833)

## 6.12.0.20250308 (2025-03-08)

PyInstaller: Complete types in splash.pyi (#13568)

---------

Co-authored-by: Avasam <samuel.06@hotmail.com>

## 6.12.0.20250301 (2025-03-01)

Fix `pyinstaller.utils.hooks.collect_entry_point` return type (#13111)

## 6.12.0.20250226 (2025-02-26)

PyInstaller: Complete types in build_main.pyi (#13528)

Co-authored-by: sobolevn <mail@sobolevn.me>

## 6.12.0.20250223 (2025-02-23)

Fix typo in PyInstaller type alias (#13525)

## 6.12.0.20250210 (2025-02-10)

[stubsabot] Bump pyinstaller to 6.12.* (#13479)

Co-authored-by: stubsabot <>

## 6.11.0.20250130 (2025-01-30)

Upgrade Black and Ruff (#13443)

## 6.11.0.20241028 (2024-10-28)

Bump pyinstaller to 6.11.* (#12911)

## 6.10.0.20240812 (2024-08-12)

Bump pyinstaller to 6.10.* (#12513)

## 6.9.0.20240710 (2024-07-10)

[stubsabot] Bump pyinstaller to 6.9.* (#12289)

Co-authored-by: stubsabot <>

## 6.8.0.20240626 (2024-06-26)

Bump pyinstaller to 6.8.* (#12198)

## 6.6.0.20240426 (2024-04-26)

pyinstaller: allow `Splash(text_pos = None)` (#11835)

## 6.6.0.20240417 (2024-04-17)

Remove remaining bare `Incomplete`s (#11768)

Enable Y065

## 6.6.0.20240415 (2024-04-15)

Bump pyinstaller to 6.6.* (#11764)

## 6.5.0.20240311 (2024-03-11)

Bump pyinstaller to 6.5.* (#11563)

Use PEP 570 syntax in third party stubs (#11554)

## 6.4.0.20240212 (2024-02-12)

[stubsabot] Bump pyinstaller to 6.4.* (#11398)

## 6.3.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

Remove Python 3.7 branches (#11238)

## 6.3.0.20240105 (2024-01-05)

Drop support for Python 3.7 (#11234)

## 6.3.0.0 (2023-12-18)

Bump pyinstaller to 6.3.* (#11175)

## 6.2.0.1 (2023-11-24)

Third-party stubs: remove unused `type: ignore`s (#11063)

## 6.2.0.0 (2023-11-13)

Bump pyinstaller to 6.2.* (#11023)

Update `PyInstaller.building.api.EXE.__init__` (#11024)

## 6.1.0.1 (2023-11-09)

Bump flake8-pyi to 23.11.0 (#10997)

## 6.1.0.0 (2023-10-14)

[stubsabot] Bump pyinstaller to 6.1.* (#10885)

Release: https://pypi.org/pypi/pyinstaller/6.1.0
Homepage: https://www.pyinstaller.org/
Repository: https://github.com/pyinstaller/pyinstaller
Diff: https://github.com/pyinstaller/pyinstaller/compare/v6.0.0...v6.1.0

Stubsabot analysis of the diff between the two releases:
 - 2 public Python files have been added: `tests/functional/modules/pyi_import_main/hooks/hook-PyInstaller.py`, `tests/functional/modules/pyi_import_main/hooks/hook-pytest.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 5 files included in typeshed's stubs have been modified or renamed: `PyInstaller/__init__.py`, `PyInstaller/building/api.py`, `PyInstaller/building/build_main.py`, `PyInstaller/depend/analysis.py`, `PyInstaller/utils/hooks/__init__.py`.
 - Total lines of Python code added: 122.
 - Total lines of Python code deleted: 22.

## 6.0.0.1 (2023-10-06)

PyInstaller: List ignored `building` sub-modules explicitly for stubtest (#10845)

This prevents stubtest from ignoring errors in modules that are stubbed.

## 6.0.0.0 (2023-09-29)

Bump pyinstaller to 6.0.* (#10800)

## 5.13.0.2 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 5.13.0.1 (2023-06-27)

[PyInstaller] TOCs are not often lists of TOCs (#10366)

## 5.13.0.0 (2023-06-25)

[stubsabot] Bump pyinstaller to 5.13.* (#10357)

* [stubsabot] Bump pyinstaller to 5.13.*

Release: https://pypi.org/pypi/pyinstaller/5.13.0
Homepage: https://www.pyinstaller.org/
Diff: https://github.com/pyinstaller/pyinstaller/compare/v5.12.0...v5.13.0

Stubsabot analysis of the diff between the two releases:
 - 1 public Python file has been added: `PyInstaller/hooks/pre_safe_import_module/hook-distutils.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 4 files included in typeshed's stubs have been modified or renamed: `PyInstaller/__init__.py`, `PyInstaller/building/api.py`, `PyInstaller/building/build_main.py`, `PyInstaller/compat.py`.
 - Total lines of Python code added: 962.
 - Total lines of Python code deleted: 648.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

* Update compat.pyi

---------

Co-authored-by: stubsabot <>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 5.12.0.0 (2023-06-09)

[stubsabot] Bump pyinstaller to 5.12.* (#10287)

Release: https://pypi.org/pypi/pyinstaller/5.12.0
Homepage: https://www.pyinstaller.org/
Diff: https://github.com/pyinstaller/pyinstaller/compare/v5.11.0...v5.12.0

Stubsabot analysis of the diff between the two releases:
 - 2 public Python files have been added: `tests/functional/scripts/pyi_lazy_import.py`, `tests/functional/test_import_lazy_loader.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 6 files included in typeshed's stubs have been modified or renamed: `PyInstaller/__init__.py`, `PyInstaller/building/build_main.py`, `PyInstaller/building/splash.py`, `PyInstaller/compat.py`, `PyInstaller/lib/modulegraph/modulegraph.py`, `PyInstaller/utils/win32/versioninfo.py`.
 - Total lines of Python code added: 647.
 - Total lines of Python code deleted: 887.

## 5.11.0.0 (2023-05-14)

Bump `PyInstaller` to `5.11.*` (#10179)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 5.10.0.1 (2023-04-27)

Type `PyInstaller.building.api` and related modules (#9730)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 5.10.0.0 (2023-04-12)

[stubsabot] Bump pyinstaller to 5.10.* (#10034)

## 5.9.0.1 (2023-03-27)

Add default values for third-party stubs beginning with 'P' (#9957)

## 5.9.0.0 (2023-03-14)

[stubsabot] Bump pyinstaller to 5.9.* (#9880)

Release: https://pypi.org/pypi/pyinstaller/5.9.0
Homepage: https://www.pyinstaller.org/
Diff: https://github.com/pyinstaller/pyinstaller/compare/v5.8.0...v5.9.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 3 files included in typeshed's stubs have been modified or renamed: `PyInstaller/__init__.py`, `PyInstaller/building/build_main.py`, `PyInstaller/isolated/_parent.py`.
 - Total lines of Python code added: 28.
 - Total lines of Python code deleted: 59.

## 5.8.0.3 (2023-02-24)

Fix some typos in comments (#9802)

## 5.8.0.2 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 5.8.0.1 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 5.8.0.0 (2023-02-12)

Bump pyinstaller to 5.8.* (#9721)

Release: https://pypi.org/pypi/pyinstaller/5.8.0
Homepage: https://www.pyinstaller.org/
Diff: https://github.com/pyinstaller/pyinstaller/compare/v5.7.0...v5.8.0

## 5.7.0.6 (2023-02-09)

Use `_typeshed.FileDescriptorOrPath` in stubs (#9695)

## 5.7.0.5 (2023-02-02)

Manual changes of `Any` union to `Incomplete` in stubs folder (#9566)

- ClassVar[Any | None]
- Missed previous changes due to alias
- Manual review of leftover Any unions (`| Any` and `Any |`)

## 5.7.0.4 (2023-02-01)

Add defaults for params and constants in pyinstaller (#9640)

## 5.7.0.3 (2023-01-25)

Fix some stubtest complaints before they happen (#9585)

Add missing objects to various stubs

## 5.7.0.2 (2023-01-14)

Update various comments now non-types dependencies are allowed (#9527)

## 5.7.0.1 (2023-01-11)

types-pyinstaller: no longer subclass "Any" (#9495)

## 5.7.0.0 (2022-12-08)

Bump pyinstaller to 5.7.* (#9343)

## 5.6.0.4 (2022-11-16)

Always use `bool` and `Literal` for Python compat code (#9213)

## 5.6.0.3 (2022-11-07)

`PyInstaller`: Fix `DeprecationWarning` when parsing the stub using `ast.parse()` (#9112)

```python
>>> import ast, warnings
>>> warnings.filterwarnings("always")
>>> with open("typeshed/stubs/pyinstaller/pyi_splash/__init__.pyi", encoding="utf-8") as file:
...     source = file.read()
...
>>> ast.parse(source)
<unknown>:11: DeprecationWarning: invalid escape sequence '\u'
<ast.Module object at 0x0000027EAF6D3AF0>
```

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 5.6.0.2 (2022-11-03)

Update pyright to 1.1.278 (#9077)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 5.6.0.1 (2022-11-03)

importlib: improve bytes handling (#9070)

## 5.6.0.0 (2022-10-25)

Bump pyinstaller to 5.6.* (#8981)

## 5.5.0.0 (2022-10-10)

Bump PyInstaller-stubs to 5.5 (#8874)

## 5.4.2 (2022-09-27)

Bump mypy to 0.981 (#8796)

## 5.4.1 (2022-09-22)

Add reportMissingParameterType to `pyrightconfig.stricter.json` (#8770)

Pyinstaller: use `StrPath` over `StrOrBytesPath` (#8780)

Fix incorrect StrOrBytesPath in PyInstaller stubs
Change StrOrBytesPath to StrPath when exclusively used with strings.

## 5.4.0 (2022-09-15)

Add stubs for `PyInstaller` (public API only) (#8702)

