import numpy as np

from test_dir.python.pypp.libs.numpy.creation import (
    pypp_np_zeros,
    pypp_np_ones,
    pypp_np_full,
)
from test_dir.python.pypp.libs.numpy.impl import PyppNpArr


def numpy_arrays_fn():
    print("start of numpy arrays")
    a: PyppNpArr[np.float32] = pypp_np_zeros([2, 3], np.float32)
    a.print()
    b: PyppNpArr[np.float32] = pypp_np_ones([2, 3], np.float32)
    b.print()
    c: PyppNpArr[np.float32] = pypp_np_full([2, 3], -1, np.float32)
    c.print()
    pypp_np_zeros([2, 3], np.float64).print()
    pypp_np_zeros([2, 3], np.int16).print()
    pypp_np_zeros([2, 3], np.uint16).print()
    pypp_np_zeros([2, 3], np.int32).print()
    pypp_np_zeros([2, 3], np.uint64).print()
    pypp_np_zeros([2, 3], np.uint).print()
    pypp_np_zeros([2, 3], np.longdouble).print()
    pypp_np_zeros([2, 3], np.bool).print()
    pypp_np_ones([2, 3], np.bool).print()
