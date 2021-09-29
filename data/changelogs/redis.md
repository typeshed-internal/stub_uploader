## 3.5.9 (2021-09-29)

redis: include local property on Lock class (#6083)

The Lock class as a property local that has a token property that sometimes
needs be accessed / set.

```python
lock = redis.lock(key)
lock.local.token = token
lock.extend(10)
```

Technically the type of `local` is `SimpleNamespace | threading.local`
but I think this setup is a bit stricter but satisfies the API.

## 3.5.8 (2021-09-10)

Fix type of blocking_timeout argument to redis.lock.Lock (#6019)

## 3.5.7 (2021-08-29)

do not use mypy-specific syntax in '# type: ignore' comments (#5953)

