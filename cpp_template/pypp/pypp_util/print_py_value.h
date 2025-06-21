#pragma once

#include <ostream>

// Forward declare PyStr to avoid circular includes
class PyStr;

template <typename T> void print_py_value(std::ostream &os, const T &value) {
    os << value;
}

// Specialization for PyStr
void print_py_value(std::ostream &os, const PyStr &value);