#include "stdexcept.h"
#include <py_str.h>

namespace pypp {

RuntimeError::RuntimeError(const PyStr &msg)
    : std::runtime_error("RuntimeError: " + msg.str()) {}
RuntimeError::RuntimeError(const std::string &msg)
    : std::runtime_error("RuntimeError: " + msg) {}

ValueError::ValueError(const PyStr &msg)
    : std::invalid_argument("ValueError: " + msg.str()) {}
ValueError::ValueError(const std::string &msg)
    : std::invalid_argument("ValueError: " + msg) {}

TypeError::TypeError(const PyStr &msg)
    : std::invalid_argument("TypeError: " + msg.str()) {}
TypeError::TypeError(const std::string &msg)
    : std::invalid_argument("TypeError: " + msg) {}

IndexError::IndexError(const PyStr &msg)
    : std::out_of_range("IndexError: " + msg.str()) {}
IndexError::IndexError(const std::string &msg)
    : std::out_of_range("IndexError: " + msg) {}

KeyError::KeyError(const PyStr &msg)
    : std::out_of_range("KeyError: " + msg.str()) {}
KeyError::KeyError(const std::string &msg)
    : std::out_of_range("KeyError: " + msg) {}

ZeroDivisionError::ZeroDivisionError(const PyStr &msg)
    : std::domain_error("ZeroDivisionError: " + msg.str()) {}
ZeroDivisionError::ZeroDivisionError(const std::string &msg)
    : std::domain_error("ZeroDivisionError: " + msg) {}

AssertionError::AssertionError(const PyStr &msg)
    : std::logic_error("AssertionError: " + msg.str()) {}
AssertionError::AssertionError(const std::string &msg)
    : std::logic_error("AssertionError: " + msg) {}

NotImplementedError::NotImplementedError(const PyStr &msg)
    : std::logic_error("NotImplementedError: " + msg.str()) {}
NotImplementedError::NotImplementedError(const std::string &msg)
    : std::logic_error("NotImplementedError: " + msg) {}

AttributeError::AttributeError(const PyStr &msg)
    : std::logic_error("AttributeError: " + msg.str()) {}
AttributeError::AttributeError(const std::string &msg)
    : std::logic_error("AttributeError: " + msg) {}

} // namespace pypp