## 1.5.8.2 (2022-11-07)

Mark typed_ast as completed (#9121)

## 1.5.8.1 (2022-10-28)

typed-ast: fix get_docstring, allow buffer (#9019)

## 1.5.8 (2022-08-29)

`typed_ast.ast3`: `arguments.kw_defaults` should be `list[expr | None]` (#8645)

```python
>>> from typed_ast import ast3
>>> print(ast3.dump(ast3.parse('def foo(*, arg: int) -> None: ...')))
Module(body=[FunctionDef(name='foo', args=arguments(args=[], vararg=None, kwonlyargs=[arg(arg='arg', annotation=Name(id='int', ctx=Load()), type_comment=None)], kw_defaults=[None], kwarg=None, defaults=[]), body=[Expr(value=Ellipsis())], decorator_list=[], returns=NameConstant(value=None), type_comment=None)], type_ignores=[])
```

This bug was discovered in https://github.com/python/mypy/pull/13547

## 1.5.7 (2022-07-19)

Third-party stubs: enforce CamelCase for type alias names (#8256)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.5.6 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 1.5.5 (2022-05-21)

Simplify and correct many numeric unions (#7906)

Unblocks PyCQA/flake8-pyi#222

## 1.5.4 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 1.5.3 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 1.5.1 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 1.5.0 (2021-11-12)

Bump typed-ast version, recommend Python 3.8 for tests (#6278)

## 1.4.5 (2021-10-12)

Add star to all non-0.1 versions (#6146)

