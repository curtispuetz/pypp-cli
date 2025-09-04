#include "tuples/exceptions.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

void tuple_exceptions_fn() {
    print(PyStr("TUPLE EXCEPTIONS RESULTS:"));
    PyTup<int, double, PyStr> a = PyTup(2, 2.2, PyStr("b"));
    try {
        a.index(1);
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
}
