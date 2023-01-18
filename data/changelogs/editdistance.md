## 0.6.3.3 (2023-01-18)

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

## 0.6.3.2 (2022-12-18)

`editdistance`: delete the `bycython` submodule (#9380)

## 0.6.3.1 (2022-10-20)

Remove `editdistance` from `pyright`'s exclude (#8941)

## 0.6.3 (2022-07-19)

Add missing third party modules (#8321)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: hauntsaninja <>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 0.6.2 (2022-07-17)

Make xxhash, editdistance into packages (#8320)

This matches the runtime. Also see #8319

## 0.6.1 (2022-06-25)

dj-database-url, docopt, editdistance, first: check missing defs (#8154)

## 0.6.0 (2022-06-21)

[stubsabot] Bump editdistance to 0.6.* (#8120)

Co-authored-by: hauntsaninja <>

## 0.5.3 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 0.5.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

