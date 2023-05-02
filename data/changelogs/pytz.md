## 2022.7.1.0 (2023-01-15)

[stubsabot] Bump pytz to 2022.7.1 (#9540)

Release: https://pypi.org/pypi/pytz/2022.7.1
Homepage: http://pythonhosted.org/pytz

## 2022.7.0.0 (2022-12-19)

[stubsabot] Bump pytz to 2022.7 (#9383)

## 2022.6.0.1 (2022-11-01)

Remove `pytz` from `pyright`s exclude (#9041)

## 2022.6.0.0 (2022-11-01)

[stubsabot] Bump pytz to 2022.6 (#9049)

Release: https://pypi.org/pypi/pytz/2022.6
Homepage: http://pythonhosted.org/pytz

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2022.5.0.0 (2022-10-19)

[stubsabot] Bump pytz to 2022.5 (#8926)

Release: https://pypi.org/pypi/pytz/2022.5
Homepage: http://pythonhosted.org/pytz

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2022.4.0.0 (2022-10-05)

[stubsabot] Bump pytz to 2022.4 (#8848)

Release: https://pypi.org/pypi/pytz/2022.4
Homepage: http://pythonhosted.org/pytz

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

Note that you will need to close and re-open the PR in order to trigger CI

Co-authored-by: stubsabot <>

## 2022.2.1.0 (2022-08-19)

[stubsabot] Bump pytz to 2022.2.1 (#8564)

Co-authored-by: stubsabot <>

## 2022.1.2 (2022-07-19)

Add missing third party modules (#8321)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: hauntsaninja <>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 2022.1.1 (2022-06-26)

Check missing definitions for several packages (#8167)

Co-authored-by: hauntsaninja <>

## 2022.1.0 (2022-06-21)

[stubsabot] Bump pytz to 2022.1 (#8121)

Co-authored-by: hauntsaninja <>

## 2021.3.8 (2022-05-07)

Import generics from standard modules in all third-party stubs (#7791)

## 2021.3.7 (2022-04-27)

Drop Python 2 support in third-party stubs (#7703)

## 2021.3.6 (2022-03-19)

pytz: utcoffset only returns None if dt is None (#7510)

## 2021.3.5 (2022-02-13)

Fix argument types of pytz.tzinfo.StaticTzInfo (#7184)

The argument is_dst of the functions StaticTzInfo.localize and
StaticTzInfo.normalize are ignored, and only present for compatibility with
DstTzInfo. The functions in DstTzInfo also accepts None, so for compatibility,
StaticTzInfo should accept them as well.

[^1] https://github.com/stub42/pytz/blob/2ed682a7c4079042f50975970fc4f503c8450058/src/pytz/tzinfo.py#L112

## 2021.3.3 (2021-12-14)

Add abstract methods to BaseTzInfo (#6579)

While these abstract methods don't exist at runtime, all sub-classes of
BaseTzInfo implement them. It can be useful to annotate variables with
BaseTzInfo and being able to call these methods on it.

## 2021.3.2 (2021-12-09)

pytz: rework stubs (#6551)

## 2021.3.1 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 2021.3.0 (2021-10-12)

Add star to all non-0.1 versions (#6146)

