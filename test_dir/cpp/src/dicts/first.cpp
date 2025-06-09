#include "dicts\first.h"

void dict_fn() {
    PyDict<int, PyStr> a({{0, PyStr("a")}, {1, PyStr("b")}, {2, PyStr("c")}});
    a.print();
}