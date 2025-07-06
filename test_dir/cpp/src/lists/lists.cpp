#include "lists\lists.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include "slice/creators.h"
#include <utility>

void _test_fn(PyList<PyStr> arg1) { print(arg1); }
void list_fn() {
    print(PyStr("LIST RESULTS:"));
    PyList<int> a = PyList({1, 2, 3, 4, 5});
    print(a);
    a[0] = 10;
    print(a);
    a.append(11);
    print(a);
    print(to_pystr(a[-1]));
    int b = a[-1];
    print(to_pystr(b));
    b = 20;
    print(to_pystr(b));
    print(a);
    print(to_pystr(a.len()));
    a.reverse();
    print(a);
    print(to_pystr(a.count(2)));
    print(to_pystr(a.index(2)));
    a.remove(2);
    print(a);
    a.insert(4, 2);
    print(a);
    int ins_val = 2;
    a.insert(4, std::move(ins_val));
    print(a);
    int popped_val = a.pop();
    print(to_pystr(popped_val));
    print(a);
    int popped_val2 = a.pop(1);
    print(to_pystr(popped_val2));
    print(a);
    a.clear();
    print(a);
    print(to_pystr(PyList({1, 2}) == PyList({1, 2})));
    print(to_pystr(PyList({1, 2}) < PyList({1, 2})));
    print(to_pystr(PyList({1, 2}) <= PyList({1, 2})));
    print(to_pystr(PyList({1, 2}) > PyList({1, 2})));
    print(to_pystr(PyList({1, 2}) >= PyList({1, 2})));
    print(to_pystr(PyList({1, 2}) != PyList({1, 2})));
    PyList<int> c = PyList({1, 2}) + PyList({3, 4});
    print(c);
    c += PyList({5, 6});
    print(c);
    PyList<int> d = c * 3;
    print(d);
    c *= 3;
    print(c);
    print(c[py_slice(1, 4, 1)]);
    print(c[py_slice(1, c.len() - 1, 2)]);
    print(c[py_slice(1, std::nullopt, 2)]);
    print(c[py_slice(1, std::nullopt, 1)]);
    print(c[py_slice(0, 4, 1)]);
    print(c[py_slice(0, std::nullopt, 2)]);
    print(c[py_slice(0, std::nullopt, 1)]);
    print(c[py_slice(c.len() - 2, 5, 1)]);
    print(c[py_slice(c.len() - 4, c.len() - 1, 1)]);
    print(c[py_slice(5, 1, -1)]);
    PyList<PyStr> e = PyList({PyStr("a"), PyStr("b")});
    print(e);
    PyList<int> f = PyList<int>({});
    print(f);
    PyList<PyList<int>> g = PyList({PyList({1, 2}), PyList({3, 4})});
    PyList<int> g_0 = g[0];
    g_0.append(99);
    print(g);
    g[1].append(98);
    print(g);
    _test_fn(PyList({PyStr("1"), PyStr("2")}));
}