#include "src/default_dict/create_with_defaults.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
static pypp::PyDict<int, int> _dict_factory_2() { return {{1, 2}, {3, 4}}; }

void default_dict_create_with_defaults() {
    pypp::print(pypp::PyStr("DEFAULT DICT CREATION WITH DEFAULTS RESULTS:"));
    auto a = pypp::PyDefaultDict<int, int>::int_factory({{1, 2}, {3, 4}});
    pypp::print(a);
    auto c =
        pypp::PyDefaultDict<int, double>::float_factory({{1, 2.0}, {3, 4.0}});
    pypp::print(c);
    auto e =
        pypp::PyDefaultDict<int, bool>::bool_factory({{1, true}, {3, false}});
    pypp::print(e);
    auto g = pypp::PyDefaultDict<int, pypp::PyStr>::str_factory(
        {{1, pypp::PyStr("one")}, {3, pypp::PyStr("three")}});
    pypp::print(g);
    auto i = pypp::PyDefaultDict<int, pypp::PyList<int>>::list_factory(
        {{1, pypp::PyList({1})}, {3, pypp::PyList({3})}});
    pypp::print(i);
    auto k = pypp::PyDefaultDict<int, pypp::PyDict<int, int>>::dict_factory(
        {{1, {{1, 2}}}, {3, {{3, 4}}}});
    pypp::print(k);
    auto m = pypp::PyDefaultDict<int, pypp::PySet<int>>::set_factory(
        {{1, pypp::PySet({1})}, {3, pypp::PySet({3})}});
    pypp::print(m);
    auto o =
        pypp::PyDefaultDict<int, int>([]() { return 42; }, {{1, 2}, {3, 4}});
    pypp::print(o);
    auto q = pypp::PyDefaultDict<int, double>([]() { return 3.14; },
                                              {{1, 2.0}, {3, 4.0}});
    pypp::print(q);
    auto s = pypp::PyDefaultDict<int, bool>([]() { return true; },
                                            {{1, true}, {3, false}});
    pypp::print(s);
    auto u = pypp::PyDefaultDict<int, pypp::PyStr>(
        []() { return pypp::PyStr("default"); },
        {{1, pypp::PyStr("one")}, {3, pypp::PyStr("three")}});
    pypp::print(u);
    auto w = pypp::PyDefaultDict<int, pypp::PyList<int>>(
        []() { return pypp::PyList({1, 2, 3}); },
        {{1, pypp::PyList({1})}, {3, pypp::PyList({3})}});
    pypp::print(w);
    auto y = pypp::PyDefaultDict<int, pypp::PyDict<int, int>>(
        _dict_factory_2, {{1, {{1, 2}}}, {3, {{3, 4}}}});
    pypp::print(y);
    auto aa = pypp::PyDefaultDict<int, pypp::PySet<int>>(
        []() { return pypp::PySet({1, 2, 3}); },
        {{1, pypp::PySet({1})}, {3, pypp::PySet({3})}});
    pypp::print(aa);
}

} // namespace me