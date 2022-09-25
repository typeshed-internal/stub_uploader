## 1.16.20 (2022-09-25)

six: Remove unused `__future__` import (#8790)

## 1.16.19 (2022-08-23)

`six`: Fix incorrect `type[type[Any]]` annotation (#8599)

Mypy will (correctly, I think) start flagging `type[type[Any]]` as an illegal annotation when mypy 0.980 comes out. Let's fix it now, before it comes out.

## 1.16.18 (2022-07-12)

Import `Match` and `Pattern` from `re`, not `typing` (#8277)

## 1.16.17 (2022-07-04)

Third-party stubs: audit more `Callable[<parameters>, Any]` annotations (#8233)

## 1.16.16 (2022-06-13)

Use `_typeshed.IdentityFunction` more consistently (#8063)

## 1.16.15 (2022-04-13)

Add back six.moves.http_cookies.Morsel (#7617)

## 1.16.14 (2022-04-13)

Add back six.moves.configparser.Error (#7616)

## 1.16.13 (2022-04-12)

Add missing definitions to six.moves.http_client (#7615)

These were removed as a side-effect of #7327, which added
`__all__` to `http.client`. I checked that all the definitions
are present at runtime via `six.moves.http_client`.

## 1.16.12 (2022-03-09)

Remove Python 2 support from some third-party distributions (#7466)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 1.16.11 (2022-03-01)

Add six.create_bound_method dunders to allowlist (#7409)

Closes: #7404

## 1.16.10 (2022-01-19)

Use PEP 585 syntax in Python 2, `protobuf` & `_ast` stubs, where possible (#6949)

## 1.16.9 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 1.16.7 (2022-01-03)

Add six.moves.copyreg six stubs (#6793)

## 1.16.6 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 1.16.5 (2021-12-27)

Enable stubtest for six (#6699)

## 1.16.4 (2021-12-25)

Add a 'stubtest' flag to METADATA.toml (#6687)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 1.16.3 (2021-11-28)

dummy_thread/ing: remove in 3.9 (#6408)

https://bugs.python.org/issue37312

## 1.16.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

