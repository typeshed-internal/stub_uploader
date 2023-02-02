## 3.5.0.1 (2023-02-02)

Fix optional USB attributes in pyserial's `ListPortInfo` (#9654)

Some USB specific attributes in pyserial's [`serial.tools.list_port_common.ListPortInfo`](https://github.com/python/typeshed/blob/main/stubs/pyserial/serial/tools/list_ports_common.pyi#L11-L24) class are not always available. They depend on the USB device and its driver correctly reporting these attributes. I discovered this recently with a new device that does not report its serial number. Only the Vendor ID `vid` and Product ID `pid` are guaranteed (This can be seen [here](https://github.com/pyserial/pyserial/blob/master/serial/tools/list_ports_linux.py#L52-L62) where `vid` and `pid` are always cast as `int` while other attributes are left as `str | None` for USB devices).
This is a follow up to #9347 and the discussion at https://github.com/python/typeshed/pull/9347#issuecomment-1358245865

## 3.5.0.0 (2022-12-22)

Add stubs for the pyserial package (#9347)

