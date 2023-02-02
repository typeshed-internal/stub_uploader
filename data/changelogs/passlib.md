## 1.7.7.7 (2023-02-02)

Manual changes of `Any` union to `Incomplete` in stubs folder (#9566)

- ClassVar[Any | None]
- Missed previous changes due to alias
- Manual review of leftover Any unions (`| Any` and `Any |`)

## 1.7.7.6 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9565)

## 1.7.7.5 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 1.7.7.4 (2023-01-13)

Fix passlib stubtest on windows (#9523)

## 1.7.7.3 (2022-11-29)

Mark `passlib` as completed (#9302)

## 1.7.7.2 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 1.7.7.1 (2022-11-09)

Annotate known magic-method return types (#9131)

## 1.7.7 (2022-07-12)

Use error codes for type ignores (#8280)

Disable reportSelfClsParameterName for pytype as this is out of typeshed's
control

Closes: #7497

## 1.7.6 (2022-07-05)

Improve passlib CryptContext typing (#8237)

## 1.7.5 (2022-04-05)

Mark many attributes as read-only properties (#7591)

## 1.7.4 (2022-03-27)

passlib: Annotate various handler methods and fields (#7521)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 1.7.3 (2022-03-19)

Add mypy error codes to `type: ignore`s, remove unused ignores (#7504)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.7.2 (2022-03-14)

passlib: Annotate pbkdf2_sha* (#7486)

## 1.7.1 (2022-03-13)

passlib: fix MutableMapping import (#7479)

Found by #7478

## 1.7.0 (2022-03-07)

Add passlib stubs (#7024)

