#include "sets/exceptions.h"
#include "exceptions/stdexcept.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

void set_exceptions_fn() {
    pypp::print(pypp::PyStr("SET EXCEPTIONS RESULTS:"));
    pypp::PySet<int> a({1, 2});
    try {
        a.remove(3);
    } catch (const pypp::PyppKeyError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("key error: ") + pypp::to_pystr(e));
    }
}
