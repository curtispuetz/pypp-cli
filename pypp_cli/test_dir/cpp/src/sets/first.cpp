#include "sets/first.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <utility>

namespace me {
void _inline_set(pypp::PySet<double> s) { pypp::print(s); }

void set_fn() {
    pypp::print(pypp::PyStr("SET RESULTS:"));
    pypp::PySet<int> a({1, 2, 3});
    pypp::print(a);
    pypp::PySet<int> c({});
    pypp::print(c);
    a.add(4);
    pypp::print(a);
    int add_val = 4;
    a.add(std::move(add_val));
    a.discard(4);
    pypp::print(a);
    a.remove(3);
    pypp::print(a);
    pypp::print(pypp::to_pystr(a.contains(1)));
    pypp::PySet<int> b({1, 5});
    pypp::print(a.union_(b));
    pypp::print(a.intersection(b));
    pypp::print(a.difference(b));
    pypp::print(a.symmetric_difference(b));
    a.update(pypp::PySet({6, 7}));
    pypp::print(a);
    a.update(pypp::PyList({9, 10}));
    pypp::print(a);
    a.intersection_update(b);
    pypp::print(a);
    a.symmetric_difference_update(b);
    pypp::print(a);
    a.difference_update(pypp::PySet({6}));
    pypp::print(a);
    pypp::print(pypp::to_pystr(b.len()));
    pypp::print(
        pypp::to_pystr(pypp::PySet({1, 2}).issubset(pypp::PySet({1, 2, 3}))));
    pypp::print(
        pypp::to_pystr(pypp::PySet({1, 4}).issubset(pypp::PySet({1, 2, 3}))));
    pypp::print(
        pypp::to_pystr(pypp::PySet({1, 2, 3}).issuperset(pypp::PySet({1, 2}))));
    pypp::print(
        pypp::to_pystr(pypp::PySet({1, 4, 3}).issuperset(pypp::PySet({1, 2}))));
    pypp::print(pypp::to_pystr(pypp::PySet({1, 2}) == pypp::PySet({1, 2})));
    pypp::print(pypp::to_pystr(pypp::PySet({1, 2}) == pypp::PySet({1, 2, 3})));
    pypp::print(pypp::to_pystr(pypp::PySet({1, 2}) != pypp::PySet({1, 2, 3})));
    pypp::print(pypp::to_pystr(pypp::PySet({1, 2}) != pypp::PySet({1, 2})));
    a.clear();
    pypp::print(a);
    pypp::PyList<pypp::PySet<int>> list_of_sets(
        {pypp::PySet({1, 2}), pypp::PySet({3, 4})});
    pypp::print(list_of_sets);
    _inline_set(pypp::PySet({1.2, 4.4}));
}

} // namespace me