#include "default_dict/first.h"
#include "compy_util/print.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include <utility>

PyDict<int, int> _dict_factory() { return {{1, 2}, {3, 4}}; }

void _default_dict_as_arg(PyDefaultDict<int, int> a) { print(a[0]); }

struct _CustomType {
    int val;
    _CustomType(int a_val) : val(std::move(a_val)) {}
};

void default_dict_fn() {
    print(PyStr("DEFAULT DICT RESULTS:"));
    auto a = PyDefaultDict<int, int>::int_factory();
    int b = a[0];
    print(b);
    print(a);
    auto c = PyDefaultDict<int, double>::float_factory();
    double d = c[0];
    print(d);
    print(c);
    auto e = PyDefaultDict<int, bool>::bool_factory();
    bool f = e[0];
    print(f);
    print(e);
    auto g = PyDefaultDict<int, PyStr>::str_factory();
    PyStr h = g[0];
    print(h);
    print(g);
    auto i = PyDefaultDict<int, PyList<int>>::list_factory();
    PyList<int> j = i[0];
    print(j);
    print(i);
    auto k = PyDefaultDict<int, PyDict<int, int>>::dict_factory();
    PyDict<int, int> l = k[0];
    print(l);
    print(k);
    auto m = PyDefaultDict<int, PySet<int>>::set_factory();
    PySet<int> n = m[0];
    print(n);
    print(m);
    auto o = PyDefaultDict<int, int>([]() { return 42; });
    int p = o[0];
    print(p);
    print(o);
    auto q = PyDefaultDict<int, double>([]() { return 3.14; });
    double r = q[0];
    print(r);
    print(q);
    auto s = PyDefaultDict<int, bool>([]() { return true; });
    bool t = s[0];
    print(t);
    print(s);
    auto u = PyDefaultDict<int, PyStr>([]() { return PyStr("default"); });
    PyStr v = u[0];
    print(v);
    print(u);
    auto w =
        PyDefaultDict<int, PyList<int>>([]() { return PyList({1, 2, 3}); });
    PyList<int> x = w[0];
    print(x);
    print(w);
    auto y = PyDefaultDict<int, PyDict<int, int>>(_dict_factory);
    PyDict<int, int> z = y[0];
    print(z);
    print(y);
    auto aa = PyDefaultDict<int, PySet<int>>([]() { return PySet({1, 2, 3}); });
    PySet<int> ab = aa[0];
    print(ab);
    print(aa);
    w[9].append(99);
    print(w);
    auto ac = PyDefaultDict<int, _CustomType>([]() { return _CustomType(42); });
    _CustomType ad = ac[0];
    print(ad.val);
    print(&ad);
    _default_dict_as_arg(PyDefaultDict<int, int>::int_factory());
}
