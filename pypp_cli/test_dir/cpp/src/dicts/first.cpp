#include "dicts/first.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <utility>

namespace me {
void _inline_dict(pypp::PyDict<int, int> d) { pypp::print(d); }

pypp::PyDict<int, int> _get_dict() { return {{0, 1}, {1, 2}}; }

void dict_fn() {
    pypp::print(pypp::PyStr("DICT RESULTS:"));
    pypp::PyDict<int, pypp::PyStr> a = {
        {0, pypp::PyStr("a")}, {1, pypp::PyStr("b")}, {2, pypp::PyStr("c")}};
    pypp::print(a);
    pypp::PyDict<int, pypp::PyStr> a_0 = {};
    pypp::print(a_0);
    pypp::PyDict<int, int> g = {{0, 1}, {1, 2}};
    int g0 = g.dg(1);
    pypp::print(g0);
    pypp::print(a[0]);
    pypp::PyStr default_v = a.get(-1, pypp::PyStr("default value"));
    pypp::print(
        pypp::PyStr(std::format("default value for dict = {}", default_v)));
    a[3] = pypp::PyStr("d");
    pypp::print(a);
    pypp::PyStr val = a.setdefault(4, pypp::PyStr("e"));
    pypp::print(val);
    pypp::print(a);
    val = a.setdefault(4, pypp::PyStr("f"));
    pypp::print(val);
    pypp::print(a);
    int x_key = 99;
    pypp::PyStr x_val = pypp::PyStr("z");
    a[std::move(x_key)] = std::move(x_val);
    pypp::print(a);
    val = a.setdefault(std::move(x_key), std::move(x_val));
    pypp::print(val);
    pypp::print(a.keys());
    pypp::print(a.values());
    pypp::print(a.items());
    pypp::PyDict<int, pypp::PyList<int>> d = {{0, pypp::PyList({1, 2, 3})},
                                              {1, pypp::PyList({4, 5, 6})}};
    pypp::print(d);
    d.clear();
    d[0] = pypp::PyList({1});
    pypp::print(d);
    a.update({{4, pypp::PyStr("z")}, {5, pypp::PyStr("x")}});
    pypp::print(a);
    pypp::PyDict<int, pypp::PyStr> b = {{6, pypp::PyStr("y")},
                                        {7, pypp::PyStr("w")}};
    pypp::PyDict<int, pypp::PyStr> x_dict = {{8, pypp::PyStr("v")},
                                             {9, pypp::PyStr("u")}};
    b.update(std::move(x_dict));
    pypp::print(b);
    pypp::PyStr pop_val = a.pop(1);
    pypp::print(pop_val);
    pypp::print(a);
    pop_val = a.pop(10, pypp::PyStr("default value"));
    pypp::print(pop_val);
    pypp::print(a);
    pypp::print(pypp::to_pystr(a.len()));
    pypp::print(pypp::to_pystr(a.contains(5)));
    pypp::PyDict<int, pypp::PyStr> a_copy = a.copy();
    a.pop(0);
    pypp::print(a_copy);
    pypp::print(a);
    pypp::PyDict<int, int> e = {};
    pypp::print(e);
    pypp::PyDict<int, pypp::PyDict<int, int>> f = {{0, {{0, 1}}},
                                                   {1, {{0, 1}}}};
    pypp::print(f);
    pypp::PyDict<int, int> &f0 = f[0];
    f0[99] = 98;
    pypp::print(f);
    f[1][77] = 76;
    pypp::print(f);
    _inline_dict({{0, 1}, {1, 2}});
    pypp::PyDict<int, int> h = _get_dict();
    pypp::print(h);
}

} // namespace me