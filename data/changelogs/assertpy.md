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

