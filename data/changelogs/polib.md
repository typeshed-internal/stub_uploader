## 1.2.0.20250401 (2025-04-01)

Add `__all__` part 2 (#13719)

---------

Co-authored-by: Avasam <samuel.06@hotmail.com>

## 1.2.0.20250114 (2025-01-14)

Allow Path in polib.pofile() (#13396)

* Allow PathLike in polib.pofile()

* Add missing import

* [pre-commit.ci] auto fixes from pre-commit.com hooks

* Update type to pathlib.Path

---------

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 1.2.0.20241221 (2024-12-21)

Update to mypy 1.14 (#13272)

## 1.2.0.20240811 (2024-08-11)

Fix type hint for `msgctxt` parameter in `polib` (#12506)

## 1.2.0.20240327 (2024-03-27)

polib: Fix POEntry.occurrences (#11661)

## 1.2.0.20240115 (2024-01-15)

[polib] Fix POEntry.msgstr_plural annotation (#11273)

## 1.2.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 1.2.0.1 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 1.2.0.0 (2023-02-24)

[stubsabot] Bump polib to 1.2.* (#9804)

Release: https://pypi.org/pypi/polib/1.2.0
Homepage: https://github.com/izimobil/polib/
Diff: https://github.com/izimobil/polib/compare/1.1.1...1.2.0

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 1 file included in typeshed's stubs has been modified or renamed: `polib.py`.
 - Total lines of Python code added: 293.
 - Total lines of Python code deleted: 195.

## 1.1.12.2 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 1.1.12.1 (2022-11-23)

Mark `polib` as complete (#9244)

## 1.1.12 (2022-04-27)

Drop Python 2 support from polib (#7714)

## 1.1.11 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.1.10 (2022-01-30)

Reduce use of `Any` in equality methods (#7081)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 1.1.9 (2022-01-17)

remove quoted strings (#6933)

## 1.1.8 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 1.1.6 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 1.1.5 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 1.1.4 (2021-10-12)

Add star to all non-0.1 versions (#6146)

