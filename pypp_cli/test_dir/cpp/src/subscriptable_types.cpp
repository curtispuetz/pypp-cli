#include "subscriptable_types.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_bridge_library_test_0/subscriptable_type.h"
#include "pypp_util/print.h"

void subscriptable_types_fn() {
    print(PyStr("pypp SUBSCRIPTABLE TYPES RESULTS:"));
    PseudoSubscriptableTypeCpp<int> a = PseudoSubscriptableTypeCpp<int>(9);
    a.print();
    PseudoSubscriptableTypeCpp<PyStr> b = PseudoSubscriptableTypeCpp<PyStr>(10);
    b.print();
    PseudoSubscriptableType2Cpp<int> c =
        PseudoSubscriptableType2Cpp<int>(PyList({1, 2}));
    c.print();
    PseudoSubscriptableType2Cpp<PyStr> d =
        PseudoSubscriptableType2Cpp<PyStr>(PyList({PyStr("a"), PyStr("b")}));
    d.print();
    PseudoSubscriptableType2Cpp<PyStr> e =
        PseudoSubscriptableType2Cpp(PyList({PyStr("c"), PyStr("d")}));
    e.print();
}
