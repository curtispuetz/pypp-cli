#include "src/lists/exceptions.h"
#include "exceptions/common.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
void list_exceptions_fn() {
    pypp::print(pypp::PyStr("LIST EXCEPTIONS RESULTS:"));
    pypp::PyList<int> a({});
    try {
        a.pop();
    } catch (const pypp::IndexError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("index error: ") + pypp::str(e));
    }
    pypp::PyList<int> b({1, 2, 3});
    try {
        b.pop(3);
    } catch (const pypp::IndexError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("index error: ") + pypp::str(e));
    }
    try {
        b.remove(4);
    } catch (const pypp::ValueError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("value error: ") + pypp::str(e));
    }
    try {
        b.index(4);
    } catch (const pypp::ValueError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("value error: ") + pypp::str(e));
    }
    try {
        b[3];
    } catch (const pypp::IndexError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("index error: ") + pypp::str(e));
    }
}

} // namespace me