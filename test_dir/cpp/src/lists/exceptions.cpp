#include "lists\exceptions.h"

void list_exceptions_fn() {
    PyStr("LIST EXCEPTIONS RESULTS:").print();
    PyList<int> a = PyList<int>({});
    try {
        a.pop();
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("index error: ") + to_pystr(e)).print();
    }
    PyList<int> b = PyList({1, 2, 3});
    try {
        b.pop(3);
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("index error: ") + to_pystr(e)).print();
    }
    try {
        b.remove(4);
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("value error: ") + to_pystr(e)).print();
    }
    try {
        b.index(4);
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("value error: ") + to_pystr(e)).print();
    }
    try {
        b[3];
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("index error: ") + to_pystr(e)).print();
    }
}