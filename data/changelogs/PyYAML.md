## 6.0.12.2 (2022-11-09)

PyYAML: Permit `width: float` for pure-Python `dump(...)` (#8973)

* PyYAML: Permit `width: float` for pure-Python `dump(...)`

To prevent `PyYAML` from wrapping *any* lines, it's possible to pass
`width=float("inf")`, but the current type hints don't like that.  This
works at runtime:

    >>> s = yaml.dump({"foo": "bar" * 1000}, width=float("inf"))
    >>> print(s)
    foo: barbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbar...

but `mypy` says

    floatwidth.py:2: error: No overload variant of "dump" matches argument types "Dict[str, str]", "float"
    floatwidth.py:2: note: Possible overload variants:
    floatwidth.py:2: note:     def dump(data: Any, stream: _WriteStream[Any], Dumper: Any = ..., *, default_style: Optional[str] = ..., default_flow_style: Optional[bool] = ..., canonical: Optional[bool] = ..., indent: Optional[int] = ..., width: Optional[int] = ..., allow_unicode: Optional[bool] = ..., line_break: Optional[str] = ..., encoding: Optional[str] = ..., explicit_start: Optional[bool] = ..., explicit_end: Optional[bool] = ..., version: Optional[Tuple[int, int]] = ..., tags: Optional[Mapping[str, str]] = ..., sort_keys: bool = ...) -> None
    floatwidth.py:2: note:     def dump(data: Any, stream: None = ..., Dumper: Any = ..., *, default_style: Optional[str] = ..., default_flow_style: Optional[bool] = ..., canonical: Optional[bool] = ..., indent: Optional[int] = ..., width: Optional[int] = ..., allow_unicode: Optional[bool] = ..., line_break: Optional[str] = ..., encoding: Optional[str] = ..., explicit_start: Optional[bool] = ..., explicit_end: Optional[bool] = ..., version: Optional[Tuple[int, int]] = ..., tags: Optional[Mapping[str, str]] = ..., sort_keys: bool = ...) -> Any
    Found 1 error in 1 file (checked 1 source file)

Poking through the `PyYAML` source, it looks the `width` parameter
could probably be anything "comparable", as it's only compared via
the `<` operator[1].

For the LibYAML implementation, however, we have to use `int`s:

    >>> stream = StringIO()
    >>> dumper = yaml.CDumper(stream, width=float("inf"))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python3/dist-packages/yaml/cyaml.py", line 81, in __init__
        version=version, tags=tags)
      File "ext/_yaml.pyx", line 973, in _yaml.CEmitter.__init__ (ext/_yaml.c:14797)
    OverflowError: cannot convert float infinity to integer

## 6.0.12.1 (2022-10-26)

Add a couple of missing type hints in pyyaml.constructor (#8965)

## 6.0.12 (2022-09-27)

Bump mypy to 0.981 (#8796)

## 6.0.11 (2022-07-24)

`PyYaml`’s Serializer: annotate `open`, `close`, `serialize` (#8383)

As seen here:
https://github.com/yaml/pyyaml/blob/master/lib/yaml/serializer.py#L27-L41

Neither `open` nor `close` methods return, so `None` added as the return type.

Finally, serialize accepts a Node and does not return as seen here:
https://github.com/yaml/pyyaml/blob/master/lib/yaml/serializer.py#L46-L58

## 6.0.10 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 6.0.9 (2022-06-25)

PyYAML: check missing defs (#8159)

## 6.0.8 (2022-06-01)

PyYAML: Add types to `add_constructor` (#7989)

## 6.0.7 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 6.0.6 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

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

