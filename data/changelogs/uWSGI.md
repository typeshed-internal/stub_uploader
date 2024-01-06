## 2.0.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs (#11245)

## 2.0.0.1 (2023-11-24)

Third-party stubs: remove unused `type: ignore`s (#11063)

## 2.0.0.0 (2023-07-24)

Adds stubs for uWSGI (#10432)

This adds stubs for the uWSGI Python API.

Similarly to GDB the Python API is only accessible within a uWSGI process, some parts of the API also only exist if certain configuration options are enabled. This makes running stubtest a bit of pain.

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

