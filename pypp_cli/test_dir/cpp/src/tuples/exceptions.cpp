#include "tuples/exceptions.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
void tuple_exceptions_fn() {
    pypp::print(pypp::PyStr("TUPLE EXCEPTIONS RESULTS:"));
    pypp::PyTup<int, double, pypp::PyStr> a =
        pypp::PyTup(2, 2.2, pypp::PyStr("b"));
    try {
        a.index(1);
    } catch (const pypp::PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("value error: ") + pypp::to_pystr(e));
    }
}

} // namespace me