#include "built_in_functions/list_fn.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/create/list.h"
#include "pypp_util/print.h"

namespace me {
void built_in_list_fn() {
    pypp::print(pypp::PyStr("BUILT-IN LIST FUNCTION RESULTS:"));
    pypp::PyList<int> a({1, 2, 3});
    pypp::PyList<int> b = pypp::list(a);
    a.append(4);
    pypp::print(a);
    pypp::print(b);
    pypp::PyList<int> c = pypp::list(pypp::PySet({1, 2, 3}));
    pypp::print(c);
    pypp::PyList<pypp::PyStr> d = pypp::list(pypp::PyStr("hello"));
    pypp::print(d);
    pypp::PyDict<pypp::PyStr, int> e = {{pypp::PyStr("one"), 1},
                                        {pypp::PyStr("two"), 2}};
    pypp::PyList<pypp::PyStr> f = pypp::list(e);
    pypp::print(f);
    pypp::PyList<pypp::PyStr> g = pypp::PyList<pypp::PyStr>();
    pypp::print(g);
    auto h = pypp::PyDefaultDict<int, pypp::PyStr>::str_factory(
        {{1, pypp::PyStr("one")}});
    pypp::PyList<int> i = pypp::list(h);
    pypp::print(i);
}

} // namespace me