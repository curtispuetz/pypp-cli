#pragma once

#include "py_str.h"
#include <iostream>

namespace pypp {

template <typename T> inline int int_(const T &value) {
    return static_cast<int>(value);
}

inline int int_(const PyStr &value) { return std::stoi(value.str()); }

template <typename T> inline double float_(const T &value) {
    return static_cast<double>(value);
}

inline double float_(const PyStr &value) { return std::stod(value.str()); }

template <typename T> inline bool bool_(const T &value) {
    return static_cast<bool>(value);
}

inline bool bool_(const PyStr &value) { return !value.str().empty(); }

template <typename T> inline float to_float32(const T &value) {
    return static_cast<float>(value);
}

inline float to_float32(const PyStr &value) { return std::stof(value.str()); }

} // namespace pypp