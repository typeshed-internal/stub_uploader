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

