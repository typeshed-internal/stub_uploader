## 0.4.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 0.4.0.3 (2023-08-13)

Fill in all missing `upstream_repository` fields (#10571)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 0.4.0.2 (2023-06-29)

Stricter pyright checks for `inifile` (#10382)

## 0.4.0.1 (2023-06-08)

inifile: add missing attributes (#10273)

And make many attributes read-only. The primary entry point to this module in `IniFile` (or its subclass
`AppIniFile`). Since the config file is read (from `filename`) and
parsed (using the `dialect`) in the `IniFile` constructor, modifying
attributes like `IniFile.filename` or `IniFile.dialect` after
construction is likely to cause problems.

## 0.4.0.0 (2023-06-07)

Add stubs for `inifile` (#10270)

