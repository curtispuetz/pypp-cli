#include "exceptions/throw_.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "exceptions/exception.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include <string>

void throw_fn() {
    print(PyStr("EXCEPTION RESULTS:"));
    try {
        throw CompyException(PyStr("test").str());
    } catch (const CompyException &) {
        print(PyStr("exception happened"));
    }
    try {
        throw CompyTypeError(PyStr("test").str());
    } catch (const CompyTypeError &) {
        print(PyStr("type error caught"));
    }
    try {
        throw CompyTypeError(PyStr("test").str());
    } catch (const CompyTypeError &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("type error caught: ") + to_pystr(e));
    }
    try {
        throw CompyTypeError(PyStr("test").str());
    } catch (const CompyTypeError &) {
        print(PyStr("type error caught"));
    } catch (const CompyValueError &) {
        print(PyStr("value error caught"));
    } catch (const CompyException &) {
        print(PyStr("other error caught"));
    }
}
