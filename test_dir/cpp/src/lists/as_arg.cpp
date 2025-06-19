#include "lists\as_arg.h"

void list_as_arg(const PyList<int> &a) {
    PyList<int> b = a * 2;
    print(b);
}
void list_as_mutable_arg(PyList<int> &a) {
    a *= 3;
    print(a);
}