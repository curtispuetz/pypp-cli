#include "subscriptable_types.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_bridge_library_test_0/subscriptable_type.h"
#include "pypp_util/print.h"

void subscriptable_types_fn() {
    pypp::print(pypp::PyStr("pypp SUBSCRIPTABLE TYPES RESULTS:"));
    PseudoSubscriptableTypeCpp<int> a = PseudoSubscriptableTypeCpp<int>(9);
    a.print();
    PseudoSubscriptableTypeCpp<pypp::PyStr> b =
        PseudoSubscriptableTypeCpp<pypp::PyStr>(10);
    b.print();
    PseudoSubscriptableType2Cpp<int> c =
        PseudoSubscriptableType2Cpp<int>(pypp::PyList({1, 2}));
    c.print();
    PseudoSubscriptableType2Cpp<pypp::PyStr> d =
        PseudoSubscriptableType2Cpp<pypp::PyStr>(
            pypp::PyList({pypp::PyStr("a"), pypp::PyStr("b")}));
    d.print();
    PseudoSubscriptableType2Cpp<pypp::PyStr> e = PseudoSubscriptableType2Cpp(
        pypp::PyList({pypp::PyStr("c"), pypp::PyStr("d")}));
    e.print();
}
