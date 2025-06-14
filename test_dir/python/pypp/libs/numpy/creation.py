from typing import Type, TypeVar
import numpy as np

from test_dir.python.pypp.libs.numpy.impl import PyppNpArr

T = TypeVar("T")


def _check_dtype(dtype: Type[np.generic]):
    if not issubclass(dtype, np.generic):
        raise TypeError("A numpy generic type class (e.g., np.float32) is required.")


def pypp_np_zeros(shape: list[int], dtype: Type[T]) -> PyppNpArr[T]:
    _check_dtype(dtype)
    return PyppNpArr(np.zeros(shape, dtype))


def pypp_np_ones(shape: list[int], dtype: Type[T]) -> PyppNpArr[T]:
    _check_dtype(dtype)
    return PyppNpArr(np.ones(shape, dtype))


def pypp_np_full(shape: list[int], fill_value, dtype: Type[T]) -> PyppNpArr[T]:
    _check_dtype(dtype)
    return PyppNpArr(np.full(shape, fill_value, dtype))
