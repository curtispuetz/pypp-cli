#include "strings/exceptions.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
void string_exceptions_fn() {
    pypp::print(pypp::PyStr("STRING EXCEPTIONS RESULTS:"));
    pypp::PyStr s = pypp::PyStr("test");
    try {
        s.index(pypp::PyStr("a"));
    } catch (const pypp::PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("value error: ") + pypp::str(e));
    }
    try {
        s.rindex(pypp::PyStr("a"));
    } catch (const pypp::PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("value error: ") + pypp::str(e));
    }
    try {
        s[9];
    } catch (const pypp::PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("index error: ") + pypp::str(e));
    }
    try {
        s[-9];
    } catch (const pypp::PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("index error: ") + pypp::str(e));
    }
}

} // namespace me