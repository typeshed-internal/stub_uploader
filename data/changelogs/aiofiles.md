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

