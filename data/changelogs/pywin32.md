## 305.0.0.6 (2023-01-13)

Allowlist-only fixes for stubtest on Windows (#9522)

## 305.0.0.5 (2022-12-28)

Check for unused `pyright: ignore` and differentiate from mypy ignores (#9397)

## 305.0.0.4 (2022-12-07)

3rd-party stubtest: run on Python 3.10 (#9342)

## 305.0.0.3 (2022-12-06)

More pywin32 stub completion (#9308)

Completed based on usage of the following libraries in mypy_primer:
- apprise
- comtypes
As well as some of the most popular libraries that use both pywin32 and mypy (all over 1k stars on github):
- certbot
- anki
- flexget
- monkey
- twisted
- salt

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 305.0.0.2 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 305.0.0.1 (2022-11-11)

Add the ability to run third-party stubtest on Windows or MacOS when needed (#8923)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 305.0.0.0 (2022-11-10)

Update pywin32 to 305 (#9153)

## 304.0.0.6 (2022-11-10)

Update pywin32 to mypy 0.990 (#9124)

## 304.0.0.5 (2022-11-09)

Annotate known magic-method return types (#9131)

## 304.0.0.4 (2022-11-05)

pywin32: Improve some types (#9089)

## 304.0.0.3 (2022-10-31)

pywin32 stubs update (#9040)

boolean methods
win32gui_struct
MonitorFromRect, FindWindow, FindWindowEx, GetWindowPlacement, GetMenuItemRect

## 304.0.0.2 (2022-10-19)

pywin32: Remove IID that doesn't exist at runtime (#8930)

Remove IID that doesn't exist at runtime

## 304.0.0.1 (2022-10-07)

pywin32: Complete modules using stubgen & stubtest (#8866)

Complete modules using stubgen & stubtest

## 304.0.0.0 (2022-10-03)

Add `pywin32` type stubs from microsoft/python-type-stubs and mhammond/pywin32  (#8825)

