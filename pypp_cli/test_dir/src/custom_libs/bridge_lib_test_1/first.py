from pypp_bridge_library_test_1.first import pseudo_fn
from pypp_bridge_library_test_1.first_folder.third import pseudo_fn_b
from pypp_bridge_library_test_1.second import pseudo_fn_a


def bridge_lib_test_1_fn():
    print("pypp BRIDGE LIB TEST 1 RESULTS:")
    print(pseudo_fn())
    print(pseudo_fn_b())
    print(pseudo_fn_a())
