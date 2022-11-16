## 2.11.0.1 (2022-11-16)

Always use `bool` and `Literal` for Python compat code (#9213)

## 2.11.0.0 (2022-11-11)

[stubsabot] Bump aws-xray-sdk to 2.11.* (#9156)

Release: https://pypi.org/pypi/aws-xray-sdk/2.11.0
Homepage: https://github.com/aws/aws-xray-sdk-python
Diff: https://github.com/aws/aws-xray-sdk-python/compare/2.10.0...2.11.0

Stubsabot analysis of the diff between the two releases:
 - 7 public Python files have been added: `aws_xray_sdk/core/utils/sqs_message_helper.py`, `aws_xray_sdk/ext/httpx/__init__.py`, `aws_xray_sdk/ext/httpx/patch.py`, `tests/ext/httpx/__init__.py`, `tests/ext/httpx/test_httpx.py`, `tests/ext/httpx/test_httpx_async.py`, `tests/test_sqs_message_helper.py`.
 - 0 files included in typeshed's stubs have been deleted.
 - 7 files included in typeshed's stubs have been modified or renamed: `aws_xray_sdk/core/async_recorder.py`, `aws_xray_sdk/core/lambda_launcher.py`, `aws_xray_sdk/core/models/dummy_entities.py`, `aws_xray_sdk/core/models/entity.py`, `aws_xray_sdk/core/patcher.py`, `aws_xray_sdk/core/recorder.py`, `aws_xray_sdk/version.py`.
 - Total lines of Python code added: 858.
 - Total lines of Python code deleted: 56.

## 2.10.1 (2022-07-04)

Third-party stubs: audit more `Callable[<parameters>, Any]` annotations (#8233)

## 2.10.0 (2022-07-01)

[stubsabot] Bump aws-xray-sdk to 2.10.* (#8221)

Co-authored-by: hauntsaninja <>

## 2.9.0 (2022-06-26)

[stubsabot] Bump aws-xray-sdk to 2.9.* (#8180)

* [stubsabot] Bump aws-xray-sdk to 2.9.*

Co-authored-by: hauntsaninja <>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.8.5 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 2.8.4 (2022-02-03)

Improve `__enter__` & constructor methods (#7114)

## 2.8.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.8.1 (2021-09-13)

Add more annotations to aws_xray_sdk.core.recorder (#6029)

