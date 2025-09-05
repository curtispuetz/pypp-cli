#include "inconsistent_behviour/editing_a_reference.h"
#include "py_str.h"
#include "pypp_util/print.h"

void editing_a_reference_fn() {
    print(PyStr("INCONSISTENT BEHAVIOR RESULTS:"));
    PyList<int> a({1, 2, 3});
    PyList<int> b = a;
    b.append(4);
    print(PyStr(std::format("inconsistent behavior: {}", a)));
    PyList<int> c({1, 2, 3});
    PyList<int> d = update_and_return_new(c);
    d[-1] = 99;
    print(PyStr(std::format("inconsistent behavior: {}", c)));
}

PyList<int> update_and_return_new(PyList<int> &l1) {
    l1.append(4);
    return l1;
}
