## 1.7.3.1 (2022-10-01)

Add `parser` to `invoke.completion.complete.complete` (#8819)

Closes https://github.com/python/typeshed/issues/8818

## 1.7.3 (2022-07-13)

Add types to `invoke.Runner.run` (#8279)

Co-authored-by: AlexWaygood <alex.waygood@gmail.com>

## 1.7.2 (2022-07-04)

Third-party stubs: audit more `Callable[<parameters>, Any]` annotations (#8233)

## 1.7.1 (2022-06-22)

Improve several `__hash__` methods (#8128)

## 1.7.0 (2022-06-21)

Bump invoke to 1.7.* (#8111)

## 1.6.8 (2022-05-25)

invoke: Fix unconstrained TypeVar (#7943)

Part of #7928

https://github.com/pyinvoke/invoke/blob/f34c6c9413146a34ede3a5b529916b4cee649887/invoke/tasks.py#L328

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

