#pragma once

#include "np_arr_imp.h"
#include <initializer_list>
#include <vector>

namespace np {

template <typename T> NpArr<T> zeros(const std::vector<size_t> &shape) {
    NpArr<T> arr(shape);
    arr.fill(T{0});
    return arr;
}

// Overload for initializer_list
template <typename T> NpArr<T> zeros(std::initializer_list<size_t> shape) {
    return zeros<T>(std::vector<size_t>(shape));
}

template <typename T> NpArr<T> ones(const std::vector<size_t> &shape) {
    NpArr<T> arr(shape);
    arr.fill(T{1});
    return arr;
}

// Overload for initializer_list
template <typename T> NpArr<T> ones(std::initializer_list<size_t> shape) {
    return ones<T>(std::vector<size_t>(shape));
}

template <typename T>
NpArr<T> full(const std::vector<size_t> &shape, const T &value) {
    NpArr<T> arr(shape);
    arr.fill(value);
    return arr;
}

// Overload for initializer_list
template <typename T>
NpArr<T> full(std::initializer_list<size_t> shape, const T &value) {
    return full<T>(std::vector<size_t>(shape), value);
}

} // namespace np