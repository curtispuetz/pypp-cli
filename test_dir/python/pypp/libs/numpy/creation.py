from typing import Type, TypeVar
import numpy as np

from test_dir.python.pypp.libs.numpy.impl import PyppNpArr

T = TypeVar("T")


def _check_dtype_and_not_empty(shape: list[int], dtype: Type[np.generic]):
    if len(shape) == 0:
        raise ValueError("empty numpy array is not supported")
    _check_dtype(dtype)


def _check_dtype(dtype: Type[np.generic]):
    if not issubclass(dtype, np.generic):
        raise TypeError("A numpy generic type class (e.g., np.float32) is required.")


def pypp_np_zeros(shape: list[int], dtype: Type[T]) -> PyppNpArr[T]:
    _check_dtype_and_not_empty(shape, dtype)
    return PyppNpArr(np.zeros(shape, dtype))


def pypp_np_ones(shape: list[int], dtype: Type[T]) -> PyppNpArr[T]:
    _check_dtype_and_not_empty(shape, dtype)
    return PyppNpArr(np.ones(shape, dtype))


def pypp_np_full(shape: list[int], fill_value, dtype: Type[T]) -> PyppNpArr[T]:
    _check_dtype_and_not_empty(shape, dtype)
    return PyppNpArr(np.full(shape, fill_value, dtype))


U = TypeVar("U")


def pypp_np_array(data: list[U], dtype: Type[T]) -> PyppNpArr[T]:
    if len(data) == 0:
        raise ValueError("empty numpy array is not supported")
    _check_dtype(dtype)
    return PyppNpArr(np.array(data, dtype))
