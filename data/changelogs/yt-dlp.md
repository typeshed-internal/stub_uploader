## 2026.3.17.20260716 (2026-07-16)

Run ty on typeshed stubs in CI ([#16013](https://github.com/python/typeshed/pull/16013))

Add a pinned ty check for the standard-library and third-party stubs across Python 3.10-3.14 and the supported target platforms. The runner honors stdlib/VERSIONS, resolves checked-in stub packages and their external dependencies, and avoids duplicate published stub packages that shadow local sources.

Match pyright's policy for non-actionable override and deprecation diagnostics, add narrowly scoped ignores beside existing checker exceptions, and exclude only the obsolete requests and legacy distutils stubs. Check geopandas, seaborn, and shapely on every target version, with two existing pandas-stubs type-bound exceptions mirrored for ty. Also fix the remaining Windows-only dateutil builtin-name collision discovered by the new check.

Closes #15999.

## 2026.3.17.20260605 (2026-06-05)

[yt-dlp] Add typing for postprocessor_hooks ([#15810](https://github.com/python/typeshed/pull/15810))

## 2026.3.17.20260518 (2026-05-18)

Upgrade black to 26.5.0 ([#15801](https://github.com/python/typeshed/pull/15801))

## 2026.3.17.20260510 (2026-05-10)

[yt-dlp] Make _Params["paths"] a dict[str, str] ([#14998](https://github.com/python/typeshed/pull/14998))

`paths` accepts a dict of output paths (keys: 'home', 'temp', and OUTTMPL_TYPES keys).
Typing it as `dict[str, str] | None` matches runtime behavior and avoids false positives
when passing a dict to YoutubeDL params.

---------

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2026.3.17.20260508 (2026-05-08)

Import some items from typing instead of typing_extensions ([#15711](https://github.com/python/typeshed/pull/15711))

Part of #13782

## 2026.3.17.20260503 (2026-05-03)

[http.cookies] Modernize ([#15266](https://github.com/python/typeshed/pull/15266))

* Inline `_DataType` type alias.
* Replace `Mapping` with protocols.
* Replace `list` in argument positions with protocols.

[yt-dlp] Fix some arg types for DateRange ([#15678](https://github.com/python/typeshed/pull/15678))

## 2026.3.17.20260408 (2026-04-08)

Use dashes instead of underscores for METADATA.toml field names ([#15614](https://github.com/python/typeshed/pull/15614))

## 2026.3.17.20260402 (2026-04-02)

Rename `requires` to `dependencies` in METADATA files ([#15594](https://github.com/python/typeshed/pull/15594))

Update mypy to 1.20.0 ([#15588](https://github.com/python/typeshed/pull/15588))

## 2026.3.17.20260318 (2026-03-18)

[stubsabot] Bump yt-dlp to 2026.3.17 ([#15522](https://github.com/python/typeshed/pull/15522))

## 2026.3.13.20260314 (2026-03-14)

[stubsabot] Bump yt-dlp to 2026.3.13 ([#15509](https://github.com/python/typeshed/pull/15509))

## 2026.3.3.20260304 (2026-03-04)

[stubsabot] Bump yt-dlp to 2026.3.3 ([#15484](https://github.com/python/typeshed/pull/15484))

## 2026.2.21.20260223 (2026-02-23)

[yt-dlp] Update to 2026.2.21 ([#15449](https://github.com/python/typeshed/pull/15449))

## 2026.2.4.20260206 (2026-02-06)

[stubsabot] Bump yt-dlp to 2026.2.4 ([#15373](https://github.com/python/typeshed/pull/15373))

Release: https://pypi.org/pypi/yt-dlp/2026.2.4
Repository: https://github.com/yt-dlp/yt-dlp
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/yt-dlp
Diff: https://github.com/yt-dlp/yt-dlp/compare/2026.01.31...2026.02.04

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 1 file included in typeshed's stubs has been modified or renamed: `yt_dlp/version.py`.
 - Total lines of Python code added: 25.
 - Total lines of Python code deleted: 4.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2026.1.31.20260202 (2026-02-02)

[yt-dlp] Update to 2026.01.31 ([#15354](https://github.com/python/typeshed/pull/15354))

## 2026.1.29.20260131 (2026-01-31)

[yt-dlp] Update to 2026.01.29 ([#15343](https://github.com/python/typeshed/pull/15343))

## 2025.12.8.20260130 (2026-01-30)

[yt-dlp] Fix YoutubeDL.YoutubeDL.download return value ([#15336](https://github.com/python/typeshed/pull/15336))

## 2025.12.8.20260116 (2026-01-16)

[yt-dlp] Make _Params["playlist_items"] a str ([#15287](https://github.com/python/typeshed/pull/15287))

## 2025.12.8.20251210 (2025-12-10)

[yt-dlp] Update to 2025.12.08 ([#15122](https://github.com/python/typeshed/pull/15122))

## 2025.11.12.20251115 (2025-11-15)

[yt-dlp] Update to 2025.11.12 ([#15025](https://github.com/python/typeshed/pull/15025))

## 2025.10.22.20251031 (2025-10-31)

[yt-dlp] Update to 2025.10.22 ([#14924](https://github.com/python/typeshed/pull/14924))

## 2025.9.26.20251009 (2025-10-09)

[yt-dlp] Check common code in extractor subpackage with stubtest ([#14682](https://github.com/python/typeshed/pull/14682))

## 2025.9.26.20250928 (2025-09-28)

[stubsabot] Bump yt-dlp to 2025.9.26 ([#14798](https://github.com/python/typeshed/pull/14798))

## 2025.9.23.20250927 (2025-09-27)

[yt-dlp] Use Final ([#14788](https://github.com/python/typeshed/pull/14788))

## 2025.9.23.20250925 (2025-09-25)

[yt-dlp] Update to 2025.9.23 ([#14776](https://github.com/python/typeshed/pull/14776))

## 2025.9.5.20250907 (2025-09-07)

[yt-dlp] Update to 2025.9.5 ([#14681](https://github.com/python/typeshed/pull/14681))

## 2025.8.27.20250829 (2025-08-29)

[stubsabot] Bump yt-dlp to 2025.8.27 ([#14654](https://github.com/python/typeshed/pull/14654))

## 2025.8.22.20250824 (2025-08-24)

[stubsabot] Bump yt-dlp to 2025.8.22 ([#14629](https://github.com/python/typeshed/pull/14629))

Release: https://pypi.org/pypi/yt-dlp/2025.8.22
Repository: https://github.com/yt-dlp/yt-dlp
Typeshed stubs: https://github.com/python/typeshed/tree/main/stubs/yt-dlp
Diff: https://github.com/yt-dlp/yt-dlp/compare/2025.08.20...2025.08.22

Stubsabot analysis of the diff between the two releases:
 - 0 public Python files have been added.
 - 0 files included in typeshed's stubs have been deleted.
 - 2 files included in typeshed's stubs have been modified or renamed: `yt_dlp/cookies.py`, `yt_dlp/version.py`.
 - Total lines of Python code added: 188.
 - Total lines of Python code deleted: 179.

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2025.8.20.20250822 (2025-08-22)

Add missing defaults to third-party stubs ([#14617](https://github.com/python/typeshed/pull/14617))

[yt-dlp] Update to 2025.8.20 ([#14609](https://github.com/python/typeshed/pull/14609))

## 2025.8.11.20250813 (2025-08-13)

[yt-dlp] Update to 2025.8.11 ([#14564](https://github.com/python/typeshed/pull/14564))

## 2025.7.21.20250728 (2025-07-28)

Fully annotate `yt-dlp` ([#14481](https://github.com/python/typeshed/pull/14481))

## 2025.7.21.20250727 (2025-07-27)

Add yt-dlp stubs ([#14216](https://github.com/python/typeshed/pull/14216))

