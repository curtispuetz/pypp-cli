#include "loops/reversed_.h"
#include "py_list.h"
#include "py_reversed.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <utility>

void reversed_fn() {
    print(PyStr("REVERSED RESULTS:"));
    PyList<int> a({});
    for (const auto &x : PyReversed(PyList({1, 2, 3}))) {
        int y = x;
        a.append(std::move(y));
    }
    print(a);
    PyList<PyStr> b({});
    for (const auto &x : PyReversed(PyStr("abcd"))) {
        PyStr y = x;
        b.append(std::move(y));
    }
    print(b);
    for (const auto &[x, z] :
         PyZip(PyReversed(PyList({1, 2, 3})), PyReversed(PyStr("abc")))) {
        print(PyStr(std::format("{}, {}", x, z)));
    }
}
