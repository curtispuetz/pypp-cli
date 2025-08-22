#include "lists/ownership.h"
#include "compy_util/print.h"
#include "py_list.h"
#include "py_str.h"
#include <utility>

class _PrivateClass {
  public:
    int _v;
    _PrivateClass(int a_v) : _v(std::move(a_v)) {}
    int m() { return _v; }
};

PyList<PyStr> _calc_list() {
    PyStr a = PyStr("a");
    return PyList({a, PyStr("b"), PyStr("c")});
}

PyList<_PrivateClass> _calc_obj_list() {
    _PrivateClass a = _PrivateClass(1);
    return PyList({a, _PrivateClass(2), _PrivateClass(3)});
}

void list_ownership_tests_fn() {
    print(PyStr("LIST OWNERSHIP TESTS RESULTS:"));
    PyList<PyStr> a = _calc_list();
    print(a);
    PyStr b = PyStr("d");
    a.append(std::move(b));
    print(a);
    PyList<_PrivateClass> c = _calc_obj_list();
    print(&c);
}
