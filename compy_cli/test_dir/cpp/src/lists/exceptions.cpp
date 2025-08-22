#include "lists/exceptions.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "exceptions/stdexcept.h"
#include "py_list.h"
#include "py_str.h"
#include <string>

void list_exceptions_fn() {
    print(PyStr("LIST EXCEPTIONS RESULTS:"));
    PyList<int> a = PyList<int>({});
    try {
        a.pop();
    } catch (const CompyIndexError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    PyList<int> b = PyList({1, 2, 3});
    try {
        b.pop(3);
    } catch (const CompyIndexError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    try {
        b.remove(4);
    } catch (const CompyValueError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        b.index(4);
    } catch (const CompyValueError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        b[3];
    } catch (const CompyIndexError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
}
