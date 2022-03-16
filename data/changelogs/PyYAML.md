## 6.0.5 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 6.0.4 (2022-01-31)

Replace IO with protocols (#7092)

## 6.0.3 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 6.0.1 (2021-11-12)

Add more type hints for pyyaml (#6265)

## 6.0.0 (2021-10-22)

Upgrade PyYAML to version 6 (#6183)

* Fix load_all() argument
* Remove Python 2 remnants
  + Replace Text with str
  + Replace alias "_Str" with str
  + Import from collections.abc and re where applicable
  + Remove Python 2 branches
* Fix PyYaml allowlist entries
  + Add yaml._yaml and move CParser and CEmitter there.
  + Add missing functions, classes, and arguments.
* Use relative imports in some modules.
* Add __all__ to yaml.cyaml.
* Remove unnecessary noqa markers.

## 5.4.12 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 5.4.11 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 5.4.10 (2021-09-01)

Delete yaml.CDangerLoader and yaml.CDangerDumper (#5990)

These no longer exist in PyYAML 4.2.

## 5.4.9 (2021-09-01)

Add C{Full,Unsafe}Loader and UnsafeConstructor (#5988)

