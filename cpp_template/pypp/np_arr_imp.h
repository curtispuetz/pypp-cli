#pragma once

#include "py_list.h"
#include <algorithm>
#include <initializer_list>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

template <typename T> class NpArr {
  private:
    std::vector<T> data_;
    std::vector<size_t> shape_;
    std::vector<size_t> strides_;

    // Helper to calculate the flat index from multidimensional indices
    template <typename... Dims> size_t get_index(size_t i, Dims... dims) const {
        // Unpack indices into a vector
        std::vector<size_t> indices = {i, static_cast<size_t>(dims)...};

        if (indices.size() != shape_.size()) {
            throw std::out_of_range(
                "Incorrect number of dimensions for indexing.");
        }

        size_t index = 0;
        for (size_t k = 0; k < indices.size(); ++k) {
            if (indices[k] >= shape_[k]) {
                throw std::out_of_range("Index out of bounds.");
            }
            index += indices[k] * strides_[k];
        }
        return index;
    }

    // Recursive helper for printing
    void print_recursive(std::ostream &os, size_t dim_index,
                         std::vector<size_t> &current_indices,
                         int indent_level) const {
        if (dim_index == shape_.size() - 1) {
            // Last dimension, print elements
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
    NpArr(const std::vector<size_t> &shape) : shape_(shape) {
        if (shape_.empty()) {
            throw std::invalid_argument(
                "Shape must have at least one dimension.");
        }
        size_t total_size =
            std::accumulate(shape_.begin(), shape_.end(),
                            static_cast<size_t>(1), std::multiplies<size_t>());
        data_.resize(total_size);

        strides_.resize(shape_.size());
        strides_.back() = 1;
        for (int i = shape_.size() - 2; i >= 0; --i) {
            strides_[i] = strides_[i + 1] * shape_[i + 1];
        }
    }

    // Constructor that takes an initializer list for convenience
    NpArr(std::initializer_list<size_t> shape)
        : NpArr(std::vector<size_t>(shape)) {}

    // Variadic template for direct access, e.g., arr(0, 1, 2)
    template <typename... Dims> T &operator()(size_t i, Dims... dims) {
        return data_[get_index(i, dims...)];
    }

    template <typename... Dims>
    const T &operator()(size_t i, Dims... dims) const {
        return data_[get_index(i, dims...)];
    }

    // Fill the entire array with a value
    void fill(const T &value) { std::fill(data_.begin(), data_.end(), value); }

    const PyList<int> shape() const {
        std::vector<int> ret;
        ret.reserve(shape_.size());
        for (size_t val : shape_) {
            ret.push_back(static_cast<int>(val));
        }
        return PyList(ret);
    }

    int size() const { return data_.size(); }

    // Print method similar to NumPy
    void print(std::ostream &os = std::cout) const {
        if (data_.empty()) {
            os << "[]" << std::endl;
            return;
        }

        std::vector<size_t> current_indices(shape_.size());
        print_recursive(
            os, 0, current_indices,
            1); // Start recursion from dimension 0, initial indent 1
        os << std::endl;
    }
};