#include "src/exceptions/throw_.h"
#include "exceptions/common.h"
#include "exceptions/exception.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
static void _test_bare_raise() {
    try {
        throw pypp::IndexError(pypp::PyStr("test"));
    } catch (const pypp::IndexError &) {
        throw;
    }
}

void throw_fn() {
    pypp::print(pypp::PyStr("EXCEPTION RESULTS:"));
    try {
        throw pypp::Exception(pypp::PyStr("test"));
    } catch (const pypp::Exception &) {
        pypp::print(pypp::PyStr("exception happened"));
    }
    try {
        throw pypp::IndexError(pypp::PyStr("test"));
    } catch (const pypp::IndexError &) {
        pypp::print(pypp::PyStr("type error caught"));
    }
    try {
        throw pypp::IndexError(pypp::PyStr("test"));
    } catch (const pypp::IndexError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("type error caught: ") + pypp::str(e));
    }
    try {
        throw pypp::IndexError(pypp::PyStr("test"));
    } catch (const pypp::IndexError &) {
        pypp::print(pypp::PyStr("type error caught"));
    } catch (const pypp::ValueError &) {
        pypp::print(pypp::PyStr("value error caught"));
    } catch (const pypp::Exception &) {
        pypp::print(pypp::PyStr("other error caught"));
    }
    try {
        throw pypp::IndexError(pypp::PyStr("test"));
    } catch (...) {
        pypp::print(pypp::PyStr("catching all"));
    }
    try {
        _test_bare_raise();
    } catch (const pypp::IndexError &) {
        pypp::print(pypp::PyStr("bare raise"));
    }
}

} // namespace me