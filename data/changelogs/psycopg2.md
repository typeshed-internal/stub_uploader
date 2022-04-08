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

