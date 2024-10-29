## 5.0.0.20241029 (2024-10-29)

Use `lib/ts_utils` for `scripts/sync_protobuf` (#12913)

- Simplified `download_file` error handling (400+ return codes already raised errors!)
- Moved `update_metadata` from `scripts/sync_protobuf/_utils.py` to `lib/ts_utils/metadata.py`
- Improved `update_metadata` to support any key (values unvalidated atm) and return the modified dictionary
- Updated `scripts/stubsabot.py` to use `update_metadata`
- Updated `scripts/sync_protobuf/*` to use  `lib/ts_utils`
- Updated `scripts/sync_protobuf/tensorflow.py` and `scripts/sync_protobuf/google_protobuf.py` to use the version directly from the `METADATA.toml` file

## 5.0.0.20240920 (2024-09-20)

Rewrote protobuf generation scripts in Python (#12527)

## 5.0.0.20240423 (2024-04-23)

Create script to generate s2clientprotocol protobuf stubs (#11772)

Regenerate using mypy-protobuf 3.6

## 5.0.0.20240302 (2024-03-02)

Add pyupgrade check outdated-version-block (UP036) (#11509)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 5.0.0.3 (2023-10-29)

Enable ruff's isort rules on files generated using mypy-protobuf (#10939)

Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 5.0.0.2 (2023-10-23)

Check  `*_pb2.pyi` files again (#10909)

## 5.0.0.1 (2023-07-22)

Add `upstream_repository` to metadata for `s2clientprotocol` (#10500)

These stubs were added yesterday in #10372, and I forgot that we had just added this new metadata field

## 5.0.0.0 (2023-07-21)

Add stubs for s2clientprotocol (#10372)

