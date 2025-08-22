import math
import random

from compy_python.ownership import Valu, mov
from compy_python.tuple_get import tg


def _fade(t: float) -> float:
    # 6t^5 - 15t^4 + 10t^3 (smoothing function)
    return t * t * t * (t * (t * 6 - 15) + 10)


def _lerp(t: float, y_1: float, y_2: float) -> float:
    return y_1 + t * (y_2 - y_1)


GRADIENTS: list[tuple[int, int]] = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1),
]


class PerlinNoise:
    def __init__(self, permutation_table_size: int, permuted_list: Valu(list[int])):
        self._p_len = permutation_table_size
        self._p = permuted_list

    def calc(
        self,
        x: float,
        y: float,
        octaves: int = 1,
        persistence: float = 0.5,
        lacunarity: float = 2.0,
    ) -> float:
        freq: float = 1.0
        amplitude: float = 1.0
        noise: float = 0.0
        for _ in range(octaves):
            noise += self._calc_one_octave(x * freq, y * freq) * amplitude
            amplitude *= persistence
            freq *= lacunarity
        return noise

    def _calc_one_octave(self, x: float, y: float) -> float:
        g00, g10, g01, g11, u, v = self._calc_grad_vecs_and_relative_position(x, y)
        s: float = _fade(u)
        t: float = _fade(v)

        dot1: float = tg(g00, 0) * u + tg(g00, 1) * v
        dot2: float = tg(g10, 0) * (u - 1) + tg(g10, 1) * v
        dot3: float = tg(g01, 0) * u + tg(g01, 1) * (v - 1)
        dot4: float = tg(g11, 0) * (u - 1) + tg(g11, 1) * (v - 1)

        i1: float = _lerp(s, dot1, dot2)
        i2: float = _lerp(s, dot3, dot4)

        return _lerp(t, i1, i2)

    def _hash(self, x: int, y: int) -> int:
        return self._p[(self._p[x % self._p_len] + y) % self._p_len]

    def _gradient_vector(self, x: int, y: int) -> tuple[int, int]:
        # x and y are lattice points
        i: int = self._hash(x, y) % 8
        return GRADIENTS[i]

    def _calc_grad_vecs_and_relative_position(
        self, x: float, y: float
    ) -> tuple[
        tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int], float, float
    ]:
        x0: int = int(math.floor(x))
        y0: int = int(math.floor(y))
        x1: int = x0 + 1
        y1: int = y0 + 1
        u: float = x - x0
        v: float = y - y0
        return (
            self._gradient_vector(x0, y0),
            self._gradient_vector(x1, y0),
            self._gradient_vector(x0, y1),
            self._gradient_vector(x1, y1),
            u,
            v,
        )


def create_perlin_noise(permutation_table_size: int, rng: random.Random) -> PerlinNoise:
    arr_to_shuffle: list[int] = [mov(i) for i in range(1, permutation_table_size + 1)]
    rng.shuffle(arr_to_shuffle)
    return PerlinNoise(permutation_table_size, mov(arr_to_shuffle))
