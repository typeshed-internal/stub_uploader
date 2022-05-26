## 1.26.15 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 1.26.14 (2022-04-29)

Delete python 2 branches from third-party stubs (#7741)

Since #7703, we no longer have third-party stubs that support Python 2, so code like `if sys.version_info >= (3, 0)` can be simplified.

## 1.26.13 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 1.26.12 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 1.26.11 (2022-03-13)

urllib3: stubs are not Python 2 compatible (#7480)

They use http.client, which is Python 3-only. Another catch from #7478.

## 1.26.10 (2022-02-28)

Add DEFAULT_CIPHERS to urllib3.util.ssl_ (#7399)

## 1.26.9 (2022-02-03)

Improve `__enter__` & constructor methods (#7114)

## 1.26.8 (2022-01-31)

Upgrade black version (#7089)

## 1.26.7 (2022-01-13)

urllib3: allow allowed_methods to be False (#6909)

## 1.26.5 (2022-01-12)

Update types in urllib3.util.retry (#6892)

## 1.26.4 (2022-01-11)

urllib3: add "__version__" (#6890)

Co-authored-by: Shantanu <12621235+hauntsaninja@users.noreply.github.com>

## 1.26.3 (2022-01-10)

Fix urllib3.util.Retry.sleep type (#6883)

## 1.26.2 (2022-01-09)

Annotate urllib3.exceptions (#6865)

Annotate urllib3.response (#6871)

## 1.26.1 (2022-01-08)

Use types-urllib3 for requests (#6859)

Add urllib3 stubs (#6858)

