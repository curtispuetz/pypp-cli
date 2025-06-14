#pragma once

#include "np_arr_imp.h"
#include <initializer_list>
#include <vector>

namespace pypp_np {

template <typename T> NpArr<T> zeros(const PyList<size_t> &shape) {
    NpArr<T> arr(shape);
    arr.fill(T{0});
    return arr;
}

// Overload for initializer_list
template <typename T> NpArr<T> zeros(std::initializer_list<size_t> shape) {
    return zeros<T>(PyList<size_t>(shape));
}

template <typename T> NpArr<T> ones(const PyList<size_t> &shape) {
    NpArr<T> arr(shape);
    arr.fill(T{1});
    return arr;
}

// Overload for initializer_list
template <typename T> NpArr<T> ones(std::initializer_list<size_t> shape) {
    return ones<T>(PyList<size_t>(shape));
}

template <typename T>
NpArr<T> full(const PyList<size_t> &shape, const T &value) {
    NpArr<T> arr(shape);
    arr.fill(value);
    return arr;
}

// Overload for initializer_list
template <typename T>
NpArr<T> full(std::initializer_list<size_t> shape, const T &value) {
    return full<T>(PyList<size_t>(shape), value);
}

} // namespace pypp_np