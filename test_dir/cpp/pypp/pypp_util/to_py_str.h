#pragma once

#include "py_str.h"
#include <string>

template <typename T> PyStr to_pystr(const T &value) {
    return PyStr(std::to_string(value));
}
