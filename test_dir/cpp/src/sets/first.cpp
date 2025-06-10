#include "sets\first.h"

void set_fn() {
    PySet<int> a = PySet({1, 2, 3});
    a.print();
    a.add(4);
    a.print();
    a.discard(4);
    a.print();
    a.discard(3);
    a.print();
    to_pystr(a.contains(1)).print();
    PySet<int> b = PySet({1, 5});
    a.union_(b).print();
    a.intersection(b).print();
    a.difference(b).print();
    a.symmetric_difference(b).print();
    a.update(PySet({6, 7}));
    a.print();
    a.update(PyList({9, 10}));
    a.print();
    a.intersection_update(b);
    a.print();
    a.symmetric_difference_update(b);
    a.print();
    a.difference_update(PySet({6}));
    a.print();
    to_pystr(b.len()).print();
    to_pystr(PySet({1, 2}).issubset(PySet({1, 2, 3}))).print();
    to_pystr(PySet({1, 4}).issubset(PySet({1, 2, 3}))).print();
    to_pystr(PySet({1, 2, 3}).issuperset(PySet({1, 2}))).print();
    to_pystr(PySet({1, 4, 3}).issuperset(PySet({1, 2}))).print();
    to_pystr(PySet({1, 2}) == PySet({1, 2})).print();
    to_pystr(PySet({1, 2}) == PySet({1, 2, 3})).print();
    to_pystr(PySet({1, 2}) != PySet({1, 2, 3})).print();
    to_pystr(PySet({1, 2}) != PySet({1, 2})).print();
    a.clear();
    a.print();
    PyList<PySet<int>> list_of_sets = PyList({PySet({1, 2}), PySet({3, 4})});
    list_of_sets.print();
}