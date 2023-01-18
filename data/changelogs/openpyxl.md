## 3.0.4.5 (2023-01-18)

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

## 3.0.4.4 (2023-01-10)

openpyxl: Use "Incomplete" instead of "Any" (#9488)

## 3.0.4.3 (2022-12-03)

openpyxl stub: add open as an alias for load_workbook (#9324)

## 3.0.4.2 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 3.0.4.1 (2022-11-09)

Annotate known magic-method return types (#9131)

## 3.0.4 (2022-06-06)

Always use `TypeAlias` when assigning to `Any` (#8021)

## 3.0.3 (2022-05-27)

`openpyxl`: annotate openpyxl.utils.cell stubs (#7969)

## 3.0.2 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 3.0.1 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 3.0.0 (2022-03-07)

Add openpyxl stubs (#6801)

