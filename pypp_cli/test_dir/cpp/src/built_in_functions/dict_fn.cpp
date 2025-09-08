#include "built_in_functions/dict_fn.h"
#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/create/dict.h"
#include "pypp_util/print.h"

namespace me {
void built_in_dict_fn() {
    pypp::print(pypp::PyStr("BUILT-IN DICT FUNCTION RESULTS:"));
    pypp::PyDict<pypp::PyStr, int> a = {{pypp::PyStr("one"), 1},
                                        {pypp::PyStr("two"), 2},
                                        {pypp::PyStr("three"), 3}};
    pypp::PyDict<pypp::PyStr, int> b = pypp::dict(a);
    a[pypp::PyStr("four")] = 4;
    pypp::print(a);
    pypp::print(b);
    pypp::PyDict<pypp::PyStr, int> c = pypp::dict(pypp::PyList(
        {pypp::PyTup(pypp::PyStr("one"), 1), pypp::PyTup(pypp::PyStr("two"), 2),
         pypp::PyTup(pypp::PyStr("three"), 3)}));
    pypp::print(c);
    pypp::PyDict<double, pypp::PyStr> d = pypp::PyDict<double, pypp::PyStr>();
    pypp::print(d);
    auto e = pypp::PyDefaultDict<pypp::PyStr, int>::int_factory(
        {{pypp::PyStr("one"), 1}});
    pypp::PyDict<pypp::PyStr, int> f = pypp::dict(e);
    pypp::print(f);
}

} // namespace me