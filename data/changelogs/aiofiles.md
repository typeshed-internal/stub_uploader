## 22.1.0.7 (2023-02-09)

Use `_typeshed.FileDescriptorOrPath` in stubs (#9695)

## 22.1.0.6 (2023-01-18)

Improve pre-commit config (#9563)

- Add a few more hooks. These are all very fast, and I've found them useful in other projects:
  - Autofixes:
    - `trailing-whitespace`: fixes trailing whitespace
    - `requirements-txt-fixer`: alphabetises items in `requirements.txt` files
    - `end-of-file-fixer`: makes sure every file ends with a single newline character
    - `mixed-line-ending`: Makes sure Windows users don't accidentally introduce CRLF line endings into a file that uses LF line endings
  - None-autofixes:
    - `check-yaml`: loads YAML files to validate syntax
    - `check-toml`: loads TOML files to validate syntax
    - `check-merge-conflict`: detects merge-conflict strings in files and blocks them from accidentally being committed
    - `check-case-conflict`: checks for files with names that would conflict on a case-insensitive filesystem like MacOS HFS+ or Windows FAT; blocks them from being committed.
  - Change the bot schedule to quarterly, to reduce noisy PRs
  - Change the `black` language target-version to Python 3.10, synching the setting here with the changes that were made to our `pyproject.toml` file in #7538

## 22.1.0.5 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 22.1.0.4 (2022-11-26)

Add aiofiles.os.scandir (#9280)

## 22.1.0.3 (2022-11-13)

Complete stubtest for `aiofiles` + fix on Windows (#9184)

## 22.1.0.2 (2022-11-08)

Fix and allow classes with missing metaclasses (#9136)

## 22.1.0.1 (2022-11-05)

Remove `aiofiles/tempfile/temptypes.pyi` from pyright exclude (#9104)

## 22.1.0 (2022-09-09)

[stubsabot] Bump aiofiles to 22.1.* (#8714)

Co-authored-by: stubsabot <>

## 0.8.11 (2022-08-29)

Delete some unused `# noqa` comments (#8639)

## 0.8.10 (2022-07-18)

Run `pycln` as a pre-commit hook in CI (#8304)

## 0.8.9 (2022-07-06)

Add missing aiofiles.tempfile classes (#7523)

Fixes: #6524

Co-authored-by: Andrej Shadura <andrew.shadura@collabora.co.uk>
Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 0.8.8 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 0.8.7 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 0.8.6 (2022-03-29)

Remove unneeded `# noqa` comments, fix broken `# noqa` comments (#7561)

## 0.8.5 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 0.8.4 (2022-03-07)

Improve open overloads when mode is a literal union (#7428)

As pointed out by @gvanrossum in https://github.com/python/typing/issues/1096

Improves type inference in cases when we know that mode is
OpenBinaryMode, but don't know anything more specific:
```
def my_open(name: str, write: bool):
    mode: Literal['rb', 'wb'] = 'wb' if write else 'rb'
    with open(name, mode) as f:
        reveal_type(f)  # previously typing.IO[Any], now typing.BinaryIO
```

You may be tempted into thinking this is some limitation of type
checkers. mypy does in fact have logic for detecting if we match
multiple overloads and union-ing up the return types of matched
overloads. The problem is the last overload interferes with this logic.
That is, if you remove the fallback overload (prior to this PR), you'd get
"Union[io.BufferedReader, io.BufferedWriter]" in the above example.

Co-authored-by: hauntsaninja <>

## 0.8.3 (2022-01-13)

Add stubs for aiofiles.os.path (#6787)

## 0.8.2 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 0.8.0 (2022-01-02)

Add missing functions and keyword arguments to aiofiles.os (#6785)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 0.7.3 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 0.7.2 (2021-12-26)

Enable stubtest for aiofiles (#6698)

## 0.7.1 (2021-12-25)

Add a 'stubtest' flag to METADATA.toml (#6687)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 0.7.0 (2021-10-12)

Update remaining versions for third-party stubs (#6094)

Also remove the python2 markers of packages that don't list Python 2
as supported in the latest version.

Don't special case version '0.1'

Co-authored-by: Akuli <akuviljanen17@gmail.com>

