#include "dicts\exceptions.h"

void dict_exceptions_fn() {
    print(PyStr("DICT EXCEPTIONS RESULTS:"));
    PyDict<int, int> a({{0, 1}, {1, 2}});
    try {
        a.pop(-1);
    } catch (const PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("key error: ") + to_pystr(e));
    }
    try {
        a.dg(-1);
    } catch (const PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("key error: ") + to_pystr(e));
    }
}