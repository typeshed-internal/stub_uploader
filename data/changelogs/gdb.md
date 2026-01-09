## 16.3.0.20260109 (2026-01-09)

Update mypy to 1.19.1 ([#15235](https://github.com/python/typeshed/pull/15235))

Skip gdb stubtest for now

## 16.3.0.20250920 (2025-09-20)

[gdb] Update ThreadExitedEvent parent class for 17.0 ([#14729](https://github.com/python/typeshed/pull/14729)) ([#14744](https://github.com/python/typeshed/pull/14744))

Even though the parent thread for `ThreadExitedEvent` won't change from
`Event` to `ThreadEvent` until 17.0 is released, this actually makes
type checking work better in practice for all released versions that
support `ThreadExitedEvent` because at run time `ThreadExitedEvent` has
the lone attribute, `inferior_thread`, that it would have inherited from
`ThreadEvent`.

## 16.3.0.20250915 (2025-09-15)

Add `@disjoint_base` decorator to the third-party stubs ([#14716](https://github.com/python/typeshed/pull/14716))

## 16.3.0.20250812 (2025-08-12)

Update GDB stubs to 16.3 ([#13923](https://github.com/python/typeshed/pull/13923))

## 15.0.0.20250809 (2025-08-09)

Fix dunder-method positional-only parameter discrepancies in third-party stubs (#14529)

Mark stub-only private symbols as `@type_check_only` in third-party stubs (#14545)

## 15.0.0.20250801 (2025-08-01)

Split `tool.stubtest.platforms` metadata key (#13746)

Co-authored-by: Avasam <samuel.06@hotmail.com>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 15.0.0.20250713 (2025-07-13)

[gdb] Complete stubs for `gdb.dap` (#14269)

## 15.0.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 15.0.0.20250514 (2025-05-14)

Replace incomplete module markers (#14030)

## 15.0.0.20250321 (2025-03-21)

[gdb] Remove unused import (#13682)

Unblocks #13680

## 15.0.0.20250308 (2025-03-08)

Remove LD_LIBRARY_PATH before running gdb (#13594)

Suggestion by @peace-maker

## 15.0.0.20250306 (2025-03-06)

Update tools versions in `stubtest` workflow (#13582)

## 15.0.0.20241204 (2024-12-04)

Fixes for `gdb` stubs (#13169)

* gdb: Clarify a comment
* gdb: Fix gdb.unwinder.Unwinder.__call__ argument. It takes a gdb.PendingFrame, not a gdb.Frame.
* gdb: Unwinders may implement a proto without subclassing gdb.unwinder.Unwinder
* gdb: Fix Breakpoint.__init__

 1. `line` should be `int|str`, not just `int` (IDK what a string means,
    but that it can be a string is clear if you read
    py-breakpoint.c:bppy_init().
 2. `type` argument should be able to be passed to the "location" form,
    not just the "spec" form, even if
    https://sourceware.org/gdb/current/onlinedocs/gdb.html/Breakpoints-In-Python.html
    neglects to mention it (don't worry, I'll be submitting a patch to fix
    the doc soon).
 3. Fix the positional argument order (based on GDB's sources, it isn't
    really documented)
 4. Use more `@overloads` to enforce that at least 1 of `function`,
    `label`, or `line` are given in the location form.

## 15.0.0.20241015 (2024-10-15)

Bump gdb to 15.0.* (#12804)

Closes: #12777

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

