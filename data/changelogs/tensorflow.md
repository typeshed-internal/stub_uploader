## 2.11.0.4 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 2.11.0.3 (2023-02-01)

Tensorflow: Add more stubs (#9560)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.11.0.2 (2023-01-18)

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

## 2.11.0.1 (2023-01-17)

Reenable flake8-pyi's Y011 and Y015 (#9551)

## 2.11.0.0 (2023-01-15)

Update tensorflow to 2.11 (#9543)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>

## 2.10.0.0 (2023-01-14)

Initial tensorflow stubs (#8974)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

