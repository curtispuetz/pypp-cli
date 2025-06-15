import numpy as np

from test_dir.python.pypp.libs.numpy.creation import (
    pypp_np_zeros,
    pypp_np_ones,
    pypp_np_full,
    pypp_np_array,
)
from test_dir.python.pypp.libs.numpy.impl import PyppNpArr


def numpy_arrays_fn():
    print("start of numpy arrays")
    # Zeros, ones, and full
    a: PyppNpArr[np.float32] = pypp_np_zeros([2, 3], np.float32)
    a.print()
    b: PyppNpArr[np.float32] = pypp_np_ones([2, 3], np.float32)
    b.print()
    c: PyppNpArr[np.float32] = pypp_np_full([2, 3], -1, np.float32)
    c.print()
    # All the supported types
    pypp_np_zeros([2, 3], np.float64).print()
    pypp_np_zeros([2, 3], np.int16).print()
    pypp_np_zeros([2, 3], np.uint16).print()
    pypp_np_zeros([2, 3], np.int32).print()
    pypp_np_zeros([2, 3], np.uint64).print()
    pypp_np_zeros([2, 3], np.uint).print()
    pypp_np_zeros([2, 3], np.longdouble).print()
    pypp_np_zeros([2, 3], np.bool).print()
    pypp_np_ones([2, 3], np.bool).print()
    # array 1D
    d: PyppNpArr[np.float64] = pypp_np_array([9.0, 10.0], np.float64)
    d.print()
    # array 2D
    e: PyppNpArr[np.float64] = pypp_np_array([[1.0, 2.0], [3.0, 4.0]], np.float64)
    e.print()
    # array 3D
    f: PyppNpArr[np.float64] = pypp_np_array(
        [[[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0, 99.0]]], np.float64
    )
    f.print()
    # array 4D
    g: PyppNpArr[np.float64] = pypp_np_array(
        [
            [[[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0, 99.0]]],
            [[[1.0, 2.0], [3.0, 4.0]], [[1.0, 2.0], [3.0, -77.0]]],
        ],
        np.float64,
    )
    g.print()
