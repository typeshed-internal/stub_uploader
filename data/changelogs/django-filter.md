## 25.2.0.20251228 (2025-12-28)

[django-filter] Fix BaseFilterSet.filter_for_lookup return type ([#15171](https://github.com/python/typeshed/pull/15171))

## 25.2.0.20251010 (2025-10-10)

[django-filter] Broaden OrderingFilter fields parameter type ([#14856](https://github.com/python/typeshed/pull/14856))

## 25.2.0.20251007 (2025-10-07)

[stubsabot] Bump django-filter to 25.2.* ([#14836](https://github.com/python/typeshed/pull/14836))

## 25.1.0.20250923 (2025-09-23)

[django-filter] Improve stubtest comment ([#14738](https://github.com/python/typeshed/pull/14738))

## 25.1.0.20250914 (2025-09-14)

Update mypy to 1.18.1 ([#14699](https://github.com/python/typeshed/pull/14699))

## 25.1.0.20250815 (2025-08-15)

[django-filter] Improve constructor param types and add missing re-exports ([#14556](https://github.com/python/typeshed/pull/14556))

* Accept `StrOrPromise` for field labels -- allow Django lazy translated strings.
* Added `__init__` params that are inherited from parent classes. Reduced usage of loosely typed `*args, **kwargs`.
* Removed `__init__` method type hints from classes whose parameters are same as parent class -- to avoid duplicating them.
* Added missing re-exports to `django_filters/rest_framework/__init__.pyi` -- the imports in this file are clearly meant as re-export

[django-filter] Replace list with more generic Sequence ([#14567](https://github.com/python/typeshed/pull/14567))

## 25.1.0.20250809 (2025-08-09)

[django-filter] Add type stubs (#14540)

