# stub_uploader

[![Build status](https://github.com/typeshed-internal/stub_uploader/workflows/Check%20scripts/badge.svg)](https://github.com/typeshed-internal/stub_uploader/actions?query=workflow%3A%22Check+scripts%22)
[![Upload status](https://github.com/typeshed-internal/stub_uploader/workflows/Daily%20update%20of%20stubs%20from%20typeshed%20to%20PyPI/badge.svg)](https://github.com/typeshed-internal/stub_uploader/actions?query=workflow%3A%22Daily+update+of+stubs+from+typeshed+to+PyPI%22)

This repository contains scripts and GitHub actions to auto-upload
[typeshed](https://github.com/python/typeshed) stubs to [PyPI](https://pypi.org/).
The directory layout is self-explanatory:
* `/scripts` contains the Python scripts used by GitHub actions.
* `/tests` contains some tests for the above scripts.
* `/data` keeps the state for upload tasks. Currently this is the last
  [typeshed commit](https://github.com/typeshed-internal/stub_uploader/blob/main/data/last_typeshed_commit.sha1)
  successfully uploaded. And the [list of distributions](https://github.com/typeshed-internal/stub_uploader/blob/main/data/uploaded_packages.txt)
  successfully uploaded. These files are modified by the actions as described below. Finally, there is an
  [empty stub package](https://github.com/typeshed-internal/stub_uploader/tree/main/data/empty_package)
  used to test that PyPI API token is still valid.

There are four GitHub actions in the repository. Here is a brief explanation
of the role of each action.

### Check scripts (CI)

[This CI action](https://github.com/typeshed-internal/stub_uploader/actions?query=workflow%3A%22Check+scripts%22)
simply runs mypy and tests on each PR and push. You don't need to run it manually.

### Test PyPI API token

[This action](https://github.com/typeshed-internal/stub_uploader/actions?query=workflow%3A%22Test+PyPI+API+token%22)
can be used to check if PyPI API token issued to `typeshed_bot` account is still valid.
You normally need to only do it if there is a breakage that needs to be investigated.
The action can be only started manually, to do this go to the action page and click "Run workflow".
Then in the input window select a version increment for [test package](https://pypi.org/project/types-tsbot-empty/#history)
that is not present on PyPI. If you select `X`, the action will attempt to upload version
`0.1.X` of the package. It should only take few seconds. Check that the version you selected was
indeed successfully uploaded. If it was, it means the API token is valid, otherwise read the action
logs to figure out the issue. If the token is expired, generate a new token on PyPI and update the value of
`TYPESHED_BOT_API_TOKEN` on [this page](https://github.com/typeshed-internal/stub_uploader/settings/secrets/actions).

### Daily update of stubs from typeshed to PyPI

[This](https://github.com/typeshed-internal/stub_uploader/actions?query=workflow%3A%22Daily+update+of+stubs+from+typeshed+to+PyPI%22)
is the main action for automatically updating the stub packages. It is scheduled to run on a regular
basis (currently every three hours). Note that GitHub cron scheduling is not very precise, and can schedule
action several minutes late. If necessary, it can be run manually by clicking on "Run workflow".
The action will fetch typeshed repository, take the diff from last successfully updated typeshed commit,
and check if anything is changed in `/stubs` directory. If yes, it will build and upload corresponding
distributions. Then it will update the typeshed commit, and the list of packages (if new packages were uploaded)
in the `/data` directory (see above). Note that the packages are uploaded in the dependency order,
to verify that we don't depend on some foreign packages. Note that if `METADATA.toml` for a distribution
specifies version `X.Y`, this will check what is the latest uploaded minor version `X.Y.Z` and will upload
`X.Y.Z+1`, if there are no matching version, it will upload `X.Y.0`.

### Force update of some stubs from typeshed to PyPI

[This action](https://github.com/typeshed-internal/stub_uploader/actions?query=workflow%3A%22Force+update+of+some+stubs+from+typeshed+to+PyPI%22)
can be run to manually force upload new version of some packages. When you click on "Run workflow",
you will need to select the name of distribution to upload. This can be a Python regexp, for example,
`six` will only upload the `six` package, `"(typing-extensions|mypy-extensions)"` will upload both packages,
and entering `".*"` will select all packages (quotes are needed since these are passed as arguments in bash).
Note that this action also sorts packages in the dependency order, but it doesn't update the typeshed commit. It may update
[list of uploaded packages](https://github.com/typeshed-internal/stub_uploader/blob/main/data/uploaded_packages.txt)
if this is the first time the package is uploaded.
