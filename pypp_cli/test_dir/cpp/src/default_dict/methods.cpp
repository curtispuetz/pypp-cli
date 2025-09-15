#include "src/default_dict/methods.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void default_dict_methods_fn() {
    pypp::print(pypp::PyStr("DEFAULT DICT METHODS RESULTS:"));
    auto a = pypp::PyDefaultDict<int, pypp::PyStr>::str_factory();
    a.update({{1, pypp::PyStr("one")},
              {2, pypp::PyStr("two")},
              {3, pypp::PyStr("three")}});
    pypp::print(a.get(4, pypp::PyStr("four")));
    pypp::print(a);
    pypp::print(a.setdefault(5, pypp::PyStr("five")));
    pypp::print(a);
    pypp::print(a.pop(2));
    pypp::print(a);
    pypp::print(a.keys());
    pypp::print(a.values());
    pypp::print(a.items());
    a.clear();
    pypp::print(a);
    a.update({{1, pypp::PyStr("one")},
              {2, pypp::PyStr("two")},
              {3, pypp::PyStr("three")}});
    auto b = a.copy();
    a[4] = pypp::PyStr("four");
    pypp::print(pypp::PyStr(
        std::format("original: {}, default dict after copy: {}", a, b)));
    auto c = pypp::PyDefaultDict<int, int>::int_factory({{1, 2}, {3, 4}});
    pypp::print(c);
    auto d = pypp::PyDefaultDict<int, pypp::PyList<pypp::PyStr>>::list_factory(
        {{1, pypp::PyList({pypp::PyStr("one"), pypp::PyStr("uno")})},
         {2, pypp::PyList({pypp::PyStr("two"), pypp::PyStr("dos")})}});
    pypp::print(d);
}

} // namespace me