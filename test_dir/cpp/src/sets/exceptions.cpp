#include "sets\exceptions.h"
#include "exceptions/stdexcept.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

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