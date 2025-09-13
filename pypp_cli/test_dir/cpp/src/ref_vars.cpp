#include "ref_vars.h"
#include "py_dict.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
static pypp::PyList<int> &_get_list(pypp::PyList<int> &input_list) {
    return input_list;
}

pypp::PyList<int> &repeat(pypp::PyList<int> &a) {
    a *= 2;
    return a;
}

pypp::PyList<int> repeat_new(pypp::PyList<int> &a) { return a * 2; }

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
    pypp::PyList<int> arr2({1, 2});
    pypp::PyList<int> &arr2_ref = repeat(arr2);
    arr2_ref.append(42);
    pypp::print(arr2);
    pypp::PyList<int> arr3({1, 2});
    pypp::PyList<int> arr_3_copy = repeat(arr3);
    arr_3_copy.append(42);
    pypp::print(arr3);
    pypp::PyList<int> arr4({1, 2});
    pypp::PyList<int> arr4_copy = repeat_new(arr4);
    arr4_copy.append(42);
    pypp::print(arr4);
    pypp::PyList<int> arr5({1, 2});
    pypp::PyList<int> &arr5_ref = arr5;
    arr5_ref.append(42);
    pypp::print(arr5);
}

} // namespace me