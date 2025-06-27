from typing import Iterator


def yield_123() -> Iterator[int]:
    yield 1
    yield 2
    yield 3

def yield_over_list() -> Iterator[int]:
    for i in [1, 2, 3]:
        yield i

def yield_fn():
    print("YIELD RESULTS:")
    a: list[int] = []
    for i in yield_123():
        a.append(i)
    print(a)
    for i in yield_over_list():
        a.append(i)
    print(a)
