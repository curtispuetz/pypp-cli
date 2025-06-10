#include "sets\first.h"

void set_fn() {
    PySet<int> a = PySet({1, 2, 3});
    a.print();
}