#include "lists/as_arg.h"
#include "compy_util/print.h"

void list_as_arg(PyList<int> &a) {
    PyList<int> b = a * 2;
    print(b);
}

void list_as_mutable_arg(PyList<int> &a) {
    a *= 3;
    print(a);
}
