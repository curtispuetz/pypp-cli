#include "sets/first.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <utility>

void _inline_set(PySet<double> s) { print(s); }

void set_fn() {
    print(PyStr("SET RESULTS:"));
    PySet<int> a({1, 2, 3});
    print(a);
    a.add(4);
    print(a);
    int add_val = 4;
    a.add(std::move(add_val));
    a.discard(4);
    print(a);
    a.remove(3);
    print(a);
    print(to_pystr(a.contains(1)));
    PySet<int> b({1, 5});
    print(a.union_(b));
    print(a.intersection(b));
    print(a.difference(b));
    print(a.symmetric_difference(b));
    a.update(PySet({6, 7}));
    print(a);
    a.update(PyList({9, 10}));
    print(a);
    a.intersection_update(b);
    print(a);
    a.symmetric_difference_update(b);
    print(a);
    a.difference_update(PySet({6}));
    print(a);
    print(to_pystr(b.len()));
    print(to_pystr(PySet({1, 2}).issubset(PySet({1, 2, 3}))));
    print(to_pystr(PySet({1, 4}).issubset(PySet({1, 2, 3}))));
    print(to_pystr(PySet({1, 2, 3}).issuperset(PySet({1, 2}))));
    print(to_pystr(PySet({1, 4, 3}).issuperset(PySet({1, 2}))));
    print(to_pystr(PySet({1, 2}) == PySet({1, 2})));
    print(to_pystr(PySet({1, 2}) == PySet({1, 2, 3})));
    print(to_pystr(PySet({1, 2}) != PySet({1, 2, 3})));
    print(to_pystr(PySet({1, 2}) != PySet({1, 2})));
    a.clear();
    print(a);
    PyList<PySet<int>> list_of_sets({PySet({1, 2}), PySet({3, 4})});
    print(list_of_sets);
    PySet<int> c({});
    print(c);
    _inline_set(PySet({1.2, 4.4}));
}
