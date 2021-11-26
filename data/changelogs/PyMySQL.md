## 1.0.6 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 1.0.5 (2021-11-09)

Improve pymysql.converters stubs (#6267)

I spent far too much time being confused about why pyanalyze thought `pymysql.converters.escape_dict` only takes two arguments.

I rewrote the stubs from scratch using the implementation: https://github.com/PyMySQL/PyMySQL/blob/main/pymysql/converters.py.

The "charset" argument is ignored as far as I can tell; it gets passed to other functions but no function actually uses it.

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

## 1.0.4 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 1.0.3 (2021-10-12)

Add star to all non-0.1 versions (#6146)

