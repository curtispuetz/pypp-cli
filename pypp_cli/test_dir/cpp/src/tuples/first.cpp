#include "tuples/first.h"
#include "py_list.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

namespace me {
void _inline_tuple(pypp::PyTup<double, pypp::PyStr> tup) { pypp::print(tup); }

pypp::PyTup<int, double> _get_tup() { return pypp::PyTup(1, 2.0); }

void _argument_unpacking(int a, double b) { pypp::print(a, b); }

void _arg_unpacking_fail(int a, int b, int c) { pypp::print(a, b, c); }

void tuples_fn() {
    pypp::print(pypp::PyStr("TUPLE RESULTS:"));
    pypp::PyTup<int, double, pypp::PyStr> a =
        pypp::PyTup(1, 1.2, pypp::PyStr("a"));
    pypp::print(a.count(2));
    pypp::print(a.index(1.2));
    int b = a.get<0>();
    pypp::print(b);
    pypp::print(pypp::PyTup(1, 2) == pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2) != pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2) < pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2) <= pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2) > pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2) >= pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2));
    pypp::print(pypp::PyTup(1, 2, pypp::PyStr("a")));
    pypp::print(pypp::PyTup(1, 2).len());
    _inline_tuple(pypp::PyTup(1.2, pypp::PyStr("z")));
    auto [x, y, z] = a;
    pypp::print(x, y, z);
    auto [u, v] = _get_tup();
    pypp::print(u, v);
    pypp::PyList<int> c({1, 2, 3});
    pypp::PyTup<int, pypp::PyList<int>> d = pypp::PyTup(1, c);
    pypp::print(d);
    pypp::print(pypp::PyStr("below will be [1, 2, 3] for Python, but [] for "
                            "C++ because the list was moved:"));
    pypp::print(c);
    pypp::PyTup<int, int> e = pypp::PyTup(1, 2);
    if (e.contains(1)) {
        pypp::print(pypp::PyStr("1 in tuple"));
    }
    if (!e.contains(3)) {
        pypp::print(pypp::PyStr("3 not in tuple"));
    }
}

} // namespace me