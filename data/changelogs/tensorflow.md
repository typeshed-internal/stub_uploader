## 2.16.0.20240627 (2024-06-27)

[tensorflow] Pin keras to 3.3.* (#12221)

## 2.16.0.20240618 (2024-06-18)

Pin various stubs to numpy to < 2 (#12152)

Fixes #12146

## 2.16.0.20240617 (2024-06-17)

Replace `np.float_` alias removed in numpy 2.0 (#12138)

## 2.16.0.20240606 (2024-06-06)

Add stubs for tf.math.angle to math.pyi (#12099)

## 2.16.0.20240428 (2024-04-28)

Fix stubtest for TensorFlow with latest keras release (#11838)

## 2.16.0.20240424 (2024-04-24)

Fix stubtest errors in tensorflow with `keras>=3.3.2` (#11817)

## 2.16.0.20240423 (2024-04-23)

Bump tensorflow to 2.16.* (#11696)

## 2.15.0.20240422 (2024-04-22)

Simplify protoc install in protobuf generation scripts (#11785)

## 2.15.0.20240417 (2024-04-17)

Remove remaining bare `Incomplete`s (#11768)

Enable Y065

## 2.15.0.20240412 (2024-04-12)

Bump flake8-pyi to 24.4.0 (#11745)

## 2.15.0.20240411 (2024-04-11)

Bump mypy-protobuf in sync_tensorflow script and improve generation scripts (#11740)

## 2.15.0.20240314 (2024-03-14)

`tensorflow`: Add `tensorflow.keras.models.Model` (#11334)

Based on:

- https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/saved_model/__init__.pyi
- https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/types/experimental.pyi

`tensorflow`: Add missing members to the `tensorflow.keras.layers` module. (#11333)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Rebecca Chen <rechen@google.com>

`tensorflow` add `tensorflow.saved_model` (#11439)

Based on:
- https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/saved_model/__init__.pyi
- https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/types/experimental.pyi

## 2.15.0.20240311 (2024-03-11)

Use PEP 570 syntax in third party stubs (#11554)

## 2.15.0.20240303 (2024-03-03)

`tensorflow`: add partial `tf.nn` module. (#11388)

Some derived from:
https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/summary.pyi
https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/nn.pyi

## 2.15.0.20240302 (2024-03-02)

`tensorflow`: add `tensorflow.bitwise` (#11440)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

`tensorflow`: add `tensorflow.audio` (#11441)

`tensorflow`: add `tensorflow.keras.activations` members (#11444)

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

Add pyupgrade check outdated-version-block (UP036) (#11509)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.15.0.20240301 (2024-03-01)

`tensorflow`: add `tensorflow.autodiff` (#11442)

`tensorflow`: add `tensorflow.autograph` (#11443)

## 2.15.0.20240218 (2024-02-18)

`tensorflow`: add `tf.linalg` module (#11386)

Taken from:
https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/linalg.pyi

`tensorflow`: add `tf.ones`, `tf.zeros`, `tf.zeros_like` and `tf.ones_like` functions (#11368)

`tensorflow` add `tf.random` module (#11359)

Partially from Mehdi Drissi's stubs.

`tensorflow`: Add members from `tensorflow.keras.metrics` (#11329)

Partially taken from: https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/keras/metrics.pyi

`tensorflow`: add `tf.distribute.experimental.coordinator.RemoteValue` (#11349)

`tensorflow`: add `tf.strings` module (#11380)

Partially taken from:
https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/strings.pyi

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

`tensorflow`: Add some `tf.raw_ops` members. (#11387)

https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/raw_ops.pyi

## 2.15.0.20240217 (2024-02-17)

`tensorflow` Add `tensorflow.summary` module  (#11358)

Partially derived from https://github.com/hmc-cs-mdrissi/tensorflow_stubs/blob/main/stubs/tensorflow/summary.pyi

## 2.15.0.20240206 (2024-02-06)

`tensorflow`: Add `tensorflow.keras.callbacks` module (#11332)

## 2.15.0.20240205 (2024-02-05)

`tensorflow` fix `tensorflow.data.Dataset`'s zip (#11357)

A new shade of Black (#11362)

## 2.15.0.20240204 (2024-02-04)

`tensorflow`: bump version to 2.15 (#11352)

## 2.12.0.20240202 (2024-02-02)

`tensorflow`: add `tf.train.CheckpointOptions` and other `tf.train` members. (#11327)

## 2.12.0.20240201 (2024-02-01)

`tensorflow`: Add some functions from the config module (#11325)

`tensorflow`: Add (and rename) aliases (#11324)

`tensorflow`: add some tensorflow functions (#11326)

`tensorflow`: add `tensorflow.math.reduce_variance` (#11328)

## 2.12.0.20240131 (2024-01-31)

`tensorflow`: fix `tensorflow.VariableSynchronization` (#11330)

## 2.12.0.20240126 (2024-01-26)

Add `convert_to_tensor` to `tensorflow` (#11292)

## 2.12.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 2.12.0.10 (2023-11-09)

Bump flake8-pyi to 23.11.0 (#10997)

## 2.12.0.9 (2023-10-29)

Enable ruff's isort rules on files generated using mypy-protobuf (#10939)

Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 2.12.0.8 (2023-10-23)

Update mypy-protobuf (#10914)

Co-authored-by: Avasam <samuel.06@hotmail.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.12.0.7 (2023-08-28)

Consistently use `Generic` as the last base class (#10610)

## 2.12.0.6 (2023-07-20)

Add a few more upstream_repository URLs (#10489)

## 2.12.0.5 (2023-06-08)

Tensorflow losses (#10264)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>

## 2.12.0.4 (2023-05-22)

Add core tensorflow.data stubs (#10122)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.12.0.3 (2023-05-10)

Add `partial_stub` metadata field (#10157)

## 2.12.0.2 (2023-04-27)

tensorflow: feature columns (#10052)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.12.0.1 (2023-04-27)

tensorflow: Add legacy optimizers (#9997)

## 2.12.0.0 (2023-03-23)

[stubsabot] Bump tensorflow to 2.12.* (#9926)

Release: https://pypi.org/pypi/tensorflow/2.12.0
Homepage: https://www.tensorflow.org/

If stubtest fails for this PR:
- Leave this PR open (as a reminder, and to prevent stubsabot from opening another PR)
- Fix stubtest failures in another PR, then close this PR

## 2.11.0.8 (2023-03-15)

Tensorflow protobuf stubs (#9873)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 2.11.0.7 (2023-03-09)

Tensorflow keras layer (#9707)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>

## 2.11.0.6 (2023-02-24)

Fix some typos in comments (#9802)

## 2.11.0.5 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` (#9779)

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 2.11.0.4 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` (#9702)

## 2.11.0.3 (2023-02-01)

Tensorflow: Add more stubs (#9560)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.11.0.2 (2023-01-18)

Improve pre-commit config (#9563)

- Add a few more hooks. These are all very fast, and I've found them useful in other projects:
  - Autofixes:
    - `trailing-whitespace`: fixes trailing whitespace
    - `requirements-txt-fixer`: alphabetises items in `requirements.txt` files
    - `end-of-file-fixer`: makes sure every file ends with a single newline character
    - `mixed-line-ending`: Makes sure Windows users don't accidentally introduce CRLF line endings into a file that uses LF line endings
  - None-autofixes:
    - `check-yaml`: loads YAML files to validate syntax
    - `check-toml`: loads TOML files to validate syntax
    - `check-merge-conflict`: detects merge-conflict strings in files and blocks them from accidentally being committed
    - `check-case-conflict`: checks for files with names that would conflict on a case-insensitive filesystem like MacOS HFS+ or Windows FAT; blocks them from being committed.
  - Change the bot schedule to quarterly, to reduce noisy PRs
  - Change the `black` language target-version to Python 3.10, synching the setting here with the changes that were made to our `pyproject.toml` file in #7538

## 2.11.0.1 (2023-01-17)

Reenable flake8-pyi's Y011 and Y015 (#9551)

## 2.11.0.0 (2023-01-15)

Update tensorflow to 2.11 (#9543)

Co-authored-by: Mehdi Drissi <mdrissi@snapchat.com>

## 2.10.0.0 (2023-01-14)

Initial tensorflow stubs (#8974)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

