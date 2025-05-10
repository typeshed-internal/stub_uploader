## 1.0.1.20250510 (2025-05-10)

[geopandas] Fix CI tests in some circumstances (#13978)

Add "libproj-dev" and "proj-bin" to apt_dependencies.
These packages are necessary to build the pyproj
dependency if a pre-built wheel is not available.

## 1.0.1.20250404 (2025-04-04)

Enable Ruff flake8-todos (TD) (#13748)

## 1.0.1.20250310 (2025-03-10)

Fix override issue in GeoDataFrame.astype return type (#13606)

## 1.0.1.20250304 (2025-03-04)

Drop flake8-noqa and remove workarounds to work with Ruff (#13571)

## 1.0.1.20250120 (2025-01-20)

Add geopandas stubs (#12990)

