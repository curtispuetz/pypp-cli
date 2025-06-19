from typing import Generic, TypeVar
from numpy.typing import NDArray
import numpy as np

T = TypeVar("T", bound=np.generic)


class PyppNpArr(Generic[T]):
    def __init__(self, np_arr: NDArray[T]):
        self._d = np_arr

    def __call__(self, *args) -> NDArray[T]:
        return self._d[*args]

    def set(self, loc: tuple[int, ...], value: T | int | float):
        self._d[loc] = value

    def print(self):
        print(self._d)

    def __str__(self) -> str:
        return self._d.__str__()

    @property
    def raw(self) -> NDArray[T]:
        return self._d
