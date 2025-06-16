#pragma once

#include "exceptions/stdexcept.h"
#include "exceptions/system_error.h"
#include "py_list.h"
#include "py_tuple.h"
#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <numeric>
#include <string>
#include <type_traits> // Required for std::true_type, std::false_type
#include <utility>     // Required for std::index_sequence
#include <vector>

template <typename T> class NpArr {
  private:
    std::vector<T> data_;
    PyList<size_t> shape_;
    std::vector<size_t> strides_;

    // Helper to calculate the flat index from multidimensional indices
    template <typename... Dims> size_t get_index(size_t i, Dims... dims) const {
        // Unpack indices into a vector
        std::vector<size_t> indices = {i, static_cast<size_t>(dims)...};

        if (indices.size() != shape_.len()) {
            throw PyppIndexError(
                "too many indices for array: array is " +
                std::to_string(shape_.len()) + "-dimensional, but " +
                std::to_string(indices.size()) + " were indexed");
        }

        size_t index = 0;
        for (size_t k = 0; k < indices.size(); ++k) {
            if (indices[k] >= shape_[k]) {
                throw PyppIndexError("index " + std::to_string(indices[k]) +
                                     " is out of bounds for axis " +
                                     std::to_string(k) + " with size " +
                                     std::to_string(shape_[k]));
            }
            index += indices[k] * strides_[k];
        }
        return index;
    }

    // Implementation part of the tuple unpacking mechanism.
    // It receives an index sequence (like 0, 1, 2, ...) and uses it to
    // call get() for each index on the tuple, effectively unpacking it.
    template <typename... Ts, size_t... Is>
    size_t get_index_from_tuple_impl(const PyTup<Ts...> &t,
                                     std::index_sequence<Is...>) const {
        // This expands to: return get_index(t.template get<0>(), t.template
        // get<1>(), ...);
        return get_index(t.template get<Is>()...);
    }

    // Kicks off the tuple unpacking.
    // It deduces the tuple type and creates an integer sequence from 0 to N-1,
    // where N is the number of elements in the tuple.
    template <typename... Ts>
    size_t get_index_from_tuple(const PyTup<Ts...> &t) const {
        // This generates the required std::index_sequence for the
        // implementation function.
        return get_index_from_tuple_impl(
            t, std::make_index_sequence<sizeof...(Ts)>{});
    }

    // Recursive helper for printing
    void print_recursive(std::ostream &os, size_t dim_index,
                         std::vector<size_t> &current_indices,
                         int indent_level) const {
        if (dim_index == shape_.len() - 1) {
            // Last dimension, print elements
            os << "[";
            for (size_t i = 0; i < shape_[dim_index]; ++i) {
                current_indices[dim_index] = i;
                size_t flat_index = 0;
                for (size_t k = 0; k < current_indices.size(); ++k) {
                    flat_index += current_indices[k] * strides_[k];
                }
                os << data_[flat_index];
                if (i < shape_[dim_index] - 1) {
                    os << " ";
                }
            }
            os << "]";
        } else {
            // Not the last dimension, print opening bracket
            os << "[";
            for (size_t i = 0; i < shape_[dim_index]; ++i) {
                current_indices[dim_index] = i;
                if (i > 0) {
                    os << std::string(indent_level,
                                      ' '); // Indent for subsequent rows
                }
                print_recursive(os, dim_index + 1, current_indices,
                                indent_level + 1);
                if (i < shape_[dim_index] - 1) {
                    os << "\n";
                }
            }
            os << "]";
        }
    }

  public:
    // Constructor takes a vector for the shape
    NpArr(const PyList<size_t> &shape) : shape_(shape) {
        if (shape_.len() == 0) {
            throw PyppValueError("empty numpy array is not supported");
        }
        size_t total_size =
            std::accumulate(shape_.begin(), shape_.end(),
                            static_cast<size_t>(1), std::multiplies<size_t>());
        data_.resize(total_size);

        strides_.resize(shape_.len());
        strides_.back() = 1;
        for (int i = shape_.len() - 2; i >= 0; --i) {
            strides_[i] = strides_[i + 1] * shape_[i + 1];
        }
    }

    // Constructor that takes an initializer list for convenience
    NpArr(std::initializer_list<size_t> shape) : NpArr(PyList<size_t>(shape)) {}

    // Default constructor for an empty array
    NpArr() : NpArr({0}) {
        data_.clear(); // Make sure data is empty for shape (0,)
    }

    // Constructor for internal use by the `from_pylist` factory method.
    // It takes a shape and moves the already-flattened data vector.
    NpArr(const PyList<size_t> &shape, std::vector<T> &&data)
        : shape_(shape), data_(std::move(data)) {
        // This constructor assumes the provided data is already validated and
        // flattened. It calculates the strides based on the given shape.
        strides_.resize(shape_.len());
        if (!(shape_.len() == 0)) {
            strides_.back() = 1;
            for (int i = shape_.len() - 2; i >= 0; --i) {
                strides_[i] = strides_[i + 1] * shape_[i + 1];
            }
        }

        // Final sanity check to ensure shape and data size match.
        size_t total_size = shape_.len() == 0
                                ? 0
                                : std::accumulate(shape_.begin(), shape_.end(),
                                                  static_cast<size_t>(1),
                                                  std::multiplies<size_t>());
        if (data_.size() != total_size) {
            throw PyppSystemError(
                "(this could be a Pypp bug) Data size and "
                "shape mismatch during "
                "construction of numpy array. The list was "
                "likely ragged in a deeper "
                "dimension.",
                std::error_code(errno, std::system_category()));
        }
    }

    // Variadic template for direct access, e.g., arr(0, 1, 2)
    template <typename... Dims> T &operator()(size_t i, Dims... dims) {
        return data_[get_index(i, dims...)];
    }

    template <typename... Dims>
    const T &operator()(size_t i, Dims... dims) const {
        return data_[get_index(i, dims...)];
    }

    template <typename... Dims>
    void set(const PyTup<int, Dims...> &i, const T &value) {
        data_[get_index_from_tuple(i)] = value;
    }

    // Fill the entire array with a value
    void fill(const T &value) { std::fill(data_.begin(), data_.end(), value); }

    const PyList<int> shape() const {
        std::vector<int> ret;
        ret.reserve(shape_.len());
        for (size_t val : shape_) {
            ret.push_back(static_cast<int>(val));
        }
        return PyList(ret);
    }

    int size() const { return data_.size(); }

    // Print method similar to NumPy
    void print(std::ostream &os = std::cout) const {
        if (shape_.len() == 1 && shape_[0] == 0) {
            os << "[]" << std::endl;
            return;
        }

        std::vector<size_t> current_indices(shape_.len());
        print_recursive(
            os, 0, current_indices,
            1); // Start recursion from dimension 0, initial indent 1
        os << std::endl;
    }
};
