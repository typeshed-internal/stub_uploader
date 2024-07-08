## 1.15.0.20240708 (2024-07-08)

Pin pygit2 to 1.15.0 (#12293)

Fixes #12292

## 1.15.0.20240520 (2024-05-20)

Bump pygit2 to 1.15 and fix enums (#11983)

## 1.14.0.20240317 (2024-03-17)

pygit2: Workaround python/mypy#16972 (#11584)

To fix the signatures of `clone_repository` and `init_repository` as
seen by type checkers.

## 1.14.0.20240313 (2024-03-13)

pygit2: Add missing Repository fields (#11579)

Add stubs for pygit2 (#11374)

The upstream library is very tricky to type (likely requires nontrivial
refactoring), and only contains partial type information, but stubs are
a lot easier because only the public signatures are involved this way,
so I plan to first make the library usable in typed projects by making
stubs available here, then gradually work my way upstream.

The stubs are auto-generated then completed with fully manual inspection
of every Python source file. The `_pygit2.pyi` comes from upstream and
is mostly untouched except for required style changes, the signature of
`options()`, and `FilterSource` which is missing from upstream.

