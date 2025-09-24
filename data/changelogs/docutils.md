## 0.22.2.20250924 (2025-09-24)

[stubsabot] Bump docutils to 0.22.2 ([#14765](https://github.com/python/typeshed/pull/14765))

## 0.22.1.20250923 (2025-09-23)

[docutils] Update to 0.22.1 ([#14737](https://github.com/python/typeshed/pull/14737))

## 0.22.0.20250919 (2025-09-19)

[docutils] Extend applicable types to _ContentModelCategory ([#14719](https://github.com/python/typeshed/pull/14719))

## 0.22.0.20250914 (2025-09-14)

Update mypy to 1.18.1 ([#14699](https://github.com/python/typeshed/pull/14699))

## 0.22.0.20250822 (2025-08-22)

Add __slots__ to third-party packages using stubdefaulter ([#14619](https://github.com/python/typeshed/pull/14619))

Add missing defaults to third-party stubs ([#14617](https://github.com/python/typeshed/pull/14617))

## 0.22.0.20250814 (2025-08-14)

[docutils] Bump to 0.22.* ([#14500](https://github.com/python/typeshed/pull/14500))

## 0.21.0.20250809 (2025-08-09)

[docutils] Add return types for a few docutils table methods (#14493)

Mark stub-only private symbols as `@type_check_only` in third-party stubs (#14545)

## 0.21.0.20250728 (2025-07-28)

[docutils] Add missing stubs (#14438)

Type inline_text in stubs/docutils/docutils/parsers/rst/states.pyi (#14467)

## 0.21.0.20250727 (2025-07-27)

[docutils] Fix type of standalone.Reader.document (#14447)

## 0.21.0.20250722 (2025-07-22)

[docutils] Add missing stubs for `writers` dir (#14223)

## 0.21.0.20250715 (2025-07-15)

[docutils] Add missing stubs for `transforms` dir (#14234)

## 0.21.0.20250710 (2025-07-10)

[docutils] Fix issue with `*_path` params (#14383)

## 0.21.0.20250708 (2025-07-08)

[docutils] Add missing stubs for `readers` dir (#14242)

[docutils] Impove main stubs (#14107)

[docutils] Add `parsers.commonmark_wrapper` (#14243)

## 0.21.0.20250604 (2025-06-04)

Improve `docutils.parsers` (#14191)

## 0.21.0.20250526 (2025-05-26)

Bump flake8-pyi to 25.5.0 (#14140)

## 0.21.0.20250525 (2025-05-25)

Improve `docutils` LanguageImporter's (#14130)

## 0.21.0.20250523 (2025-05-23)

Add `visit_*` and `depart_*` methods to `docutils` visitor classes (#13928)

Improve languages dirs for `docutils` (#14124)

Improve `docutils.utils` (#14122)

Expand docutils.core.Publisher.get_settings types (#14112)

## 0.21.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 0.21.0.20250514 (2025-05-14)

Replace incomplete module markers (#14030)

## 0.21.0.20241128 (2024-11-28)

Generate `docutils.core` and type `publish_parts`'s return type (#13118)

## 0.21.0.20241005 (2024-10-05)

improve type annotations in 'docutils.frontend' (#12735)

Co-authored-by: daniel.eades <daniel.eades@seebyte.com>

## 0.21.0.20241004 (2024-10-04)

add type annotations for 'docutils.parsers.rst.directives.admonitions' (#12396)

add type annotations to docutils.writers (#12420)

Co-authored-by: daniel.eades <daniel.eades@seebyte.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: James Addison <55152140+jayaddison@users.noreply.github.com>

## 0.21.0.20240907 (2024-09-07)

Fix type of `transform` argument of `docutils.nodes.pending.__init__` (#12459)

add type stubs for 'docutils.parsers.rst.directives.references' (#12442)

## 0.21.0.20240724 (2024-07-24)

Add type annotations for 'docutils.writers.latex2e.Babel' (#12394)

Add docutils.utils.roman (#12393)

## 0.21.0.20240711 (2024-07-11)

Docutils: wrong type: SystemMessage vs system_message (#12314)

## 0.21.0.20240710 (2024-07-10)

improve type annotations in 'docutils.parsers.rst.states' (#11545)

## 0.21.0.20240708 (2024-07-08)

remove generic 'context' from 'docutils.parsers.rst.RSTState' (#12291)

## 0.21.0.20240704 (2024-07-04)

Expand docutils.parsters.rst.states (#12226)

## 0.21.0.20240423 (2024-04-23)

Bump docutils to 0.21.* (#11805)

## 0.20.0.20240406 (2024-04-06)

docutils: Correct 'parsers.rst.directives.format_values' (#11719)

## 0.20.0.20240331 (2024-03-31)

Remove bare Incomplete annotations in third-party stubs (#11671)

Add annotations to docutils.parsers.rst.directives.parts (#11667)

## 0.20.0.20240317 (2024-03-17)

improve type annotations in 'docutils.nodes.Element' (#11539)

## 0.20.0.20240316 (2024-03-16)

improve type annotations in 'docutils.utils.Reporter' (#11521)

## 0.20.0.20240315 (2024-03-15)

improve type annotations in 'docutils.parsers.rst.directives' (#11597)

## 0.20.0.20240314 (2024-03-14)

improve type annotations in 'docutils.statemachine' (#11469)

improve type annotations in 'docutils.parsers.rst.directives.misc' (#11524)

Co-authored-by: daniel.eades <daniel.eades@seebyte.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 0.20.0.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 0.20.0.20240310 (2024-03-10)

`docutils`: Use `ClassVar` for `Directive` class variables (#11550)

These are intended to be set as class variables, in subclasses of Directive, rather
than instance variables.

See also:
- https://docutils.sourceforge.io/docs/howto/rst-directives.html#the-directive-class
- https://docutils.sourceforge.io/docs/howto/rst-directives.html#admonitions

improve type annotations in 'docutils.io.Input' (#11540)

## 0.20.0.20240309 (2024-03-09)

improve type annotations in 'docutils.utils' (#11526)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

Improve type annotations in 'docutils.parsers.rst' (#11523)

## 0.20.0.20240308 (2024-03-08)

improve type annotations in 'docutils.parsers.rst.tableparser' (#11530)

Co-authored-by: daniel.eades <daniel.eades@seebyte.com>

## 0.20.0.20240304 (2024-03-04)

improve type annotations in 'docutils.parsers.rst.states.Inliner' (#11473)

## 0.20.0.20240303 (2024-03-03)

improve type annotations in 'docutils.readers.doctree' (#11492)

improve type annotations in 'docutils.parsers.rst.roles' (#11481)

Co-authored-by: daniel.eades <daniel.eades@seebyte.com>

## 0.20.0.20240302 (2024-03-02)

improve type annotations in 'docutils.readers' (#11490)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 0.20.0.20240227 (2024-02-27)

Improve type annotations in 'docutils.node.document' (#11468)

## 0.20.0.20240201 (2024-02-01)

[docutils] Add remaining node classes and functions (#11255)

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Avasam <samuel.06@hotmail.com>

## 0.20.0.20240126 (2024-01-26)

Add docutils.nodes.system_message and .BackLinkable

Add stubs for docutils.nodes.system_message and docutils.nodes.BackLinkable

Ad docutils.nodes.raw and docutils.nodes.Inline (#11312)

## 0.20.0.20240125 (2024-01-25)

Add type stubs for docutils.nodes.literal_block and docutils.nodes.Fi… (#11308)

Add substitution_defs to docutils.nodes.document (#11307)

## 0.20.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 0.20.0.3 (2023-08-16)

Docutils frontend fix (#10569)

## 0.20.0.2 (2023-08-13)

Fill in all missing `upstream_repository` fields (#10571)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 0.20.0.1 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 0.20.0.0 (2023-05-10)

Bump docutils to 0.20.* (#10167)

## 0.19.1.9 (2023-05-03)

[docutils] Add items to docutils.node (#10102)

* Add class paragraph
* Add class TextElement
* Add Element.index(), .remove(), and .insert()

## 0.19.1.8 (2023-04-29)

docutils: Input can take bytearray (#10108)

Part of #9006

docutils: add nodes.General; make Element iterable (#10099)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 0.19.1.7 (2023-03-27)

Add defaults for third-party stubs A-D (#9952)

## 0.19.1.6 (2023-02-22)

Update `Unused` parameters in `stubs/` (#9704)

* Update _Unused TypeAlias

* Update `object | None` params

* Replace unused `object` parameters with `Unused` alias

## 0.19.1.5 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 0.19.1.4 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 0.19.1.3 (2023-02-06)

Use `OSError` instead of `IOError` (#9683)

## 0.19.1.2 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 0.19.1.1 (2022-10-15)

Use `Incomplete` instead of `Any` in `__getattr__` (#8903)

## 0.19.1 (2022-09-11)

Add missing attributes for docutils.io (#8716)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 0.19.0 (2022-07-08)

[stubsabot] Bump docutils to 0.19.* (#8260)

## 0.18.3 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 0.18.2 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 0.18.1 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 0.18.0 (2022-02-28)

docutils: complete nodes.Node & bump version to 0.18.* (#7380)

## 0.17.7 (2022-02-24)

docutils: Add missing dunders to nodes.Element (#7377)

## 0.17.6 (2022-02-21)

Improve docutils stubs (#7256)

## 0.17.5 (2022-02-03)

Use `_typeshed.Self` in `docutils.VersionInfo` and `os.sched_param` (#7117)

## 0.17.4 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 0.17.2 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 0.17.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

