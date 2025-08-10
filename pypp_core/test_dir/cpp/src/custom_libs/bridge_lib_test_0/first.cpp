#include "custom_libs\bridge_lib_test_0\first.h"
#include "py_str.h"
#include "pypp_bridge_library_test_0/pseudo_a.h"
#include "pypp_bridge_library_test_0/pseudo_custom_type.h"
#include "pypp_util/print.h"

void _as_arg(PseudoCustomTypeCpp &arg) { print(arg.get_a()); }

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

struct _PseudoPyppName_ConfigClassA {
    PseudoCustomTypeCpp pseudo_custom_type = PseudoCustomTypeCpp(1);
};
inline _PseudoPyppName_ConfigClassA _ConfigClassA;

void bridge_lib_test_0_fn() {
    print(PyStr("PYPP BRIDGE LIB TEST 0 RESULTS:"));
    PseudoCustomTypeCpp a = PseudoCustomTypeCpp(42);
    int b = a.get_a();
    print(b);
    _as_arg(a);
    _ClassA c = _ClassA(a);
    print(c.get_a());
    PseudoCustomTypeCpp d = _factory();
    print(d.get_a());
    _DataClassA e = _DataClassA(a);
    print(e.pseudo_custom_type.get_a());
    print(_ConfigClassA.pseudo_custom_type.get_a());
    test_namespace::PseudoACpp f = test_namespace::PseudoACpp(7);
    print(f.get_a());
}
