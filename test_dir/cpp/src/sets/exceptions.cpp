#include "sets\exceptions.h"

void set_exceptions_fn() {
    PyStr("SET EXCEPTIONS RESULTS:").print();
    PySet<int> a = PySet({1, 2});
    try {
        a.remove(3);
    } catch (const PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("key error: ") + to_pystr(e)).print();
    }
}