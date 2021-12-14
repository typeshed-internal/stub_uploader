## 2021.3.3 (2021-12-14)

Add abstract methods to BaseTzInfo (#6579)

While these abstract methods don't exist at runtime, all sub-classes of
BaseTzInfo implement them. It can be useful to annotate variables with
BaseTzInfo and being able to call these methods on it.

## 2021.3.2 (2021-12-09)

pytz: rework stubs (#6551)

## 2021.3.1 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 2021.3.0 (2021-10-12)

Add star to all non-0.1 versions (#6146)

