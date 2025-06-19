import numpy as np

from test_dir.python.pypp.libs.numpy.creation import (
    pypp_np_zeros,
    pypp_np_ones,
    pypp_np_full,
    pypp_np_array,
)
from test_dir.python.pypp.libs.numpy.impl import PyppNpArr


def numpy_arrays_fn():
    print("NUMPY ARRAY RESULTS: ")
    # Zeros, ones, and full
    a: PyppNpArr[np.float32] = pypp_np_zeros([2, 3], np.float32)
    print(a)
    b: PyppNpArr[np.float32] = pypp_np_ones([2, 3], np.float32)
    print(b)
    c: PyppNpArr[np.float32] = pypp_np_full([2, 3], -1, np.float32)
    print(c)
    # All the supported types
    print(pypp_np_zeros([2, 3], np.float64))
    print(pypp_np_zeros([2, 3], np.int16))
    print(pypp_np_zeros([2, 3], np.uint16))
    print(pypp_np_zeros([2, 3], np.int32))
    print(pypp_np_zeros([2, 3], np.uint64))
    print(pypp_np_zeros([2, 3], np.uint))
    print(pypp_np_zeros([2, 3], np.longdouble))
    print(pypp_np_zeros([2, 3], np.bool))
    print(pypp_np_ones([2, 3], np.bool))
    # array 1D
    d: PyppNpArr[np.float64] = pypp_np_array([9.0, 10.0], np.float64)
    print(d)
    # array 2D
    e: PyppNpArr[np.float64] = pypp_np_array([[1.0, 2.0], [3.0, 4.0]], np.float64)
    print(e)
    # array 3D
    f: PyppNpArr[np.float64] = pypp_np_array(
        [[[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0, 99.0]]], np.float64
    )
    print(f)
    # array 4D
    g: PyppNpArr[np.float64] = pypp_np_array(
        [
            [[[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0, 99.0]]],
            [[[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0, -77.0]]],
        ],
        np.float64,
    )
    print(g)
    # Calculations
    h: float = d(0) * 56.455432737426
    print(str(h))
    # access
    i: float = d(0)
    print(str(i))
    j: np.float64 = d(0)
    print(str(j))
    # access with np.float32
    k: float = a(0, 0)
    print(str(k))
    l1: np.float32 = a(0, 0)
    print(str(l1))
    # setting elements
    a.set((0, 0), 1.0)
    print(a)
    a.set((0, 0), 2)
    print(a)
    # inline passing
    _inline_numpy_arr(pypp_np_array([1.0, 3.0], np.float64))


def _inline_numpy_arr(arr: PyppNpArr[np.float64]):
    print(arr)
