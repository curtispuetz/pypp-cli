#include "sets/exceptions.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "exceptions/stdexcept.h"
#include "py_set.h"
#include "py_str.h"
#include <string>

void set_exceptions_fn() {
    print(PyStr("SET EXCEPTIONS RESULTS:"));
    PySet<int> a = PySet({1, 2});
    try {
        a.remove(3);
    } catch (const CompyKeyError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("key error: ") + to_pystr(e));
    }
}
