#include "exceptions/throw_.h"
#include "exceptions/exception.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

void throw_fn() {
    pypp::print(pypp::PyStr("EXCEPTION RESULTS:"));
    try {
        throw pypp::PyppException(pypp::PyStr("test"));
    } catch (const pypp::PyppException &) {
        pypp::print(pypp::PyStr("exception happened"));
    }
    try {
        throw pypp::PyppTypeError(pypp::PyStr("test"));
    } catch (const pypp::PyppTypeError &) {
        pypp::print(pypp::PyStr("type error caught"));
    }
    try {
        throw pypp::PyppTypeError(pypp::PyStr("test"));
    } catch (const pypp::PyppTypeError &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("type error caught: ") + pypp::to_pystr(e));
    }
    try {
        throw pypp::PyppTypeError(pypp::PyStr("test"));
    } catch (const pypp::PyppTypeError &) {
        pypp::print(pypp::PyStr("type error caught"));
    } catch (const pypp::PyppValueError &) {
        pypp::print(pypp::PyStr("value error caught"));
    } catch (const pypp::PyppException &) {
        pypp::print(pypp::PyStr("other error caught"));
    }
}
