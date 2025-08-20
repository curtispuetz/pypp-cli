from pypp_bridge_library_test_1.first import pseudo_fn
from pypp_bridge_library_test_1.second import pseudo_fn_a
from pypp_bridge_library_test_1.first_folder.third import pseudo_fn_b
import pypp_bridge_library_test_1.fourth as pseudo_namespace


def bridge_lib_test_1_fn():
    print("PYPP BRIDGE LIB TEST 1 RESULTS:")
    print(pseudo_fn())
    print(pseudo_fn_a())
    print(pseudo_fn_b())
    print(pseudo_namespace.pseudo_fn_c())
