#pragma once

#include <ostream>

namespace pypp {

// Forward declare PyStr to avoid circular includes
class PyStr;

template <typename T> void print_py_value(std::ostream &os, const T &value) {
    os << value;
}

// NOTE: It is not as easy to support True and False printing in
// the print() function. For that it still prints 1 and 0.
inline void print_py_value(std::ostream &os, const bool value) {
    os << (value ? "True" : "False");
}

// Specialization for PyStr
void print_py_value(std::ostream &os, const PyStr &value);

} // namespace pypp