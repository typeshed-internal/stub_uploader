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

