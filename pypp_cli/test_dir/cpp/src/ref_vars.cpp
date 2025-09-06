#include "ref_vars.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

pypp::PyList<int> &_get_list(pypp::PyList<int> &input_list) {
    return input_list;
}

void ref_vars_fn() {
    pypp::print(pypp::PyStr("REF VARS RESULTS:"));
    pypp::PyList<pypp::PyList<int>> a(
        {pypp::PyList({1, 2}), pypp::PyList({3, 4})});
    pypp::print(a);
    pypp::PyList<int> b = a[0];
    b.append(5);
    pypp::print(pypp::PyStr("Python and C++ should print different results:"));
    pypp::print(a);
    pypp::PyList<pypp::PyList<int>> c(
        {pypp::PyList({1, 2}), pypp::PyList({3, 4})});
    pypp::PyList<int> &d = c[0];
    d.append(5);
    pypp::print(pypp::PyStr("Python and C++ should print the same results:"));
    pypp::print(c);
    pypp::PyDict<int, pypp::PyList<int>> e = {{0, pypp::PyList({1, 2})},
                                              {1, pypp::PyList({3, 4})}};
    pypp::PyList<int> &f = e[0];
    f.append(5);
    pypp::print(e);
    pypp::PyList<int> original_list({1, 2, 3});
    pypp::PyList<int> &g = _get_list(original_list);
    g.append(4);
    pypp::print(original_list);
}
