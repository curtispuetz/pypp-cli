from dataclasses import dataclass
import random


def _random_as_arg(a: random.Random) -> float:
    return a.random()


@dataclass
class _RandomWrapper:
    _r: random.Random

    def mult(self, b: random.Random) -> float:
        return self._r.random() * b.random()


def random_fn():
    print("pypp RANDOM RESULTS:")
    a: random.Random = random.Random(42)
    a.seed(123)
    b: float = a.random()
    print(b)
    print(_random_as_arg(a))
    c: _RandomWrapper = _RandomWrapper(a)
    d: float = c.mult(a)
    print(d)
    # TODO now: test more of the functions
    e: int = a.randint(1, 10)
    print(e)
    f: list[int] = [1, 2, 3]
    a.shuffle(f)
    print(f)
    g: int = a.choice(f)
    print(g)
    try:
        empty_list: list[int] = []
        a.choice(empty_list)  # should throw
    except IndexError as ex:
        print(f"Caught random.Random.choice exception: {ex}")
    # TODO: what does it print in Python and C++ with the seed number?
    # Python: [0.052, 1, [1, 3, 2], 3]
    print("Expected: [0.052, 1, [1, 3, 2], 3] for Python:")
    print("Excepted: [0.713, 8, [2, 1, 3], 3] for C++:")
    print(f"[{b}, {e}, {f}, {g}]")
