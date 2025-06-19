#include "sets\exceptions.h"

void set_exceptions_fn() {
    print(PyStr("SET EXCEPTIONS RESULTS:"));
    PySet<int> a = PySet({1, 2});
    try {
        a.remove(3);
    } catch (const PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("key error: ") + to_pystr(e));
    }
}