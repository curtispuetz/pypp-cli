#include "dicts\first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"

void dict_fn() {
    print(PyStr("DICT RESULTS:"));
    PyDict<int, PyStr> a({{0, PyStr("a")}, {1, PyStr("b")}, {2, PyStr("c")}});
    print(a);
    PyDict<int, int> g({{0, 1}, {1, 2}});
    int g0 = g.dg(1);
    print(to_pystr(g0));
    print(a[0]);
    PyStr default_v = a.get(-1, PyStr("default value"));
    print(default_v);
    a[3] = PyStr("d");
    print(a);
    PyStr val = a.setdefault(4, PyStr("e"));
    print(val);
    print(a);
    val = a.setdefault(4, PyStr("f"));
    print(val);
    print(a);
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
    PyDict<int, int> &f0(f[0]);
    f0[99] = 98;
    print(f);
    f[1][77] = 76;
    print(f);
    _inline_dict({{0, 1}, {1, 2}});
}
void _inline_dict(const PyDict<int, int> &d) { print(d); }