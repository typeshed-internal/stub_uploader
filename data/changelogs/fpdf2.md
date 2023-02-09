## 2.6.1.4 (2023-02-09)

Fix Any subclassing in `fpdf2` (#9536)

## 2.6.1.3 (2023-02-07)

Bump mypy to 1.0 (#9684)

## 2.6.1.2 (2023-01-18)

[fpdf2] Restore string default values (#9562)

Cf. #9546

## 2.6.1.1 (2023-01-18)

Replace `Any` with `Incomplete` in many places (#9558)

## 2.6.1.0 (2023-01-17)

Update fpdf2 stubs to 2.6.1 (#9546)

## 2.6.0.5 (2023-01-14)

Pin `fpdf2` stubs to 2.6.0 (#9535)

They will need some updates to become compatible with `fpdf2` 2.6.1.

Closes #9524

## 2.6.0.4 (2022-12-25)

fpdf:annotation of dash_pattern, line_width, text_mode (#9387)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.6.0.3 (2022-12-13)

Fpdf2: annotate more graphics_state properties (#9337)

## 2.6.0.2 (2022-12-05)

fpdf:annotation of underline, font_style, font_streching (#9327)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 2.6.0.1 (2022-12-01)

fpdf2: annotate draw_color, fill_color, text_color (#9282)

## 2.6.0.0 (2022-11-23)

Update fpdf2 stubs to 2.6 (#9236)

Mark first argument of `__[get|set|del]attr__` as `str` (#9245)

## 2.5.4.3 (2022-10-14)

Add return types to fpdf.drawing (#8891)

Co-authored-by: Akuli <akuviljanen17@gmail.com>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 2.5.4.2 (2022-10-06)

`fpdf2`: complete stubs (#8855)

## 2.5.4.1 (2022-10-04)

`fpdf2`: Add missing files (#8836)

## 2.5.4 (2022-09-11)

Update `fdpf2` stubs for v2.5.7 (#8721)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.5.3 (2022-08-30)

`fpdf2`: Remove redundant `str | Literal['DEPRECATED']` union (#8650)

## 2.5.2 (2022-08-17)

fpdf2: fix for 2.5.6 changes (#8546)

Life is much easier when upstream has some annotations

Fixes #8545

## 2.5.1 (2022-07-04)

Fix size parameter of FPDF.set_font_size (#8234)

## 2.5.0 (2022-06-29)

Bump fpdf2 to 2.5.* (#8173)

Co-authored-by: hauntsaninja <>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 2.4.9 (2022-06-26)

fpdf2: improve types (#8176)

Co-authored-by: hauntsaninja <>

## 2.4.8 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 2.4.7 (2022-02-10)

fpdf2: Correct annotations of @contextmanager methods (#7172)

## 2.4.5 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.4.4 (2021-12-23)

Fix third-party issues found by stubtest (#6667)

## 2.4.3 (2021-12-21)

Add some missing attributes and types to FPDF (#6618)

## 2.4.2 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 2.4.1 (2021-11-16)

Improve fpdf.image_parsing (#6313)

* Annotate more attributes, arguments, and return types.
* Add "dims" argument to get_img_info(), added in 2.4.6.

## 2.4.0 (2021-11-10)

Add stubs for fpdf2 (#6252)

