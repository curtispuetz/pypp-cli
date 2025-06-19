#include "strings\exceptions.h"

void string_exceptions_fn() {
    print(PyStr("STRING EXCEPTIONS RESULTS:"));
    PyStr s = PyStr("test");
    try {
        s.index(PyStr("a"));
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        s.rindex(PyStr("a"));
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        s[9];
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    try {
        s[-9];
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
}