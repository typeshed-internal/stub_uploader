## 2.9.16 (2022-06-03)

psycopg2: stub improvements (#7964)

Fixes an entry from #7928 along with a number of other improvements.

I went off the C code:
https://github.com/psycopg/psycopg2/blob/master/psycopg/connection_type.c

## 2.9.15 (2022-05-30)

psycopg2: Fix the return type of Composable.as_string (#7984)

Signed-off-by: Zixuan James Li <359101898@qq.com>

## 2.9.14 (2022-05-21)

Annotations for psycopg2.ConnectionInfo (#7834)

* Annotations for psycopg2.ConnectionInfo

These annotations come from the documentation here:

https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.ConnectionInfo
If there was doubt, I referred to the libpq documentation cited by
psycopg2's docs.

I wasn't completely sure about `dsn_parameters`. Psycopg2's docs list it
as an `dict`, and the example suggests it's a `dict[str, str]` at that.
From psycopg2's source I found

    https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/conninfo_type.c#L183-L206

which is implemented here:

    https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/utils.c#L251-L279

I'm no expert in CPython's API, but this looks to me like it's building
a `dict[str, str]`.

Additionally, the libpq docs

https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-PQCONNINFO
https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-PQCONNDEFAULTS

show that the underlying data just consists of strings.

Additionally, I'm pretty sure from this chunk of source

    https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/conninfo_type.c#L581-L598

That `ConnectionInfo.__init__` takes one positional-only argument, which
must be a `psycopg2.connection`. But I don't think users are intended to
be constructing this type, so I've not added that annotation.

* Annotate `connection.info` and related attributes

* Make ConnectionInfo attributes properties

According to https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/conninfo_type.c#L534-L563

* Mark connection attributes as readonly

according to https://github.com/psycopg/psycopg2/blob/8ef195f2ff187454cc709d7857235676bb4176ee/psycopg/connection_type.c#L1244

* Explain why some properties aren't `T | None`

## 2.9.13 (2022-04-22)

Annotate Error and Diagnostics (#7671)

Move cursor class to top of file so it can be used as base class

## 2.9.12 (2022-04-20)

Use `TypeAlias` for type aliases where possible, part II (#7667)

## 2.9.11 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 2.9.10 (2022-04-08)

psycopg2: correct return type (#7607)

Fixes the return type of `psycopg2.cursor.fetchone()` to match the psycopg2 code:

https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/cursor_type.c#L647-L651
https://github.com/psycopg/psycopg2/blob/1d3a89a0bba621dc1cc9b32db6d241bd2da85ad1/psycopg/cursor_type.c#L748-L786

It also matches the [psycopg2 documentation](https://www.psycopg.org/docs/cursor.html?highlight=copy_from#cursor.fetchone) as well as the [DB-API](https://peps.python.org/pep-0249/#fetchone)

## 2.9.9 (2022-03-16)

psycopg2: Accept Composable in place of query string (#7494)

https://www.psycopg.org/docs/sql.html#psycopg2.sql.Composable
“Composable objects can be passed directly to execute(),
executemany(), copy_expert() in place of the query string.”

Signed-off-by: Anders Kaseorg <andersk@mit.edu>

## 2.9.8 (2022-03-08)

psycopg2: Annotate cursor execute* and dunder methods (#7460)

## 2.9.7 (2022-02-22)

Correct several positional-only differences in third-party stubs (#7352)

## 2.9.5 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.9.4 (2021-12-02)

Fix psycopg2 connection.cursor() stub (#6470)

Adds `scrollable=` argument missing since psycopg2 2.5 and prevents `Any` from being hinted when `cursor_factory=` is passed.

## 2.9.3 (2021-11-30)

psycopg2: use Error and Warning from _psycopg.pyi in errors.pyi (#6454)

## 2.9.2 (2021-11-23)

Move abstract methods to AbstractConnectionPool (#6340)

## 2.9.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

