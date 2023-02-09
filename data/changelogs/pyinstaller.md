## 5.7.0.6 (2023-02-09)

Use `_typeshed.FileDescriptorOrPath` in stubs (#9695)

## 5.7.0.5 (2023-02-02)

Manual changes of `Any` union to `Incomplete` in stubs folder (#9566)

- ClassVar[Any | None]
- Missed previous changes due to alias
- Manual review of leftover Any unions (`| Any` and `Any |`)

## 5.7.0.4 (2023-02-01)

Add defaults for params and constants in pyinstaller (#9640)

## 5.7.0.3 (2023-01-25)

Fix some stubtest complaints before they happen (#9585)

Add missing objects to various stubs

## 5.7.0.2 (2023-01-14)

Update various comments now non-types dependencies are allowed (#9527)

## 5.7.0.1 (2023-01-11)

types-pyinstaller: no longer subclass "Any" (#9495)

## 5.7.0.0 (2022-12-08)

Bump pyinstaller to 5.7.* (#9343)

## 5.6.0.4 (2022-11-16)

Always use `bool` and `Literal` for Python compat code (#9213)

## 5.6.0.3 (2022-11-07)

`PyInstaller`: Fix `DeprecationWarning` when parsing the stub using `ast.parse()` (#9112)

```python
>>> import ast, warnings
>>> warnings.filterwarnings("always")
>>> with open("typeshed/stubs/pyinstaller/pyi_splash/__init__.pyi", encoding="utf-8") as file:
...     source = file.read()
...
>>> ast.parse(source)
<unknown>:11: DeprecationWarning: invalid escape sequence '\u'
<ast.Module object at 0x0000027EAF6D3AF0>
```

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 5.6.0.2 (2022-11-03)

Update pyright to 1.1.278 (#9077)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 5.6.0.1 (2022-11-03)

importlib: improve bytes handling (#9070)

## 5.6.0.0 (2022-10-25)

Bump pyinstaller to 5.6.* (#8981)

## 5.5.0.0 (2022-10-10)

Bump PyInstaller-stubs to 5.5 (#8874)

## 5.4.2 (2022-09-27)

Bump mypy to 0.981 (#8796)

## 5.4.1 (2022-09-22)

Add reportMissingParameterType to `pyrightconfig.stricter.json` (#8770)

Pyinstaller: use `StrPath` over `StrOrBytesPath` (#8780)

Fix incorrect StrOrBytesPath in PyInstaller stubs
Change StrOrBytesPath to StrPath when exclusively used with strings.

## 5.4.0 (2022-09-15)

Add stubs for `PyInstaller` (public API only) (#8702)

