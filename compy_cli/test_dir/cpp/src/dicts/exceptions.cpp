#include "dicts/exceptions.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "exceptions/stdexcept.h"
#include "py_dict.h"
#include "py_str.h"
#include <string>

void dict_exceptions_fn() {
    print(PyStr("DICT EXCEPTIONS RESULTS:"));
    PyDict<int, int> a({{0, 1}, {1, 2}});
    try {
        a.pop(-1);
    } catch (const CompyKeyError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("key error: ") + to_pystr(e));
    }
    try {
        a.dg(-1);
    } catch (const CompyKeyError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("key error: ") + to_pystr(e));
    }
}
