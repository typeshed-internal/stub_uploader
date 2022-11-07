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

