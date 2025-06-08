#include "lists\lists.h"

void list_fn() {
    PyList<int> a = {1, 2, 3, 4, 5};
    a.print();
    a[0] = 10;
    a.print();
    a.append(11);
    a.print();
    to_pystr(a[-1]).print();
    int b = a[-1];
    b = 20;
    to_pystr(b).print();
    a.print();
}