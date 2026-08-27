## [0.8.0.20260827](https://pypi.org/project/types-hnswlib/0.8.0.20260827/) (2026-08-27)

* Fix SIGILL in stubtest by building without `-march=native` ([#16244](https://github.com/python/typeshed/pull/16244))

    hnswlib is source-only and compiles with -march=native by default. CI
    restores pip's wheel cache across runners with different CPUs, so a
    wheel built on one host can hit an illegal instruction on the next.
    That is the SIGILL (exit -4) with empty output from #16100.

    Add a general `install-environment` key to [tool.stubtest] that sets
    environment variables for the pip install step, and use it to pass
    hnswlib's own HNSWLIB_NO_NATIVE opt-out. This lets the darwin-only
    workaround from #16125 be dropped so hnswlib is tested on Linux again.

## [0.8.0.20260801](https://pypi.org/project/types-hnswlib/0.8.0.20260801/) (2026-08-01)

* Use darwin for stubtest ([#16125](https://github.com/python/typeshed/pull/16125))

    Stubtest crashes on Linux, cf. https://github.com/python/typeshed/issues/16100

## [0.8.0.20260728](https://pypi.org/project/types-hnswlib/0.8.0.20260728/) (2026-07-28)

* Use optional-dependencies for third-party packages ([#16089](https://github.com/python/typeshed/pull/16089))

## 0.8.0.20260518 (2026-05-18)

Upgrade black to 26.5.0 ([#15801](https://github.com/python/typeshed/pull/15801))

## 0.8.0.20260408 (2026-04-08)

Use dashes instead of underscores for METADATA.toml field names ([#15614](https://github.com/python/typeshed/pull/15614))

## 0.8.0.20260402 (2026-04-02)

Rename `requires` to `dependencies` in METADATA files ([#15594](https://github.com/python/typeshed/pull/15594))

## 0.8.0.20250227 (2025-02-27)

[hnswlib] Add ArrayLike annotations and raise Numpy dependency ([#13538](https://github.com/python/typeshed/pull/13538))

## 0.8.0.20250224 (2025-02-24)

Add type annotations for `hnswlib` ([#13529](https://github.com/python/typeshed/pull/13529))

