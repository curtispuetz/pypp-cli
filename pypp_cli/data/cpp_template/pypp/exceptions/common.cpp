#include "exceptions/common.h"
#include <py_str.h>

namespace pypp {

ValueError::ValueError(const PyStr &msg)
    : Exception("ValueError: " + msg.str()) {}
ValueError::ValueError(const std::string &msg)
    : Exception("ValueError: " + msg) {}

AssertionError::AssertionError(const PyStr &msg)
    : Exception("AssertionError: " + msg.str()) {}

LookupError::LookupError(const PyStr &msg)
    : Exception("LookupError: " + msg.str()) {}

IndexError::IndexError(const PyStr &msg)
    : LookupError("IndexError: " + msg.str()) {}
IndexError::IndexError(const std::string &msg)
    : LookupError("IndexError: " + msg) {}

KeyError::KeyError(const PyStr &msg) : LookupError("KeyError: " + msg.str()) {}
KeyError::KeyError(const std::string &msg) : LookupError("KeyError: " + msg) {}

RuntimeError::RuntimeError(const PyStr &msg)
    : Exception("RuntimeError: " + msg.str()) {}
RuntimeError::RuntimeError(const std::string &msg)
    : Exception("RuntimeError: " + msg) {}

NotImplementedError::NotImplementedError(const PyStr &msg)
    : RuntimeError("NotImplementedError: " + msg.str()) {}

} // namespace pypp