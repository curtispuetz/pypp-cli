#include "inconsistent_behviour\editing_a_reference.h"
#include "pypp_util/print.h"

void editing_a_reference_fn() {
    PyList<int> a = PyList({1, 2, 3});
    PyList<int> b = a;
    b.append(4);
    print(a);
    PyList<int> c = PyList({1, 2, 3});
    PyList<int> d = update_and_return_new(c);
    d[-1] = 99;
    print(c);
}
PyList<int> update_and_return_new(PyList<int> &l1) {
    l1.append(4);
    return l1;
}