#include "tuples\exceptions.h"

void tuple_exceptions_fn() {
    PyStr("TUPLE EXCEPTIONS RESULTS:").print();
    PyTup<int, double, PyStr> a = PyTup(2, 2.2, PyStr("b"));
    try {
        a.index(1);
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("value error: ") + to_pystr(e)).print();
    }
}