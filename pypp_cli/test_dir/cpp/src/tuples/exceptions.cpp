#include "tuples/exceptions.h"
#include "exceptions/common.h"
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
    } catch (const pypp::ValueError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("value error: ") + pypp::str(e));
    }
}

} // namespace me