#include "slices/first.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "slice/creators.h"
#include "slice/py_slice.h"

void slices_fn() {
    print(PyStr("SLICE RESULTS:"));
    print(py_slice(2));
    print(py_slice(1, 5));
    print(py_slice(1, 5, -2));
    print(py_slice(1, 5, 1));
    print(py_slice(0, 5, 1));
    PyList<int> a = PyList({1, 2, 3, 4, 5});
    PyStr s = PyStr("12345");
    PySlice b = py_slice(2);
    print(a[b]);
    print(a[py_slice(0, 2, 1)]);
    print(s[b]);
    print(s[py_slice(0, 2, 1)]);
    PySlice c = py_slice(1, 4);
    print(a[c]);
    print(a[py_slice(1, 4, 1)]);
    print(s[c]);
    print(s[py_slice(1, 4, 1)]);
    PySlice d = py_slice(4, 1, -1);
    print(a[d]);
    print(a[py_slice(4, 1, -1)]);
    print(s[d]);
    print(s[py_slice(4, 1, -1)]);
    PySlice e = py_slice(0, 100, 2);
    print(a[e]);
    print(a[py_slice(0, std::nullopt, 2)]);
    print(s[e]);
    print(s[py_slice(0, std::nullopt, 2)]);
    PySlice f = py_slice(2, 100);
    print(a[f]);
    print(a[py_slice(2, std::nullopt, 1)]);
    print(s[f]);
    print(s[py_slice(2, std::nullopt, 1)]);
    PySlice g = py_slice(2, 100, 2);
    print(a[g]);
    print(a[py_slice(2, std::nullopt, 2)]);
    print(s[g]);
    print(s[py_slice(2, std::nullopt, 2)]);
    PySet<PySlice> h = PySet({e, g});
    print(h);
}
