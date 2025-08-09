## 2.0.0.20250809 (2025-08-09)

Mark stub-only private symbols as `@type_check_only` in third-party stubs (#14545)

## 2.0.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 2.0.0.20250306 (2025-03-06)

Fix: OAuth1 type hints to include realm parameter (#13579)

## 2.0.0.20250119 (2025-01-19)

requests-oauthlib: decoding can be None (#13404)

it is passed along to oauthlib where the default there is None

## 2.0.0.20240417 (2024-04-17)

Remove remaining bare `Incomplete`s (#11768)

Enable Y065

## 2.0.0.20240324 (2024-03-24)

[stubsabot] Bump requests-oauthlib to 2.0.* (#11649)

Release: https://pypi.org/pypi/requests-oauthlib/2.0.0
Homepage: https://github.com/requests/requests-oauthlib
Repository: https://github.com/requests/requests-oauthlib
Diff: https://github.com/requests/requests-oauthlib/compare/v1.4.0...v2.0.0

Stubsabot analysis of the diff between the two releases:
 - 1 public Python file has been added: `tests/examples/__init__.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 1 file included in typeshed's stubs has been modified or renamed: `requests_oauthlib/__init__.py`.
 - Total lines of Python code added: 2.
 - Total lines of Python code deleted: 4.

## 1.4.0.20240315 (2024-03-15)

Bump requests-oauthlib to 1.4.* (#11601)

## 1.3.0.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 1.3.0.20240310 (2024-03-10)

Bump mypy to 1.9, add to json.encoder, small fixups (#11549)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 1.3.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 1.3.0.1 (2023-10-13)

Fix the type for `OAuth2Session.authorization_url` (#10878)

fix the type for `OAuth2Session.authorization_url`

## 1.3.0.0 (2023-09-11)

Add stubs for requests-oauthlib (#10658)

