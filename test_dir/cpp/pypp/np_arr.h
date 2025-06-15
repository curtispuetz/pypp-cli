#pragma once

#include "np_arr_imp.h"
#include "np_arr_util.h"
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

template <typename T, typename U> NpArr<T> array(const PyList<U> &list) {
    // 1. Deduce the shape from the nested list structure.
    PyList<size_t> shape;
    deduce_shape_recursive(list, shape);

    // 2. Flatten the nested list into a single vector.
    std::vector<T> flat_data;
    // Calculate total size to reserve memory efficiently.
    size_t total_size = shape.len() == 0
                            ? 0
                            : std::accumulate(shape.begin(), shape.end(),
                                              static_cast<size_t>(1),
                                              std::multiplies<size_t>());

    if (total_size > 0) {
        flat_data.reserve(total_size);
        flatten_recursive(list, flat_data);
    }

    // 3. Use the private constructor to create the NpArr instance.
    return NpArr<T>(shape, std::move(flat_data));
}

} // namespace pypp_np