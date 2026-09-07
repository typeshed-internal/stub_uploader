## [1.5.1.20260907](https://pypi.org/project/types-rasterio/1.5.1.20260907/) (2026-09-07)

* Accept int EPSG codes and any to_wkt provider in CRSInput ([#16294](https://github.com/python/typeshed/pull/16294))

    `CRS.from_user_input` dispatches on a `to_wkt` method before checking any
    concrete type, and reads a bare `int` as an EPSG code. Model the former as a
    `_SupportsToWkt` Protocol rather than taking a dependency on pyproj.

## [1.5.1.20260906](https://pypi.org/project/types-rasterio/1.5.1.20260906/) (2026-09-06)

* Allow WarpedVRT to take DatasetWriter ([#16156](https://github.com/python/typeshed/pull/16156))

## [1.5.1.20260819](https://pypi.org/project/types-rasterio/1.5.1.20260819/) (2026-08-19)

* 1.5.1 support ([#16180](https://github.com/python/typeshed/pull/16180))

## [1.5.0.20260810](https://pypi.org/project/types-rasterio/1.5.0.20260810/) (2026-08-10)

* Pin to 1.5.0 ([#16172](https://github.com/python/typeshed/pull/16172))

    Remove redundant stubtest-dependencies field

## [1.5.0.20260728](https://pypi.org/project/types-rasterio/1.5.0.20260728/) (2026-07-28)

* Accept WarpedVRT and __geo_interface__ geometries ([#16092](https://github.com/python/typeshed/pull/16092))

    Widen dataset parameters from the concrete DatasetReader to the shared \
    DatasetReaderBase so any readable dataset (including WarpedVRT) is \
    accepted, matching the runtime duck-typed contract:
    - merge.merge and stack.stack sources
    - features.geometry_window and features.dataset_features
    - mask.mask and mask.raster_geometry_mask
    - sample.sample_gen
    - the AnyDataset alias (now DatasetReaderBase | MemoryFile)

    Introduce a shared Geometry alias in _typing (a GeoJSON-like Mapping or \
    any object implementing __geo_interface__, e.g. shapely geometries) and \
    use it wherever the runtime unwraps __geo_interface__:
    - features.rasterize, geometry_mask, bounds, is_valid_geom, geometry_window
    - mask.mask and mask.raster_geometry_mask shapes
    - warp.transform_geom and _warp._transform_geom

    `Geometry` now lives in the blanket-allowlisted `rasterio._typing` module \
    and is only re-exported from `rasterio.features`.

## [1.5.0.20260724](https://pypi.org/project/types-rasterio/1.5.0.20260724/) (2026-07-24)

* Import `Self` from `typing_extensions` ([#16080](https://github.com/python/typeshed/pull/16080))

* Add stubs ([#15884](https://github.com/python/typeshed/pull/15884))

