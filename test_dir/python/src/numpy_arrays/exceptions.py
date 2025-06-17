import numpy as np

from test_dir.python.pypp.libs.numpy.creation import pypp_np_zeros, pypp_np_array
from test_dir.python.pypp.libs.numpy.impl import PyppNpArr


def numpy_array_exceptions_fn():
    print("NUMPY ARRAY EXCEPTIONS RESULTS:")
    a: PyppNpArr[np.float32] = pypp_np_zeros([2, 3], np.float32)
    try:
        a(0, 0, 0)
    except IndexError as e:
        print("index error: " + str(e))
    try:
        a(99, 0)
    except IndexError as e:
        print("index error: " + str(e))
    try:
        a(0, 98)
    except IndexError as e:
        print("index error: " + str(e))
    empty_list: list[int] = []
    try:
        pypp_np_zeros(empty_list, np.float32)
    except ValueError as e:
        print("value error: " + str(e))
    try:
        pypp_np_array(empty_list, np.float32)
    except ValueError as e:
        print("value error: " + str(e))
    try:
        pypp_np_zeros([-1, 2], np.float32)
    except ValueError as e:
        print("value error: " + str(e))
    try:
        pypp_np_array([[1, 2], [3, 4, 5]], np.float32)
    except ValueError as e:
        print("value error: " + str(e))
