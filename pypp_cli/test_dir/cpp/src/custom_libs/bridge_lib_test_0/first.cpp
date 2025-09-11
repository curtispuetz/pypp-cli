#include "custom_libs/bridge_lib_test_0/first.h"
#include "py_list.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_bridge_library_test_0/custom_list.h"
#include "pypp_bridge_library_test_0/custom_mapping_starts_with_call.h"
#include "pypp_bridge_library_test_0/include_only_call.h"
#include "pypp_bridge_library_test_0/modules_to_cpp_inc.h"
#include "pypp_bridge_library_test_0/modules_to_cpp_inc_2.h"
#include "pypp_bridge_library_test_0/name_only_call.h"
#include "pypp_bridge_library_test_0/pseudo_a.h"
#include "pypp_bridge_library_test_0/pseudo_custom_type_cpp.h"
#include "pypp_bridge_library_test_0/replace_with_double_colon_call.h"
#include "pypp_util/print.h"
#include <iostream>

namespace me {
void _as_arg(PseudoCustomTypeCpp &arg) { pypp::print(arg.get_a()); }

PseudoCustomTypeCpp _factory() { return PseudoCustomTypeCpp(100); }

class _ClassA {
  public:
    PseudoCustomTypeCpp &_pseudo_custom_type;
    _ClassA(PseudoCustomTypeCpp &a_pseudo_custom_type)
        : _pseudo_custom_type(a_pseudo_custom_type) {}
    int get_a() { return _pseudo_custom_type.get_a(); }
};

struct _DataClassA {
    const PseudoCustomTypeCpp &pseudo_custom_type;
    _DataClassA(PseudoCustomTypeCpp &a_pseudo_custom_type)
        : pseudo_custom_type(a_pseudo_custom_type) {}
};

struct __PseudoPyppName_ConfigClassA {
    PseudoCustomTypeCpp pseudo_custom_type = PseudoCustomTypeCpp(1);
};
inline __PseudoPyppName_ConfigClassA _ConfigClassA;

void bridge_lib_test_0_fn() {
    pypp::print(pypp::PyStr("pypp BRIDGE LIB TEST 0 RESULTS:"));
    PseudoCustomTypeCpp a = PseudoCustomTypeCpp(42);
    int b = a.get_a();
    pypp::print(b);
    _as_arg(a);
    _ClassA c = _ClassA(a);
    pypp::print(c.get_a());
    PseudoCustomTypeCpp d = _factory();
    pypp::print(d.get_a());
    _DataClassA e = _DataClassA(a);
    pypp::print(e.pseudo_custom_type.get_a());
    pypp::print(_ConfigClassA.pseudo_custom_type.get_a());
    test_namespace::PseudoACpp f = test_namespace::PseudoACpp(7);
    pypp::print(f.get_a());
    pypp::print(name_only_call_fn_cpp());
    pypp::print(include_only_call_fn());
    pypp::PyTup<int, int> g = pypp::PyTup(1, 2);
    pypp::print(g.get<1>());
    PseudoGeneric<int> h = PseudoGeneric<int>(3);
    h.print_value();
    PseudoGeneric<pypp::PyStr> i = PseudoGeneric<pypp::PyStr>::string_factory();
    i.print_value();
    int j = dc_test::sub_namespace::test_fn();
    pypp::print(j);
    pypp::print(pseudo_fn_a());
    pypp::print(m2::pseudo_fn_b());
    std::cout << "[Custom Print]: " << pypp::PyStr("aloha") << std::endl;
    PseudoCustomList<int> k(pypp::PyList({1, 2, 3}));
    pypp::print(&k);
}

} // namespace me