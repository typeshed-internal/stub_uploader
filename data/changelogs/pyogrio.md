## 0.13.0.20260716 (2026-07-16)

Run ty on typeshed stubs in CI ([#16013](https://github.com/python/typeshed/pull/16013))

Add a pinned ty check for the standard-library and third-party stubs across Python 3.10-3.14 and the supported target platforms. The runner honors stdlib/VERSIONS, resolves checked-in stub packages and their external dependencies, and avoids duplicate published stub packages that shadow local sources.

Match pyright's policy for non-actionable override and deprecation diagnostics, add narrowly scoped ignores beside existing checker exceptions, and exclude only the obsolete requests and legacy distutils stubs. Check geopandas, seaborn, and shapely on every target version, with two existing pandas-stubs type-bound exceptions mirrored for ty. Also fix the remaining Windows-only dateutil builtin-name collision discovered by the new check.

Closes #15999.

## 0.13.0.20260712 (2026-07-12)

Add pyogrio stubs ([#16004](https://github.com/python/typeshed/pull/16004))

