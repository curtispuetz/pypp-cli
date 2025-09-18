from dataclasses import dataclass
from pypp_python.stl import Random

# TODO: I could consider changing import random to from pypp_python.stl import random
# as well as the other standard library things. I could also consider different
# ways of importing things. Like from pypp_python.stl.random import Random. or just
# from pypp_python.stl import Random.


def _random_as_arg(a: Random) -> float:
    return a.random()


@dataclass
class _RandomWrapper:
    _r: Random

    def mult(self, b: Random) -> float:
        return self._r.random() * b.random()


def random_fn():
    print("pypp RANDOM RESULTS:")
    a: Random = Random(42)
    a.seed(123)
    b: float = a.random()
    print(b)
    print(_random_as_arg(a))
    c: _RandomWrapper = _RandomWrapper(a)
    d: float = c.mult(a)
    print(d)
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
        print(f"Caught Random.choice exception: {ex}")
    print("Expected: [0.052, 1, [1, 3, 2], 3] for Python:")
    print("Excepted: [0.713, 8, [2, 1, 3], 3] for C++:")
    print(f"[{b}, {e}, {f}, {g}]")
