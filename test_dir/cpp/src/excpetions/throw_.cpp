#include "excpetions\throw_.h"

void throw_fn() {
    try {
        throw PyppException(PyStr("test").str());
    } catch (const PyppException &) {
        PyStr("exception happened").print();
    }
    try {
        throw PyppTypeError(PyStr("test").str());
    } catch (const PyppTypeError &) {
        PyStr("type error caught").print();
    }
    try {
        throw PyppTypeError(PyStr("test").str());
    } catch (const PyppTypeError &pypp_e) {
        std::string e = pypp_e.what();
        (PyStr("type error caught: ") + to_pystr(e)).print();
    }
    try {
        throw PyppTypeError(PyStr("test").str());
    } catch (const PyppTypeError &) {
        PyStr("type error caught").print();
    } catch (const PyppValueError &) {
        PyStr("value error caught").print();
    } catch (const PyppException &) {
        PyStr("other error caught").print();
    }
}