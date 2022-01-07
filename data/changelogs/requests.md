## 2.27.0 (2022-01-07)

requests: Add JSONDecodeError (#6838)

## 2.26.3 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 2.26.2 (2021-12-17)

Use stubtest 0.920 (#6589)

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>
Co-authored-by: Sebastian Rittau <srittau@rittau.biz>
Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 2.26.1 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 2.26.0 (2021-11-10)

Add some kwonly arguments to Session.send() (#6266)

Bump version to 2.26

## 2.25.12 (2021-11-09)

Remove BaseAdapter from requests.sessions (#6264)

## 2.25.11 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 2.25.10 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 2.25.9 (2021-09-25)

requests: Response.encoding can be None (#6067)

The type of the `encoding` attribute was previously typed as `str`, even though it can be `None` at runtime.

## 2.25.8 (2021-09-21)

Update Session.prepare_request, .get_adapter (#6058)

## 2.25.7 (2021-09-20)

Support name, content-type and headers in file upload (#6052)

`requests` supports not only passing binary file-like objects for multi-part file uploads but also additionally passing a name,  content-type and headers. This adds type hints for those options.

See https://docs.python-requests.org/en/master/user/quickstart/#post-a-multipart-encoded-file.

