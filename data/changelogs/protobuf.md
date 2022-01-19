## 3.19.4 (2022-01-19)

Use `_typeshed.Self` in `protobuf/google/protobuf/message.pyi` (#6955)

Use PEP 585 syntax in Python 2, `protobuf` & `_ast` stubs, where possible (#6949)

Flatten stubtest_allowlist for protobuf generated files (#6944)

I added stubtest testing for generated files within mypy-protobuf.
There are many ways in which the protobuf code is doing *weird*
things and we want the stubs to look a bit different. They're enumerated
in the `stubtest_allowlist.txt` of mypy-protobuf, so squashing them here
so that this one can focus on the non-generated files.

## 3.19.0 (2022-01-10)

Bump protobuf to 3.19.2 (#6879)

## 3.18.3 (2022-01-03)

Add google.protobuf.internal.api_implementation (#6802)

## 3.18.2 (2021-11-27)

Improve stubs for sequence types (#6386)

## 3.18.1 (2021-11-21)

Fix MutableMapping overrides (#6352)

## 3.18.0 (2021-10-13)

Bump protobuf stub to 3.18.1 and mypy-protobuf 3.0.0 (#6157)

* Bump protobuf stub to 3.18.1 and mypy-protobuf 3.0.0

* Fix ConsumeInteger in google/protobuf/text_format.pyi

The arg was removed in protobuf 3.18

## 3.17.5 (2021-10-12)

Add star to all non-0.1 versions (#6146)

