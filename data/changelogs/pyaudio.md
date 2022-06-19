## 0.2.16 (2022-06-19)

stubtest: use separate table in METADATA.toml (#8096)

## 0.2.15 (2022-05-21)

Simplify and correct many numeric unions (#7906)

Unblocks PyCQA/flake8-pyi#222

## 0.2.14 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 0.2.13 (2022-04-27)

Drop Python 2 support in third-party stubs (#7703)

## 0.2.12 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 0.2.11 (2022-03-19)

PEP 604: Remove some more uses of Union/Optional (#7515)

The following patterns still break mypy:

1. `type[]` at top level fails
2. `tuple[T1, T2]` at top level fails (but `tuple[T1, ...]` is fine)
3. `T1 | Callable[..., T2 | T3]` fails, but only <=3.9

This PR cleans up usage of `Union` and `Optional` outside these patterns.

## 0.2.10 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 0.2.9 (2022-01-16)

remove "= ..." from top-level values (#6930)

## 0.2.7 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 0.2.6 (2021-12-27)

Replace METADATA stubtest key with stubtest_apt_packages (#6704)

## 0.2.5 (2021-12-25)

Add a 'stubtest' flag to METADATA.toml (#6687)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 0.2.4 (2021-10-12)

Add star to all non-0.1 versions (#6146)

