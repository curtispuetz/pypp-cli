#pragma once

#include <string>
#include "py_str.h"

template<typename T>
PyStr to_pystr(const T& value) {
    return PyStr(std::to_string(value));
}
