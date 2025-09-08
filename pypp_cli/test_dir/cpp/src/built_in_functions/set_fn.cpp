#include "built_in_functions/set_fn.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/create/set.h"
#include "pypp_util/print.h"

namespace me {
void built_in_set_fn() {
    pypp::print(pypp::PyStr("BUILT-IN set FUNCTION RESULTS:"));
    pypp::PySet<int> a({1, 2, 3});
    pypp::PySet<int> b = pypp::set(a);
    a.add(4);
    pypp::print(a);
    pypp::print(b);
    pypp::PySet<int> c = pypp::set(pypp::PyList({1, 2, 3}));
    pypp::print(c);
    pypp::PySet<pypp::PyStr> d = pypp::set(pypp::PyStr("hello"));
    pypp::print(d);
    pypp::PyDict<pypp::PyStr, int> e = {{pypp::PyStr("one"), 1},
                                        {pypp::PyStr("two"), 2}};
    pypp::PySet<pypp::PyStr> f = pypp::set(e);
    pypp::print(f);
    pypp::PySet<pypp::PyStr> g = pypp::PySet<pypp::PyStr>();
    pypp::print(g);
    auto h = pypp::PyDefaultDict<int, pypp::PyStr>::str_factory(
        {{1, pypp::PyStr("one")}});
    pypp::PySet<int> i = pypp::set(h);
    pypp::print(i);
}

} // namespace me