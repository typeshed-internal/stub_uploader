## 4.64.7.13 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 4.64.7.12 (2023-02-07)

Complete stubtest and fix `Any` subclassing in `tqdm` (#9525)

## 4.64.7.11 (2023-01-18)

Improve pre-commit config (#9563)

- Add a few more hooks. These are all very fast, and I've found them useful in other projects:
  - Autofixes:
    - `trailing-whitespace`: fixes trailing whitespace
    - `requirements-txt-fixer`: alphabetises items in `requirements.txt` files
    - `end-of-file-fixer`: makes sure every file ends with a single newline character
    - `mixed-line-ending`: Makes sure Windows users don't accidentally introduce CRLF line endings into a file that uses LF line endings
  - None-autofixes:
    - `check-yaml`: loads YAML files to validate syntax
    - `check-toml`: loads TOML files to validate syntax
    - `check-merge-conflict`: detects merge-conflict strings in files and blocks them from accidentally being committed
    - `check-case-conflict`: checks for files with names that would conflict on a case-insensitive filesystem like MacOS HFS+ or Windows FAT; blocks them from being committed.
  - Change the bot schedule to quarterly, to reduce noisy PRs
  - Change the `black` language target-version to Python 3.10, synching the setting here with the changes that were made to our `pyproject.toml` file in #7538

## 4.64.7.10 (2023-01-13)

Fix some Any subclassing in tqdm (#9505)

## 4.64.7.9 (2022-11-23)

tqdm: Add missing tqdm.monitor class variable (#9249)

Co-authored-by: Gabriel Smith <gabriel.smith@precisionot.com>

## 4.64.7.3 (2022-11-11)

tqdm: allow `disable=None` in `tqdm.__init__` (#9154)

## 4.64.7.2 (2022-11-08)

Fix and allow classes with missing metaclasses (#9136)

## 4.64.7.1 (2022-10-16)

Remove empty `__init__` methods from classes with 0 parents (#8907)

## 4.64.7 (2022-09-27)

Bump mypy to 0.981 (#8796)

## 4.64.6 (2022-08-24)

tqdm: All `leave` arguments can be `None` (#8603)

All `leave` arguments are optional in tqdm.

## 4.64.5 (2022-08-18)

Support extras in stubtest_third_party.py (#8467)

## 4.64.4 (2022-07-15)

`tqdm`: Add `__all__` to `__init__.pyi` and submodules (#8308)

Fixes #8307

## 4.64.3 (2022-07-15)

`tqdm`: Improve a few `__init__` methods (#8246)

## 4.64.2 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 4.64.1 (2022-07-07)

Improve `tqdm.contrib.logging` context managers (#8251)

## 4.64.0 (2022-07-05)

Add stubs for `tqdm` (#8235)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

