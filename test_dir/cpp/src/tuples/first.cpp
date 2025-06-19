#include "tuples\first.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <any>

void tuples_fn() {
    print(PyStr("TUPLE RESULTS:"));
    PyTup<int, double, PyStr> a = PyTup(1, 1.2, PyStr("a"));
    print(to_pystr(a.count(2)));
    print(to_pystr(a.index(1.2)));
    int b = a.get<0>();
    print(to_pystr(b));
    print(to_pystr(PyTup(1, 2) == PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) != PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) < PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) <= PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) > PyTup(1, 2)));
    print(to_pystr(PyTup(1, 2) >= PyTup(1, 2)));
    print(PyTup(1, 2));
    print(PyTup(1, 2, PyStr("a")));
    print(to_pystr(PyTup(1, 2).len()));
    _inline_tuple(PyTup(1.2, PyStr("z")));
}
void _inline_tuple(const PyTup<double, PyStr> &tup) { print(tup); }