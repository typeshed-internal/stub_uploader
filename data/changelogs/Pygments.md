## 2.19.0.20250715 (2025-07-15)

RawTokenFormatter always returns bytes (#14412)

## 2.19.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs (#14063)

## 2.19.0.20250514 (2025-05-14)

Replace incomplete module markers (#14030)

## 2.19.0.20250305 (2025-03-05)

Remove `setuptools/pkg_resources` (#13369)

## 2.19.0.20250219 (2025-02-19)

pygments: Fix return type of pygments.lexers.guess_lexer_for_filename (#13515)

## 2.19.0.20250107 (2025-01-07)

[stubsabot] Bump Pygments to 2.19.* (#13370)

Release: https://pypi.org/pypi/Pygments/2.19.0
Homepage: https://pygments.org
Repository: https://github.com/pygments/pygments
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/Pygments
Changelog: https://github.com/pygments/pygments/blob/master/CHANGES
Diff: https://github.com/pygments/pygments/compare/2.18.0...2.19.0

Stubsabot analysis of the diff between the two releases:
 - 9 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 36 files included in typeshed's stubs have been modified or renamed.
 - Total lines of Python code added: 2960.
 - Total lines of Python code deleted: 694.

## 2.18.0.20240506 (2024-05-06)

[stubsabot] Bump Pygments to 2.18.* (#11861)

Release: https://pypi.org/pypi/Pygments/2.18.0
Homepage: https://pygments.org
Repository: https://github.com/pygments/pygments
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/Pygments
Changelog: https://github.com/pygments/pygments/blob/master/CHANGES
Diff: https://github.com/pygments/pygments/compare/2.17.2...2.18.0

Stubsabot analysis of the diff between the two releases:
 - 5 public Python files have been added: `pygments/lexers/mojo.py`, `pygments/lexers/soong.py`, `pygments/lexers/tact.py`, `pygments/lexers/typst.py`, `pygments/styles/coffee.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 36 files included in typeshed's stubs have been modified or renamed.
 - Total lines of Python code added: 4858.
 - Total lines of Python code deleted: 2467.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2.17.0.20240310 (2024-03-10)

`docutils`: Use `ClassVar` for `Directive` class variables (#11550)

These are intended to be set as class variables, in subclasses of Directive, rather
than instance variables.

See also:
- https://docutils.sourceforge.io/docs/howto/rst-directives.html#the-directive-class
- https://docutils.sourceforge.io/docs/howto/rst-directives.html#admonitions

## 2.17.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 2.17.0.0 (2023-11-24)

Bump pygments to 2.17 (#11051)

* Add some previously missing lexers.
* Improve lexer type annotations.

## 2.16.0.1 (2023-11-10)

Add types for `pygments.lex`. (#10998)

## 2.16.0.0 (2023-08-07)

[stubsabot] Bump Pygments to 2.16.* (#10536)

Release: https://pypi.org/pypi/Pygments/2.16.1
Homepage: https://pygments.org
Repository: https://github.com/pygments/pygments
Changelog: https://github.com/pygments/pygments/blob/master/CHANGES
Diff: https://github.com/pygments/pygments/compare/2.15.1...2.16.1

Stubsabot analysis of the diff between the two releases:
 - 12 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 6 files included in typeshed's stubs have been modified or renamed: `pygments/__init__.py`, `pygments/formatters/img.py`, `pygments/lexer.py`, `pygments/sphinxext.py`, `pygments/styles/__init__.py`, `pygments/token.py`.
 - Total lines of Python code added: 2942.
 - Total lines of Python code deleted: 477.

Co-authored-by: stubsabot <>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.15.0.2 (2023-07-20)

Add an upstream_repository field to METADATA.toml (#10487)

Closes: #10478

## 2.15.0.1 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 2.15.0.0 (2023-04-11)

[stubsabot] Bump Pygments to 2.15.* (#10030)

Release: https://pypi.org/pypi/Pygments/2.15.0
Homepage: https://pygments.org
Changelog: https://github.com/pygments/pygments/blob/master/CHANGES
Diff: https://github.com/pygments/pygments/compare/2.14.0...2.15.0

Stubsabot analysis of the diff between the two releases:
 - 3 public Python files have been added: `pygments/lexers/carbon.py`, `pygments/lexers/dax.py`, `pygments/lexers/wgsl.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 28 files included in typeshed's stubs have been modified or renamed.
 - Total lines of Python code added: 2582.
 - Total lines of Python code deleted: 502.

## 2.14.0.7 (2023-03-27)

Add default values for third-party stubs beginning with 'P' (#9957)

## 2.14.0.6 (2023-03-08)

Pygments: fix get_style_by_name return type (#9803)

## 2.14.0.5 (2023-02-21)

Integrate requirements-stubtest.txt into METADATA.toml (#9778)

## 2.14.0.4 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 2.14.0.3 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 2.14.0.2 (2023-02-09)

Use `_typeshed.FileDescriptorOrPath` in stubs (#9695)

## 2.14.0.1 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 2.14.0.0 (2023-01-02)

[stubsabot] Bump Pygments to 2.14.* (#9440)

Release: https://pypi.org/pypi/Pygments/2.14.0
Homepage: https://pygments.org/
Changelog: https://github.com/pygments/pygments/blob/master/CHANGES
Diff: https://github.com/pygments/pygments/compare/2.13.0...2.14.0

Stubsabot analysis of the diff between the two releases:
 - 11 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 7 files included in typeshed's stubs have been modified or renamed: `pygments/__init__.py`, `pygments/formatters/__init__.py`, `pygments/formatters/html.py`, `pygments/formatters/irc.py`, `pygments/lexer.py`, `pygments/lexers/__init__.py`, `pygments/sphinxext.py`.
 - Total lines of Python code added: 3094.
 - Total lines of Python code deleted: 1387.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2.13.1.1 (2022-10-15)

Use `Incomplete` instead of `Any` in `__getattr__` (#8903)

## 2.13.1 (2022-09-21)

`pygments.lexers.guess_lexer_for_filename` cannot return `None` (#8777)

## 2.13.0 (2022-08-19)

[stubsabot] Bump Pygments to 2.13.* (#8561)

Co-authored-by: stubsabot <>

## 2.12.1 (2022-07-05)

Pygments: add pygments.__version__ (#8241)

Signed-off-by: Anders Kaseorg <andersk@mit.edu>

## 2.12.0 (2022-06-18)

[stubsabot] Bump Pygments to 2.12.* (#8093)

Co-authored-by: hauntsaninja <>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.9.19 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.9.18 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 2.9.17 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 2.9.16 (2022-02-07)

Improve a bunch of `__(deep)copy__` methods (#7148)

## 2.9.15 (2022-01-22)

fix incorrect tuple[T] (#6996)

Found from PyCQA/flake8-pyi#135.

## 2.9.14 (2022-01-15)

pygments: delete _TokenType.__init__ (#6918)

## 2.9.13 (2022-01-08)

Pygments: make Formatter generic and improve format/highlight (#6819)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.9.12 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 2.9.10 (2021-12-28)

pygments: remove outdated TODOs (#6725)

## 2.9.9 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.9.8 (2021-12-27)

Always alias `collections.abc.Set` (#6712)

## 2.9.7 (2021-12-26)

Annotate return type of pygments.plugin.iter_entry_points (#6697)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

pygments: Annotate several generator functions (#6695)

## 2.9.6 (2021-12-21)

pygments.formatters.get_all_formatters yields Formatters (#6636)

## 2.9.5 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 2.9.4 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 2.9.3 (2021-10-12)

Add star to all non-0.1 versions (#6146)

