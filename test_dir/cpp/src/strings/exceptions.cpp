#include "strings\exceptions.h"

void string_exceptions_fn() {
    PyStr("STRING EXCEPTIONS RESULTS:").print();
    PyStr s = PyStr("test");
    try {
        s.index(PyStr("a"));
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("value error: ") + to_pystr(e)).print();
    }
    try {
        s.rindex(PyStr("a"));
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("value error: ") + to_pystr(e)).print();
    }
    try {
        s[9];
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("index error: ") + to_pystr(e)).print();
    }
    try {
        s[-9];
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("index error: ") + to_pystr(e)).print();
    }
}