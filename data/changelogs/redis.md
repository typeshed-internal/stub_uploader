## 4.0.5 (2021-12-21)

Fix Redis.zpopmin and zpopmax (#6642)

Co-authored-by: Sebastian Rittau <srittau@rittau.biz>

## 4.0.4 (2021-12-17)

Always import Protocol from typing in stubs (#6617)

## 4.0.3 (2021-12-01)

Fix various issues in redis.client (#6464)

## 4.0.2 (2021-12-01)

redis: fix several stubtest warnings (#6378)

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Shantanu <12621235+hauntsaninja@users.noreply.github.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 4.0.1 (2021-11-26)

Add mypy error codes to '# type: ignore' comments (#6379)

## 4.0.0 (2021-11-25)

Update redis stubs to version 4 (#6368)

## 3.5.18 (2021-11-23)

Reduce use of deprecated `typing` aliases (#6358)

## 3.5.17 (2021-11-18)

Revert "do not use mypy-specific syntax in '# type: ignore' comments" (#6338)

## 3.5.16 (2021-11-12)

Redis Sentinel master_for, slave_for returns a Redis client (#6269)

## 3.5.15 (2021-10-16)

Annotate Client.decr() and decrby() (#6179)

## 3.5.14 (2021-10-15)

Add redis/sentinel.pyi (#6174)

## 3.5.13 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 3.5.12 (2021-10-12)

Add star to all non-0.1 versions (#6146)

## 3.5.11 (2021-10-09)

Add Redis.memory_purge() (#6138)

## 3.5.10 (2021-10-09)

Add memory_stats() to Redis (#6137)

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

