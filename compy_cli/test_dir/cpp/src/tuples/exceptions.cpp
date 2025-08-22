#include "tuples/exceptions.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "py_tuple.h"
#include <string>

void tuple_exceptions_fn() {
    print(PyStr("TUPLE EXCEPTIONS RESULTS:"));
    PyTup<int, double, PyStr> a = PyTup(2, 2.2, PyStr("b"));
    try {
        a.index(1);
    } catch (const CompyValueError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
}
