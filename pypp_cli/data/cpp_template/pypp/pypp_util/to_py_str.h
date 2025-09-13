#pragma once

#include "py_str.h"
#include <string>

namespace pypp {

template <typename T> inline PyStr str(const T &value) {
    return PyStr(std::to_string(value));
}
// Note: I think this is only used for throwing exceptions. But not sure.
inline PyStr str(std::string value) { return PyStr(std::move(value)); }
inline PyStr str(const char *value) { return PyStr(std::string(value)); }

} // namespace pypp