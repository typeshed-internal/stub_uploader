## 63.2.3 (2022-08-03)

Remove redundant `__str__` methods (#8475)

## 63.2.2 (2022-07-28)

Fix todo in setuptools.command.test (#8416)

With https://github.com/python/mypy/pull/10884 merged and released, this should be safe to re-enable per the todo comment.

https://github.com/pypa/setuptools/blob/main/setuptools/command/test.py#L117

## 63.2.1 (2022-07-20)

Update setuptools stubs (#8345)

setuptools now vendors `distutils` as `setuptools._distutils`.

## 63.2.0 (2022-07-15)

[stubsabot] Bump setuptools to 63.2.* (#8301)

Co-authored-by: hauntsaninja <>

## 62.6.1 (2022-07-11)

Remove Python 3.6 branches from typeshed (#8269)

## 62.6.0 (2022-07-08)

[stubsabot] Bump setuptools to 62.6.* (#8224)

Most of setuptools.config is not included as the module is deprecated.

## 57.4.18 (2022-06-26)

Third-party stubs: audit `Callable[<parameters>, None]` annotations (#8175)

## 57.4.17 (2022-05-26)

Third-party stubs: fix several fictitious type aliases (#7958)

## 57.4.16 (2022-05-25)

pkg_resources: Fix unconstrained TypeVars (#7941)

https://github.com/pypa/setuptools/blob/499c468a57d240e5bb450bdb6daedc3e559541dd/pkg_resources/__init__.py#L1049

Part of #7928

## 57.4.15 (2022-05-22)

More setuptools.command.easy_install definitions. (#7145)

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 57.4.14 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 57.4.13 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 57.4.12 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 57.4.11 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 57.4.10 (2022-03-08)

Widen the `cmdclass` parameter of `setuptools.setup` (#7458)

## 57.4.9 (2022-02-07)

Improve some in-place BinOp methods (#7149)

## 57.4.8 (2022-01-30)

Reduce use of `Any` in equality methods (#7081)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 57.4.7 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 57.4.5 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 57.4.4 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 57.4.3 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 57.4.2 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 57.4.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 57.4.0 (2021-09-19)

Add setuptools stubs (#5762)

