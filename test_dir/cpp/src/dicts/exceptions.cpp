#include "dicts\exceptions.h"

void dict_exceptions_fn() {
    PyStr("DICT EXCEPTIONS RESULTS:").print();
    PyDict<int, int> a({{0, 1}, {1, 2}});
    try {
        a.pop(-1);
    } catch (const PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("key error: ") + to_pystr(e)).print();
    }
    try {
        a.dg(-1);
    } catch (const PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("key error: ") + to_pystr(e)).print();
    }
}