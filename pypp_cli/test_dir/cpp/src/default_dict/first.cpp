#include "default_dict/first.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

pypp::PyDict<int, int> _dict_factory() { return {{1, 2}, {3, 4}}; }

void _default_dict_as_arg(pypp::PyDefaultDict<int, int> a) {
    pypp::print(a[0]);
}

struct _CustomType {
    int val;
    _CustomType(int a_val) : val(std::move(a_val)) {}
};

void default_dict_fn() {
    pypp::print(pypp::PyStr("DEFAULT DICT RESULTS:"));
    auto a = pypp::PyDefaultDict<int, int>::int_factory();
    int b = a[0];
    pypp::print(b);
    pypp::print(a);
    auto c = pypp::PyDefaultDict<int, double>::float_factory();
    double d = c[0];
    pypp::print(d);
    pypp::print(c);
    auto e = pypp::PyDefaultDict<int, bool>::bool_factory();
    bool f = e[0];
    pypp::print(f);
    pypp::print(e);
    auto g = pypp::PyDefaultDict<int, pypp::PyStr>::str_factory();
    pypp::PyStr h = g[0];
    pypp::print(h);
    pypp::print(g);
    auto i = pypp::PyDefaultDict<int, pypp::PyList<int>>::list_factory();
    pypp::PyList<int> j = i[0];
    pypp::print(j);
    pypp::print(i);
    auto k = pypp::PyDefaultDict<int, pypp::PyDict<int, int>>::dict_factory();
    pypp::PyDict<int, int> l = k[0];
    pypp::print(l);
    pypp::print(k);
    auto m = pypp::PyDefaultDict<int, pypp::PySet<int>>::set_factory();
    pypp::PySet<int> n = m[0];
    pypp::print(n);
    pypp::print(m);
    auto o = pypp::PyDefaultDict<int, int>([]() { return 42; });
    int p = o[0];
    pypp::print(p);
    pypp::print(o);
    auto q = pypp::PyDefaultDict<int, double>([]() { return 3.14; });
    double r = q[0];
    pypp::print(r);
    pypp::print(q);
    auto s = pypp::PyDefaultDict<int, bool>([]() { return true; });
    bool t = s[0];
    pypp::print(t);
    pypp::print(s);
    auto u = pypp::PyDefaultDict<int, pypp::PyStr>(
        []() { return pypp::PyStr("default"); });
    pypp::PyStr v = u[0];
    pypp::print(v);
    pypp::print(u);
    auto w = pypp::PyDefaultDict<int, pypp::PyList<int>>(
        []() { return pypp::PyList({1, 2, 3}); });
    pypp::PyList<int> x = w[0];
    pypp::print(x);
    pypp::print(w);
    auto y = pypp::PyDefaultDict<int, pypp::PyDict<int, int>>(_dict_factory);
    pypp::PyDict<int, int> z = y[0];
    pypp::print(z);
    pypp::print(y);
    auto aa = pypp::PyDefaultDict<int, pypp::PySet<int>>(
        []() { return pypp::PySet({1, 2, 3}); });
    pypp::PySet<int> ab = aa[0];
    pypp::print(ab);
    pypp::print(aa);
    w[9].append(99);
    pypp::print(w);
    auto ac =
        pypp::PyDefaultDict<int, _CustomType>([]() { return _CustomType(42); });
    _CustomType ad = ac[0];
    pypp::print(ad.val);
    pypp::print(&ad);
    _default_dict_as_arg(pypp::PyDefaultDict<int, int>::int_factory());
}
