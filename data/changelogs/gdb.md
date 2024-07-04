## 12.1.4.20240704 (2024-07-04)

Add `global_context` keyword to `gdb.parse_and_eval` in GDB stub (#12269)

## 12.1.4.20240408 (2024-04-08)

[gdb] Add __r{add,sub,mul,truediv,mod}__ for gdb.Value (#11707)

## 12.1.4.20240401 (2024-04-01)

Update GDB stubs to 12.1 (#11665)

## 12.1.4.20240327 (2024-03-27)

Run gdb stubtests (#11644)

The gdb package is only available inside gdb and cannot be installed externally through e.g. pip.
Run the stubtest inside gdb.

## 12.1.4.20240322 (2024-03-22)

Overload gdb.execute return type (#11638)

## 12.1.4.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 12.1.4.20240305 (2024-03-05)

Add VERSION to gdb stubs (#11529)

## 12.1.4.20240113 (2024-01-13)

Fix inconsistencies in gdb stubs (#11227)

See #11225

## 12.1.4.5 (2023-08-13)

Fill in all missing `upstream_repository` fields (#10571)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 12.1.4.4 (2023-03-14)

Fix typos in `extra_description` fields (#9883)

## 12.1.4.3 (2023-02-01)

Bump black to 23.1.0 (#9647)

## 12.1.4.2 (2023-01-05)

`gdb-stubs` fixes (#9439)

* fix: Union subprinters with `None`

See https://github.com/bminor/binutils-gdb/blob/a4418a9c6f99fd31c51698b1f6a6f8dbc1b81b6f/gdb/python/lib/gdb/printing.py#L52-L55

* fix: Allow callables as argument to `printer`

See https://github.com/bminor/binutils-gdb/blob/a4418a9c6f99fd31c51698b1f6a6f8dbc1b81b6f/gdb/python/lib/gdb/printing.py#L77 and the description of "function / old way" in the body of `register_pretty_printer`.

The new union's signature is equivalent to `gdb.printing.PrettyPrinter(...).__call__`.

* fix: make `gdb.Block` iterable over `gdb.Symbol`

See https://sourceware.org/gdb/onlinedocs/gdb/Blocks-In-Python.html#Blocks-In-Python:

> A gdb.Block is iterable. The iterator returns the symbols (see [Symbols In Python](https://sourceware.org/gdb/onlinedocs/gdb/Symbols-In-Python.html#Symbols-In-Python)) local to the block.

Implementation of `gdb.BlockIterator` is given in https://github.com/bminor/binutils-gdb/blob/gdb-12-branch/gdb/python/py-block.c. As with many of the other classes, `BlockIterator` is actually imported from the built-in `_gdb` module (https://github.com/bminor/binutils-gdb/blob/a4418a9c6f99fd31c51698b1f6a6f8dbc1b81b6f/gdb/python/lib/gdb/__init__.py#L28).

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 12.1.4.1 (2022-12-28)

Add type stubs for gdb.Value comparison operators (#9411)

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

