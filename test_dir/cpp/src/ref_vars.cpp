#include "ref_vars.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

void ref_vars_fn() {
    print(PyStr("REF VARS RESULTS:"));
    PyList<PyList<int>> a = PyList({PyList({1, 2}), PyList({3, 4})});
    print(a);
    PyList<int> b = a[0];
    b.append(5);
    print(PyStr("Python and C++ should print different results:"));
    print(a);
    PyList<PyList<int>> c = PyList({PyList({1, 2}), PyList({3, 4})});
    PyList<int> &d = c[0];
    d.append(5);
    print(PyStr("Python and C++ should print the same results:"));
    print(c);
}