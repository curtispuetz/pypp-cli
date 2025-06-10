#include "dicts\first.h"

void dict_fn() {
    PyDict<int, PyStr> a({{0, PyStr("a")}, {1, PyStr("b")}, {2, PyStr("c")}});
    a.print();
    a[0].print();
    PyStr default_v = a.get(-1, PyStr("default value"));
    default_v.print();
    std::optional<PyStr> b = a.get(1);
    if (b.has_value()) {
        b.value().print();
    }
    std::optional<PyStr> c = a.get(-1);
    if (!c.has_value()) {
        PyStr("no value").print();
    }
    c.value_or(PyStr("no value from value_or")).print();
}