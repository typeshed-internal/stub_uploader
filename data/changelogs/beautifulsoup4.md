## 4.10.15 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 4.10.14 (2022-03-02)

bs4: expose several other classes (#7420)

On the same lines as #7419

These are all imports that are not used within bs4/__init__.py
My main interest here is in exposing NavigableString

Co-authored-by: hauntsaninja <>

## 4.10.13 (2022-03-02)

bs4: expose bs4.PageElement (#7419)

This is generally useful. It's also imported in the source without being
used in bs4/__init__.py which in well maintained packages is a pretty
good marker of intention to export

Co-authored-by: hauntsaninja <>

## 4.10.12 (2022-02-18)

Tag.attrs is a dict, instead of an immutable Mapping (#7253)

## 4.10.11 (2022-01-23)

bs4: Expose bs4.SoupStrainer and bs4.Tag (#7002)

## 4.10.10 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 4.10.9 (2022-01-07)

Update pyright (#6840)

## 4.10.7 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 4.10.6 (2021-12-23)

Fix third-party issues found by stubtest (#6667)

## 4.10.5 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 4.10.4 (2021-10-13)

Cleanup: use lower-case list and dict, add a test (#6161)

## 4.10.3 (2021-10-12)

Put Generic last in base class list (#6155)

## 4.10.2 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 4.10.1 (2021-09-27)

PageElement.find_all() can return any subclass of PageElement (#6081)

## 4.10.0 (2021-09-22)

Update for beautifulsoup4 for version 4.10 (#6059)

Tighten types and add missing fields

