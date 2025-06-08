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
    to_pystr(b).print();
    b = 20;
    to_pystr(b).print();
    a.print();
    to_pystr(a.len()).print();
    a.reverse();
    a.print();
    to_pystr(a.count(2)).print();
    to_pystr(a.index(2)).print();
    a.remove(2);
    a.print();
    a.insert(4, 2);
    a.print();
    int popped_val = a.pop();
    to_pystr(popped_val).print();
    a.print();
    int popped_val2 = a.pop(1);
    to_pystr(popped_val2).print();
    a.print();
    a.clear();
    a.print();
}