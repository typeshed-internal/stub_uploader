## 1.6.7 (2022-05-05)

Improve types of invoke/env.pyi (#7780)

## 1.6.6 (2022-04-16)

Third-party stubs: import from `collections.abc` where possible (#7637)

## 1.6.5 (2022-03-22)

Mark pre/post tasks in invoke tasks as iterable (#7531)

Fix wrong return type of invoke decorator (#7536)

Closes #7530

## 1.6.4 (2022-03-21)

Fix invoke task decorator (#7511)

The decorator can be called with and without (). The current types only consider the first case

## 1.6.3 (2022-03-17)

Add annotations to invoke.tasks (#7502)

## 1.6.2 (2022-02-07)

Improve a bunch of `__(deep)copy__` methods (#7148)

## 1.6.1 (2022-01-30)

Reduce use of `Any` in equality methods (#7081)

Co-authored-by: Akuli <akuviljanen17@gmail.com>

## 1.6.0 (2022-01-22)

Add stubs for invoke (#6938)

