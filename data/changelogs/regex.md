## 2024.11.6.20250318 (2025-03-18)

Fix various argument of extension modules (#13651)

* Mark various positional-only arguments: These are all positional-only
  arguments in C code using the `METH_O` flag.
* Remove various `*args, **kwargs` arguments that are using the
  `METH_NOARGS` flag in C.

## 2024.11.6.20250305 (2025-03-05)

Enable Ruff PLE (Pylint Error) (#13305)

## 2024.11.6.20241221 (2024-12-21)

Update to mypy 1.14 (#13272)

## 2024.11.6.20241108 (2024-11-08)

[stubsabot] Bump regex to 2024.11.6 (#12967)

## 2024.9.11.20240912 (2024-09-12)

[stubsabot] Bump regex to 2024.9.11 (#12641)

Release: https://pypi.org/pypi/regex/2024.9.11
Homepage: https://github.com/mrabarnett/mrab-regex
Repository: https://github.com/mrabarnett/mrab-regex
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2024.7.24...2024.9.11

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 7.
 - Total lines of Python code deleted: 3.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2024.7.24.20240726 (2024-07-26)

[stubsabot] Bump regex to 2024.7.24 (#12424)

## 2024.5.15.20240519 (2024-05-19)

Mark pos-only __class_getitem__ args (#11970)

Use assignment instead of annotation in third party enums (#11957)

## 2024.5.15.20240516 (2024-05-16)

[stubsabot] Bump regex to 2024.5.15 (#11918)

Co-authored-by: stubsabot <>

## 2024.5.10.20240512 (2024-05-12)

regex: functions do not accept any buffer for pattern (#11899)

## 2024.5.10.20240511 (2024-05-11)

[stubsabot] Bump regex to 2024.5.10 (#11894)

Release: https://pypi.org/pypi/regex/2024.5.10
Homepage: https://github.com/mrabarnett/mrab-regex
Repository: https://github.com/mrabarnett/mrab-regex
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2024.4.28...2024.5.10

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 6.
 - Total lines of Python code deleted: 4.

## 2024.4.28.20240506 (2024-05-06)

regex: improve Pattern annotations (#11862)

- Corrected types for `pos` and `endpos` arguments to `int | None = None`
- Corrected type for `timeout` argument to `float | None = None`
- Added default value `None` for `concurrent` and `timeout` parameters
- Added default value `0` for `maxsplit` parameter
- Added `partial` parameter where applicable
- Removed invalid `flags` parameter from `sub` methods

## 2024.4.28.20240430 (2024-04-30)

[stubsabot] Bump regex to 2024.4.28 (#11842)

Release: https://pypi.org/pypi/regex/2024.4.28
Homepage: https://github.com/mrabarnett/mrab-regex
Repository: https://github.com/mrabarnett/mrab-regex
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2024.4.16...2024.4.28

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 10.
 - Total lines of Python code deleted: 7.

## 2024.4.16.20240423 (2024-04-23)

Add precise values for enum members where possible (#11299)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Alex Waygood <alex.waygood@gmail.com>

## 2024.4.16.20240418 (2024-04-18)

[stubsabot] Bump regex to 2024.4.16 (#11773)

## 2023.12.25.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 2023.12.25.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 2023.12.25.20231225 (2023-12-25)

[stubsabot] Bump regex to 2023.12.25 (#11198)

## 2023.10.3.0 (2023-10-04)

[stubsabot] Bump regex to 2023.10.3 (#10832)

## 2023.8.8.0 (2023-08-10)

[stubsabot] Bump regex to 2023.8.8 (#10553)

Release: https://pypi.org/pypi/regex/2023.8.8
Homepage: https://github.com/mrabarnett/mrab-regex
Repository: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2023.6.3...2023.8.8

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 15.
 - Total lines of Python code deleted: 10.

## 2023.6.3.1 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 2023.6.3.0 (2023-06-04)

[stubsabot] Bump regex to 2023.6.3 (#10252)

Release: https://pypi.org/pypi/regex/2023.6.3
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2023.5.5...2023.6.3

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 8.
 - Total lines of Python code deleted: 2.

## 2023.5.5.0 (2023-05-04)

[stubsabot] Bump regex to 2023.5.5 (#10138)

Release: https://pypi.org/pypi/regex/2023.5.5
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2023.5.4...2023.5.5

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 2.
 - Total lines of Python code deleted: 2.

## 2023.5.4.0 (2023-05-03)

[stubsabot] Bump regex to 2023.5.4 (#10131)

Release: https://pypi.org/pypi/regex/2023.5.4
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2023.3.23...2023.5.4

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 8.
 - Total lines of Python code deleted: 3.

## 2023.3.23.1 (2023-03-28)

Add defaults for third-party stubs Q-T (#9959)

## 2023.3.23.0 (2023-03-24)

[stubsabot] Bump regex to 2023.3.23 (#9933)

Release: https://pypi.org/pypi/regex/2023.3.23
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2023.03.22...2023.3.23

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 2.
 - Total lines of Python code deleted: 2.

## 2023.3.22.0 (2023-03-23)

[stubsabot] Bump regex to 2023.3.22 (#9927)

Release: https://pypi.org/pypi/regex/2023.3.22
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2022.10.31...2023.03.22

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 6.
 - Total lines of Python code deleted: 8.

## 2022.10.31.6 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 2022.10.31.5 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 2022.10.31.4 (2023-02-07)

Improve pyright verification of third-party test cases in CI (#9650)

Co-authored-by: Avasam <samuel.06@hotmail.com>

## 2022.10.31.3 (2022-11-24)

Add test case for recent `types-regex` regression (#9269)

## 2022.10.31.2 (2022-11-24)

regex: fix type signatures using Scanner (#9266)

## 2022.10.31.1 (2022-11-23)

Mark regex as completed (#9214)

## 2022.10.31.0 (2022-11-01)

[stubsabot] Bump regex to 2022.10.31 (#9050)

Release: https://pypi.org/pypi/regex/2022.10.31
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2022.9.13...2022.10.31

Stubsabot analysis of the diff between the two releases:
 - Total lines of Python code added: 3.
 - Total lines of Python code deleted: 2.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2022.9.13.0 (2022-09-16)

[stubsabot] Bump regex to 2022.9.13 (#8751)

Release: https://pypi.org/project/regex/2022.9.13/
Homepage: https://github.com/mrabarnett/mrab-regex
Diff: https://github.com/mrabarnett/mrab-regex/compare/2022.8.17...2022.9.13

## 2022.8.17.0 (2022-08-19)

[stubsabot] Bump regex to 2022.8.17 (#8562)

Co-authored-by: stubsabot <>

## 2022.7.25.0 (2022-07-29)

[stubsabot] Bump regex to 2022.7.25 (#8432)

Co-authored-by: stubsabot <>

## 2022.7.9.0 (2022-07-15)

[stubsabot] Bump regex to 2022.7.9 (#8300)

Co-authored-by: hauntsaninja <>

## 2022.6.2.0 (2022-06-26)

Bump regex to 2022.6.2 (#8162)

Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 2021.11.10.6 (2022-06-21)

`requests`, `regex`: use re-exports instead of assignments in a few places (#8127)

## 2021.11.10.5 (2022-05-11)

regex: accept buffers (#7680)

Similar to #7679

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2021.11.10.4 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2021.11.10.3 (2022-02-23)

regex stubs: Add __getitem__ method to Match (#7372)

## 2021.11.10.2 (2022-01-07)

Update pyright (#6840)

## 2021.11.10.0 (2021-12-30)

Add regex stubs (#6713)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

