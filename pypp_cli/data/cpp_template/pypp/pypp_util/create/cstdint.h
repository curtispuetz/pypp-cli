#pragma once

#include <cstdint>

namespace pypp {

template <typename T> inline int8_t to_int8_t(const T &value) {
    return static_cast<int8_t>(value);
}

template <typename T> inline int16_t to_int16_t(const T &value) {
    return static_cast<int16_t>(value);
}

template <typename T> inline int32_t to_int32_t(const T &value) {
    return static_cast<int32_t>(value);
}

template <typename T> inline int64_t to_int64_t(const T &value) {
    return static_cast<int64_t>(value);
}

template <typename T> inline uint8_t to_uint8_t(const T &value) {
    return static_cast<uint8_t>(value);
}

template <typename T> inline uint16_t to_uint16_t(const T &value) {
    return static_cast<uint16_t>(value);
}

template <typename T> inline uint32_t to_uint32_t(const T &value) {
    return static_cast<uint32_t>(value);
}

template <typename T> inline uint64_t to_uint64_t(const T &value) {
    return static_cast<uint64_t>(value);
}

} // namespace pypp