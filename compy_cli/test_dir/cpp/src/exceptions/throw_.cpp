#include "exceptions/throw_.h"
#include "exceptions/exception.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

void throw_fn() {
    print(PyStr("EXCEPTION RESULTS:"));
    try {
        throw PyppException(PyStr("test").str());
    } catch (const PyppException &) {
        print(PyStr("exception happened"));
    }
    try {
        throw PyppTypeError(PyStr("test").str());
    } catch (const PyppTypeError &) {
        print(PyStr("type error caught"));
    }
    try {
        throw PyppTypeError(PyStr("test").str());
    } catch (const PyppTypeError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("type error caught: ") + to_pystr(e));
    }
    try {
        throw PyppTypeError(PyStr("test").str());
    } catch (const PyppTypeError &) {
        print(PyStr("type error caught"));
    } catch (const PyppValueError &) {
        print(PyStr("value error caught"));
    } catch (const PyppException &) {
        print(PyStr("other error caught"));
    }
}
