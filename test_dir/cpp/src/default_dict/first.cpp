#include "default_dict\first.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "pypp_util/print.h"
#include <utility>

PyDict<int, int> _dict_factory() { return {{1, 2}, {3, 4}}; }

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
    PyDict<int, int> l(k[0]);
    print(l);
    print(k);
    auto m = PyDefaultDict<int, PySet<int>>::set_factory();
    PySet<int> n = m[0];
    print(n);
    print(m);
    PyDefaultDict<int, int> o([]() { return 42; });
    int p = o[0];
    print(p);
    print(o);
    PyDefaultDict<int, double> q([]() { return 3.14; });
    double r = q[0];
    print(r);
    print(q);
    PyDefaultDict<int, bool> s([]() { return true; });
    bool t = s[0];
    print(t);
    print(s);
    PyDefaultDict<int, PyStr> u([]() { return PyStr("default"); });
    PyStr v = u[0];
    print(v);
    print(u);
    PyDefaultDict<int, PyList<int>> w([]() { return PyList({1, 2, 3}); });
    PyList<int> x = w[0];
    print(x);
    print(w);
    PyDefaultDict<int, PyDict<int, int>> y(_dict_factory);
    PyDict<int, int> z(y[0]);
    print(z);
    print(y);
    PyDefaultDict<int, PySet<int>> aa([]() { return PySet({1, 2, 3}); });
    PySet<int> ab = aa[0];
    print(ab);
    print(aa);
    w[9].append(99);
    print(w);
    PyDefaultDict<int, _CustomType> ac([]() { return _CustomType(42); });
    _CustomType ad = ac[0];
    print(ad.val);
}
