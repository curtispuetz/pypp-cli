#include "dicts\first.h"

void dict_fn() {
    PyStr("DICT RESULTS:").print();
    PyDict<int, PyStr> a({{0, PyStr("a")}, {1, PyStr("b")}, {2, PyStr("c")}});
    a.print();
    a[0].print();
    PyStr default_v = a.get(-1, PyStr("default value"));
    default_v.print();
    PyppOpt<PyStr> b = a.dg_opt(1);
    if (b.has_value()) {
        b.value().print();
    }
    PyppOpt<PyStr> c = a.dg_opt(-1);
    if (!c.has_value()) {
        PyStr("no value").print();
    }
    c.value_or(PyStr("no value from value_or")).print();
    a[3] = PyStr("d");
    a.print();
    PyStr val = a.setdefault(4, PyStr("e"));
    val.print();
    a.print();
    val = a.setdefault(4, PyStr("f"));
    val.print();
    a.print();
    a.keys().print();
    a.values().print();
    PyDict<int, PyList<int>> d(
        {{0, PyList({1, 2, 3})}, {1, PyList({4, 5, 6})}});
    d.print();
    d.clear();
    d[0] = PyList({1});
    d.print();
    a.update({{4, PyStr("z")}, {5, PyStr("x")}});
    a.print();
    PyStr pop_val = a.pop(1);
    pop_val.print();
    a.print();
    pop_val = a.pop(10, PyStr("default value"));
    pop_val.print();
    a.print();
    to_pystr(a.len()).print();
    to_pystr(a.contains(5)).print();
    PyDict<int, PyStr> a_copy(a.copy());
    a.pop(0);
    a_copy.print();
    a.print();
    _fn_dict_arg({{0, 1}, {1, 2}});
    PyDict<int, int> e({});
    e.print();
    PyDict<int, PyDict<int, int>> f({{0, {{0, 1}}}, {1, {{0, 1}}}});
    f.print();
    PyDict<int, int> &f0(f[0]);
    f0[99] = 98;
    f.print();
    f[1][77] = 76;
    f.print();
    PyppOpt<PyDict<int, int>> f1 = f.dg_opt(1);
    if (f1.has_value()) {
        f1.value()[9] = 8;
    }
    f.print();
    PyDict<int, int> g({{0, 1}, {1, 2}});
    int g0 = g.dg(1);
    to_pystr(g0).print();
}
void _fn_dict_arg(const PyDict<int, int> &d) { d.print(); }