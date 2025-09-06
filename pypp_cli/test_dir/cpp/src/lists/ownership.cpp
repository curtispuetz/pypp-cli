#include "lists/ownership.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

class _PrivateClass {
  public:
    int _v;
    _PrivateClass(int a_v) : _v(std::move(a_v)) {}
    int m() { return _v; }
};

pypp::PyList<pypp::PyStr> _calc_list() {
    pypp::PyStr a = pypp::PyStr("a");
    return pypp::PyList({a, pypp::PyStr("b"), pypp::PyStr("c")});
}

pypp::PyList<_PrivateClass> _calc_obj_list() {
    _PrivateClass a = _PrivateClass(1);
    return pypp::PyList({a, _PrivateClass(2), _PrivateClass(3)});
}

void list_ownership_tests_fn() {
    pypp::print(pypp::PyStr("LIST OWNERSHIP TESTS RESULTS:"));
    pypp::PyList<pypp::PyStr> a = _calc_list();
    pypp::print(a);
    pypp::PyStr b = pypp::PyStr("d");
    a.append(std::move(b));
    pypp::print(a);
    pypp::PyList<_PrivateClass> c = _calc_obj_list();
    pypp::print(&c);
}
