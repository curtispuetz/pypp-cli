#include "slices\first.h"
#include "py_list.h"
#include "py_set.h"
#include "py_slice.h"
#include "py_str.h"
#include "pypp_util/print.h"

void slices_fn() {
    print(PyStr("SLICE RESULTS:"));
    print(PySlice(2));
    print(PySlice(1, 5));
    print(PySlice(1, 5, -2));
    print(PySlice(1, 5, 1));
    print(PySlice(0, 5, 1));
    PyList<int> a = PyList({1, 2, 3, 4, 5});
    PyStr s = PyStr("12345");
    PySlice b = PySlice(2);
    print(a[b]);
    print(a[PySlice(0, 2, 1)]);
    print(s[b]);
    print(s[PySlice(0, 2, 1)]);
    PySlice c = PySlice(1, 4);
    print(a[c]);
    print(a[PySlice(1, 4, 1)]);
    print(s[c]);
    print(s[PySlice(1, 4, 1)]);
    PySlice d = PySlice(4, 1, -1);
    print(a[d]);
    print(a[PySlice(4, 1, -1)]);
    print(s[d]);
    print(s[PySlice(4, 1, -1)]);
    PySlice e = PySlice(0, 100, 2);
    print(a[e]);
    print(a[PySlice(0, std::nullopt, 2)]);
    print(s[e]);
    print(s[PySlice(0, std::nullopt, 2)]);
    PySlice f = PySlice(2, 100);
    print(a[f]);
    print(a[PySlice(2, std::nullopt, 1)]);
    print(s[f]);
    print(s[PySlice(2, std::nullopt, 1)]);
    PySlice g = PySlice(2, 100, 2);
    print(a[g]);
    print(a[PySlice(2, std::nullopt, 2)]);
    print(s[g]);
    print(s[PySlice(2, std::nullopt, 2)]);
    PySet<PySlice> h = PySet({e, g});
    print(h);
}