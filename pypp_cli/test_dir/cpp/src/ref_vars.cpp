#include "ref_vars.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

PyList<int> &_get_list(PyList<int> &input_list) { return input_list; }

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
    PyDict<int, PyList<int>> e = {{0, PyList({1, 2})}, {1, PyList({3, 4})}};
    PyList<int> &f = e[0];
    f.append(5);
    print(e);
    PyList<int> original_list = PyList({1, 2, 3});
    PyList<int> &g = _get_list(original_list);
    g.append(4);
    print(original_list);
}
