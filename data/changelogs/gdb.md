## 12.1.4 (2022-09-24)

gdb: add missing automatic imports (#8788)

When GDB has just started, several `gdb` submodules are automatically
loaded, so user code does not have to manually import them (for instance
`import gdb.events`). Reflect that in `gdb` stubs.

## 12.1.3 (2022-07-07)

Fix various `TypeAlias` issues (#8248)

## 12.1.2 (2022-06-23)

Various fixes in `gdb` (#8144)

* gdb.events.BreakpointEvent: fix various typos

* gdb.printing: remove GenPrinterFunction

This was meant to be a private type alias, but it is unused and a
duplicate of the better named gdb._PrettyPrinterLookupFunction.

## 12.1.1 (2022-06-19)

stubtest: use separate table in METADATA.toml (#8096)

## 12.1.0 (2022-06-15)

Add stubs for "gdb" (#8013)

This commit adds type stubs for the "gdb" package, the Python API to
extend GDB (https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html).

