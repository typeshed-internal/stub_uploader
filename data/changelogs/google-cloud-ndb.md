## 1.11.5 (2022-09-27)

google-cloud-ndb: drop dependency on types-six (#8793)

For https://github.com/typeshed-internal/stub_uploader/pull/61#discussion_r979327370

## 1.11.4 (2022-09-24)

google-cloud-ndb: bump stubtest protobuf requirement (#8786)

Bumps [protobuf](https://github.com/protocolbuffers/protobuf) from 3.20.1 to 3.20.2.
- [Release notes](https://github.com/protocolbuffers/protobuf/releases)
- [Changelog](https://github.com/protocolbuffers/protobuf/blob/main/generate_changelog.py)
- [Commits](https://github.com/protocolbuffers/protobuf/compare/v3.20.1...v3.20.2)

---
updated-dependencies:
- dependency-name: protobuf
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] <support@github.com>

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

## 1.11.3 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 1.11.2 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 1.11.1 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 1.11.0 (2022-04-05)

Update google-cloud-ndb stubs to 1.11 (#7593)

## 1.9.4 (2022-02-08)

google-cloud-ndb: Fix incorrect type definition for `validator` (#7116)

This function was mistakenly typed as `Callable[[Property], object] |
None`, however the actual function accepts two parameters of type
`Property, value`. The value can be of any type. Strictly speaking, the
type corresponds to the type of the property which is defined at runtime.

Fixes #7103

## 1.9.3 (2022-02-03)

Fix mistyped `get_by_id` class methods (#7120)

The types for these class methods were mixed up. The async method
returned an optional `Model`, while the synchronous method returned a
`Future`. It's the other way around.

Fixes #7103

Improve `__enter__` & constructor methods (#7114)

## 1.9.2 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 1.9.0 (2021-10-21)

Stubs for google.cloud.ndb the Google Cloud Datastore ndb client library (#5821)

