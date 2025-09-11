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
    b: float = a.random()
    print(b)
    print(_random_as_arg(a))
    c: _RandomWrapper = _RandomWrapper(a)
    d: float = c.mult(a)
    print(d)
