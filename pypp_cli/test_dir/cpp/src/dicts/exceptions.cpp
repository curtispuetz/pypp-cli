#include "dicts/exceptions.h"
#include "exceptions/common.h"
#include "py_dict.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
void dict_exceptions_fn() {
    pypp::print(pypp::PyStr("DICT EXCEPTIONS RESULTS:"));
    pypp::PyDict<int, int> a = {{0, 1}, {1, 2}};
    try {
        a.pop(-1);
    } catch (const pypp::KeyError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("key error: ") + pypp::str(e));
    }
    try {
        a.dg(-1);
    } catch (const pypp::KeyError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("key error: ") + pypp::str(e));
    }
}

} // namespace me