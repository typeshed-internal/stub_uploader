## 2.4.6 (2022-05-27)

constructors: Fix defaulted TypeVars (#7965)

From the list in https://github.com/microsoft/pyright/issues/3501

## 2.4.5 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.4.4 (2022-02-22)

Correct several positional-only differences in third-party stubs (#7352)

## 2.4.3 (2022-02-21)

contextvars, pycurl: make classes final (#7334)

## 2.4.2 (2022-01-27)

Improve `contextvars.Context` (#7052)

Similar changes to the ones @sobolevn made in #6942

## 2.4.0 (2021-10-12)

Update remaining versions for third-party stubs (#6094)

Also remove the python2 markers of packages that don't list Python 2
as supported in the latest version.

Don't special case version '0.1'

Co-authored-by: Akuli <akuviljanen17@gmail.com>

