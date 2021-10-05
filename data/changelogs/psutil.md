## 5.8.10 (2021-10-05)

Add several missing type annotations to `psutil._common` (#6104)

## 5.8.9 (2021-10-05)

Properly export types from psutil._compat (#6112)

## 5.8.8 (2021-09-25)

Improves `Popen` types in `psutil` (#6074)

## 5.8.7 (2021-09-25)

Further improvements to `psutil` (#6072)

Adds types to the following functions:
- `psutil.environ()`
- `psutil.send_signal()`
- `psutil.sensors_temperatures()`
- `psutil.sensors_fans()`
- `psutil.sensors_battery()`

## 5.8.6 (2021-09-24)

Further annotations for the psutil module (#6066)

## 5.8.5 (2021-09-10)

Annotate more NamedTuples for psutil (#6021)

## 5.8.4 (2021-09-09)

Annotate several NamedTuples in psutil (#6016)

Annotate more methods of psutil.Process (#6012)

## 5.8.3 (2021-09-06)

Improves `psutil/_common.pyi` (#6010)

* Improves `psutil/_common.pyi`

In this iteration I've fixed the most obvious types and corrected several mistakes.
We can go deeper in the next iteration(s).

* We don't need to import `Union`

* Update _common.pyi

* Update _common.pyi

* Update _common.pyi

## 5.8.2 (2021-09-06)

Adds more missing `ContextManager` types (#6007)

1. https://github.com/giampaolo/psutil/blob/c3e63b4dd59f1724a7fa29371e53dfa7f46cbcd3/psutil/_psbsd.py#L571
2. https://github.com/giampaolo/psutil/blob/c3e63b4dd59f1724a7fa29371e53dfa7f46cbcd3/psutil/_psosx.py#L365

## 5.8.1 (2021-09-05)

Fix return type of Process.oneshot() (#6006)

