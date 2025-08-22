#include "dicts/first.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_str.h"
#include <utility>

void _inline_dict(PyDict<int, int> d) { print(d); }

PyDict<int, int> _get_dict() { return {{0, 1}, {1, 2}}; }

void dict_fn() {
    print(PyStr("DICT RESULTS:"));
    PyDict<int, PyStr> a({{0, PyStr("a")}, {1, PyStr("b")}, {2, PyStr("c")}});
    print(a);
    PyDict<int, int> g({{0, 1}, {1, 2}});
    int g0 = g.dg(1);
    print(g0);
    print(a[0]);
    a[3] = PyStr("d");
    print(a);
    PyStr val = a.setdefault(4, PyStr("e"));
    print(val);
    print(a);
    val = a.setdefault(4, PyStr("f"));
    print(val);
    print(a);
    int x_key = 99;
    PyStr x_val = PyStr("z");
    a[std::move(x_key)] = std::move(x_val);
    print(a);
    val = a.setdefault(std::move(x_key), std::move(x_val));
    print(val);
    print(a.keys());
    print(a.values());
    print(a.items());
    PyDict<int, PyList<int>> d(
        {{0, PyList({1, 2, 3})}, {1, PyList({4, 5, 6})}});
    print(d);
    d.clear();
    d[0] = PyList({1});
    print(d);
    a.update({{4, PyStr("z")}, {5, PyStr("x")}});
    print(a);
    PyDict<int, PyStr> b({{6, PyStr("y")}, {7, PyStr("w")}});
    PyDict<int, PyStr> x_dict({{8, PyStr("v")}, {9, PyStr("u")}});
    b.update(std::move(x_dict));
    print(b);
    PyStr pop_val = a.pop(1);
    print(pop_val);
    print(a);
    pop_val = a.pop(10, PyStr("default value"));
    print(pop_val);
    print(a);
    print(to_pystr(a.len()));
    print(to_pystr(a.contains(5)));
    PyDict<int, PyStr> a_copy(a.copy());
    a.pop(0);
    print(a_copy);
    print(a);
    PyDict<int, int> e({});
    print(e);
    PyDict<int, PyDict<int, int>> f({{0, {{0, 1}}}, {1, {{0, 1}}}});
    print(f);
    PyDict<int, int> &f0 = f[0];
    f0[99] = 98;
    print(f);
    f[1][77] = 76;
    print(f);
    _inline_dict({{0, 1}, {1, 2}});
    PyDict<int, int> h(_get_dict());
    print(h);
}
