#include "strings/exceptions.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include <string>

void string_exceptions_fn() {
    print(PyStr("STRING EXCEPTIONS RESULTS:"));
    PyStr s = PyStr("test");
    try {
        s.index(PyStr("a"));
    } catch (const CompyValueError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        s.rindex(PyStr("a"));
    } catch (const CompyValueError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        s[9];
    } catch (const CompyIndexError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    try {
        s[-9];
    } catch (const CompyIndexError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
}
