#pragma once

#include "py_str.h"
#include <string>

namespace pypp {

template <typename T> inline PyStr to_pystr(const T &value) {
    return PyStr(std::to_string(value));
}

// Note: I think this is only used for throwing exceptions.
inline PyStr to_pystr(std::string value) { return PyStr(std::move(value)); }

inline PyStr to_pystr(const char *value) { return PyStr(std::string(value)); }

} // namespace pypp