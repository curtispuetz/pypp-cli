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
    for (const auto &pypp_hardcoded_it_tup :
         PyZip(PyReversed(PyList({1, 2, 3})), PyReversed(PyStr("abc")))) {
        auto &x = pypp_hardcoded_it_tup.get<0>();
        auto &z = pypp_hardcoded_it_tup.get<1>();
        print(PyStr(std::format("{}, {}", x, z)));
    }
    PyReversed<PyList<int>> c = PyReversed(PyList({1, 2, 3}));
    for (const auto &x : c) {
        a.append(x);
    }
    print(a);
}