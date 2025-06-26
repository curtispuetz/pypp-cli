#include "loops\reversed_.h"
#include "py_list.h"
#include "py_reversed.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"

void reversed_fn() {
    print(PyStr("REVERSED RESULTS:"));
    PyList<int> a = PyList<int>({});
    for (const auto &x : PyReversed(PyList({1, 2, 3}))) {
        a.append(x);
    }
    print(a);
    PyList<PyStr> b = PyList<PyStr>({});
    for (const auto &x : PyReversed(PyStr("abcd"))) {
        b.append(x);
    }
    print(b);
    for (const auto &[x, z] :
         PyZip(PyReversed(PyList({1, 2, 3})), PyReversed(PyStr("abc")))) {
        print(PyStr(std::format("{}, {}", x, z)));
    }
}