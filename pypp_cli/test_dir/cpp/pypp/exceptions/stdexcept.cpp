#include "stdexcept.h"
#include <py_str.h>

PyppRuntimeError::PyppRuntimeError(const PyStr &msg)
    : std::runtime_error("PyppRuntimeError: " + msg.str()) {}
PyppRuntimeError::PyppRuntimeError(const std::string &msg)
    : std::runtime_error("PyppRuntimeError: " + msg) {}

PyppValueError::PyppValueError(const PyStr &msg)
    : std::invalid_argument("PyppValueError: " + msg.str()) {}
PyppValueError::PyppValueError(const std::string &msg)
    : std::invalid_argument("PyppValueError: " + msg) {}

PyppTypeError::PyppTypeError(const PyStr &msg)
    : std::invalid_argument("PyppTypeError: " + msg.str()) {}
PyppTypeError::PyppTypeError(const std::string &msg)
    : std::invalid_argument("PyppTypeError: " + msg) {}

PyppIndexError::PyppIndexError(const PyStr &msg)
    : std::out_of_range("PyppIndexError: " + msg.str()) {}
PyppIndexError::PyppIndexError(const std::string &msg)
    : std::out_of_range("PyppIndexError: " + msg) {}

PyppKeyError::PyppKeyError(const PyStr &msg)
    : std::out_of_range("PyppKeyError: " + msg.str()) {}
PyppKeyError::PyppKeyError(const std::string &msg)
    : std::out_of_range("PyppKeyError: " + msg) {}

PyppZeroDivisionError::PyppZeroDivisionError(const PyStr &msg)
    : std::domain_error("PyppZeroDivisionError: " + msg.str()) {}
PyppZeroDivisionError::PyppZeroDivisionError(const std::string &msg)
    : std::domain_error("PyppZeroDivisionError: " + msg) {}

PyppAssertionError::PyppAssertionError(const PyStr &msg)
    : std::logic_error("PyppAssertionError: " + msg.str()) {}
PyppAssertionError::PyppAssertionError(const std::string &msg)
    : std::logic_error("PyppAssertionError: " + msg) {}

PyppNotImplementedError::PyppNotImplementedError(const PyStr &msg)
    : std::logic_error("PyppNotImplementedError: " + msg.str()) {}
PyppNotImplementedError::PyppNotImplementedError(const std::string &msg)
    : std::logic_error("PyppNotImplementedError: " + msg) {}

PyppAttributeError::PyppAttributeError(const PyStr &msg)
    : std::logic_error("PyppAttributeError: " + msg.str()) {}
PyppAttributeError::PyppAttributeError(const std::string &msg)
    : std::logic_error("PyppAttributeError: " + msg) {}