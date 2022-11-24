## 0.5.10.3 (2022-11-24)

Add support for Homebrew and Chocolatey (#9187)

## 0.5.10.2 (2022-11-16)

Add missing symbols in `JACK-Client` stubs (#9205)

`ignore_missing_stub = false` and completed on Windows & MacOS

## 0.5.10.1 (2022-11-11)

Add the ability to run third-party stubtest on Windows or MacOS when needed (#8923)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 0.5.10 (2022-06-26)

`JACK-Client`: audit callback annotations (#8177)

The returned values from these functions are all ignored at runtime.

## 0.5.9 (2022-06-19)

stubtest: use separate table in METADATA.toml (#8096)

## 0.5.8 (2022-04-28)

jack: Fix MidiPort properties (#7730)

Fixes #7729

https://github.com/spatialaudio/jackclient-python/blob/26b648a36143b1e3db6e6fc827ca927b0c93cbec/src/jack.py#L1950

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 0.5.7 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 0.5.6 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 0.5.5 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 0.5.4 (2022-01-22)

Add missing context manager stub for JACK Client (#6982)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 0.5.2 (2021-12-29)

Enable stubtest for jack (#6727)

## 0.5.1 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 0.5.0 (2021-10-12)

Update remaining versions for third-party stubs (#6094)

Also remove the python2 markers of packages that don't list Python 2
as supported in the latest version.

Don't special case version '0.1'

Co-authored-by: Akuli <akuviljanen17@gmail.com>

