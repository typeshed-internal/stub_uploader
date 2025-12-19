## 1.1.0.20251219 (2025-12-19)

[assertpy] Replace or explain `Any`s ([#15144](https://github.com/python/typeshed/pull/15144))

## 1.1.0.20250502 (2025-05-02)

Correct type of `kwargs` in `assertpy.exception.ExceptionMixin.when_called_with` (#13903)

The keys of `kwargs` dicts are always strings, the type hint is for the values,
which in this case could be anything.

## 1.1.0.20250407 (2025-04-07)

Mark internal stuff in allowlist for `assertpy` (#13802)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 1.1.0.20240712 (2024-07-12)

Update assertpy/string.pyi to correct type of pattern arg (#12235)

The methods requires the pattern arg to be of type str, not Pattern.

Signed-off-by: BJ Hargrave <bj@hargrave.dev>

## 1.1.0.20240703 (2024-07-03)

Update assertpy/extracting.pyi so that kwargs are not required (#12229)

The recent change to better type the `sort` and `filter` kwargs had the
side effect of making them required. So we fix to supply a default
argument.

Signed-off-by: BJ Hargrave <bj@hargrave.dev>

## 1.1.0.20240627 (2024-06-27)

assertpy: improve type for extracting (#12224)

Signed-off-by: BJ Hargrave <bj@hargrave.dev>
Co-authored-by: hauntsaninja <hauntsaninja@gmail.com>

## 1.1.0.20240516 (2024-05-16)

Add stubs for `assertpy` (#11916)

