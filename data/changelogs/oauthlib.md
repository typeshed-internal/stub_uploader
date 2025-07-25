## 3.3.0.20250708 (2025-07-08)

[oauthlib] Add missing stubs (#14301)

[oauthlib] Fix type on body argument of oauthlib.oauth1.Client.sign() (#14295)

## 3.3.0.20250703 (2025-07-03)

Make Mapping.get(default) more constrained (#14360)

## 3.3.0.20250622 (2025-06-22)

Bump oauthlib to 3.3.* (#14300)

## 3.2.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 3.2.0.20250514 (2025-05-14)

Improve `oauthlib.oauth2.rfc6749` (#13965)

Improve `oauthlib.openid.connect.core` (#13966)

## 3.2.0.20250408 (2025-04-08)

Improve `oauthlib.oauth2.rfc6749` (#13793)

Improve `oauthlib` (#13794)

## 3.2.0.20250403 (2025-04-03)

Improve stubs for `oauthlib.oauth2.rfc6749` (#13752)

## 3.2.0.20250401 (2025-04-01)

Improve `oauthlib.common` (#13744)

## 3.2.0.20240806 (2024-08-06)

Bump mypy to 1.11.1 (#12463)

## 3.2.0.20240217 (2024-02-17)

oauthlib: Fix annotations for `oauthlib.oauth2.RequestValidator` (#11417)

## 3.2.0.20240124 (2024-01-24)

[oauthlib] Fix return types of `Client` methods (#9908)

## 3.2.0.20240105 (2024-01-05)

Add support for the refresh_token grant type (RefreshTokenGrant) (#11… (#11206)

Add support for the refresh_token grant type (RefreshTokenGrant).

## 3.2.0.10 (2023-09-18)

oauthlib: Update types for RequestValidator to match implementation (#10725)

## 3.2.0.9 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 3.2.0.8 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 3.2.0.7 (2023-03-27)

Add defaults for third-party stubs M-O (#9956)

## 3.2.0.6 (2023-03-11)

[oauthlib] Add types in oauth1/rfc5849/request_validator.pyi (#9844)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 3.2.0.5 (2023-02-23)

Remove unused `type: ignore` comments (#9801)

## 3.2.0.4 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 3.2.0.3 (2023-01-18)

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

## 3.2.0.2 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 3.2.0.1 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 3.2.0 (2022-06-18)

Bump oauthlib to 3.2.* (#8081)

## 3.1.5 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 3.1.4 (2021-11-18)

Revert "do not use mypy-specific syntax in '# type: ignore' comments" (#6338)

## 3.1.3 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 3.1.2 (2021-08-29)

do not use mypy-specific syntax in '# type: ignore' comments (#5953)

