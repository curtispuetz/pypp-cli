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
