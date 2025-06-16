#pragma once

#include "py_str.h"
#include <string>

template <typename T> inline PyStr to_pystr(const T &value) {
    return PyStr(std::to_string(value));
}

inline PyStr to_pystr(const std::string &value) { return PyStr(value); }

inline PyStr to_pystr(const char *value) { return PyStr(std::string(value)); }