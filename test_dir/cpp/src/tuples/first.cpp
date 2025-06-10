#include "tuples\first.h"

void tuples_fn() {
    PyTup<int, double, PyStr> a = PyTup(1, 1.2, PyStr("a"));
    to_pystr(a.count(2)).print();
    to_pystr(a.index(1.2)).print();
    int b = a.get<0>();
    to_pystr(b).print();
    to_pystr(PyTup(1, 2) == PyTup(1, 2)).print();
    to_pystr(PyTup(1, 2) != PyTup(1, 2)).print();
    to_pystr(PyTup(1, 2) < PyTup(1, 2)).print();
    to_pystr(PyTup(1, 2) <= PyTup(1, 2)).print();
    to_pystr(PyTup(1, 2) > PyTup(1, 2)).print();
    to_pystr(PyTup(1, 2) >= PyTup(1, 2)).print();
    PyTup(1, 2).print();
    PyTup(1, 2, PyStr("a")).print();
    to_pystr(PyTup(1, 2).len()).print();
}