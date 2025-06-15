#pragma once

#include "py_list.h"
#include <stdexcept>
#include <vector>

// Helper to check if a type is a PyList
template <typename> struct is_pylist : std::false_type {};
template <typename U> struct is_pylist<PyList<U>> : std::true_type {};

// Recursive helper to deduce the shape of a nested PyList.
// It also validates that the list is not ragged.
template <typename ListType>
static void deduce_shape_recursive(const ListType &list,
                                   PyList<size_t> &shape) {
    // Use if-constexpr to distinguish between a list of lists and a list of
    // elements at compile time.
    if constexpr (is_pylist<typename ListType::value_type>::value) {
        // This is a list of lists.
        shape.append(list.len());
        if (list.len() > 0) {
            // Check for raggedness: ensure all sublists have the same
            // length.
            const auto &first_sublist = list[0];
            for (size_t i = 1; i < list.len(); ++i) {
                if (list[i].len() != first_sublist.len()) {
                    throw std::invalid_argument(
                        "Inconsistent sublist length; array must not be "
                        "ragged.");
                }
            }
            // Recurse into the first sublist to determine the shape of the
            // next dimension.
            deduce_shape_recursive(first_sublist, shape);
        }
    } else {
        // This is the innermost list (contains type T, not PyList<...>),
        // representing the last dimension.
        shape.append(list.len());
    }
}

// Recursive helper to flatten the nested PyList into a single std::vector.
template <typename T, typename ListType>
static void flatten_recursive(const ListType &list, std::vector<T> &data) {
    if constexpr (is_pylist<typename ListType::value_type>::value) {
        // This list contains other lists, so recurse into each one.
        for (const auto &sublist : list) {
            flatten_recursive(sublist, data);
        }
    } else {
        // This list contains the actual data elements. Copy them to the
        // flat vector.
        for (const T &item : list) {
            data.push_back(item);
        }
    }
}