from typing import Iterator

from compy_python.ownership import mov


def yield_123() -> Iterator[int]:
    yield 1
    yield 2
    yield 3


def yield_over_list() -> Iterator[int]:
    for i in [1, 2, 3]:
        yield i


def yield_from_example() -> Iterator[int]:
    yield from yield_over_list()


def yield_fn():
    print("YIELD RESULTS:")
    a: list[int] = []
    for i in yield_123():
        y: int = i
        a.append(mov(y))
    print(a)
    for i in yield_over_list():
        y: int = i
        a.append(mov(y))
    print(a)
    for i in yield_from_example():
        y: int = i
        a.append(mov(y))
    print(a)
