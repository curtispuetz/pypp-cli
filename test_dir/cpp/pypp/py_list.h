#pragma once

#include "py_slice.h"
#include <algorithm>
#include <iostream>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <vector>

template <typename T> class PyList {
  private:
    std::vector<T> data;

    PyList<T> slice(int start, std::optional<int> stop, int step) const {
        PyList<T> result;
        std::vector<int> indices = compute_slice_indices(
            start, stop, step, static_cast<int>(data.size()));
        for (int i : indices) {
            result.data.push_back(data[i]);
        }
        return result;
    }

    static std::vector<T> repeat_data(const std::vector<T> &input, int count) {
        std::vector<T> result;
        if (count <= 0)
            return result;

        result.reserve(input.size() * count);
        for (int i = 0; i < count; ++i) {
            result.insert(result.end(), input.begin(), input.end());
        }
        return result;
    }

  public:
    using value_type = T;
    // Constructors
    PyList() = default;
    PyList(const std::vector<T> &vec) : data(vec) {}
    PyList(std::initializer_list<T> init) : data(init) {}

    // Append
    void append(const T &value) { data.push_back(value); }

    // Pop
    T pop(int index = -1) {
        if (index == -1) {
            T ret = data[data.size() - 1];
            data.pop_back();
            return ret;
        }
        if (data.empty()) {
            throw std::out_of_range("pop from empty list");
        }
        if (index < 0)
            index += data.size();
        if (index < 0 || index >= static_cast<int>(data.size())) {
            throw std::out_of_range("pop index out of range");
        }
        T value = data[index];
        data.erase(data.begin() + index);
        return value;
    }

    // Insert
    void insert(int index, const T &value) {
        if (index < 0)
            index += data.size();
        if (index < 0)
            index = 0;
        if (index > static_cast<int>(data.size()))
            index = data.size();
        data.insert(data.begin() + index, value);
    }

    // Remove
    void remove(const T &value) {
        auto it = std::find(data.begin(), data.end(), value);
        if (it == data.end()) {
            throw std::invalid_argument("value not in list");
        }
        data.erase(it);
    }

    // Clear
    void clear() { data.clear(); }

    // Index
    int index(const T &value) const {
        auto it = std::find(data.begin(), data.end(), value);
        if (it == data.end()) {
            throw std::invalid_argument("value not in list");
        }
        return it - data.begin();
    }

    // Count
    int count(const T &value) const {
        return std::count(data.begin(), data.end(), value);
    }

    // Reverse
    void reverse() { std::reverse(data.begin(), data.end()); }

    // Size
    int len() const { return data.size(); }

    // Operator []
    // So modifications of operators are allowed?
    T &operator[](int index) {
        if (index < 0)
            index += data.size();
        if (index < 0 || index >= static_cast<int>(data.size())) {
            throw std::out_of_range("list index out of range");
        }
        return data[index];
    }

    const T &operator[](int index) const {
        if (index < 0)
            index += data.size();
        if (index < 0 || index >= data.size()) {
            throw std::out_of_range("list index out of range");
        }
        return data[index];
    }

    PyList<T> operator[](const PySlice &sl) const {
        return slice(sl.start, sl.stop, sl.step);
    }

    bool operator==(const PyList<T> &other) const { return data == other.data; }

    bool operator!=(const PyList<T> &other) const { return data != other.data; }

    bool operator<(const PyList<T> &other) const { return data < other.data; }

    bool operator<=(const PyList<T> &other) const { return data <= other.data; }

    bool operator>(const PyList<T> &other) const { return data > other.data; }

    bool operator>=(const PyList<T> &other) const { return data >= other.data; }

    PyList<T> operator+(const PyList<T> &other) const {
        PyList<T> result;
        result.data.reserve(data.size() + other.data.size());
        result.data.insert(result.data.end(), data.begin(), data.end());
        result.data.insert(result.data.end(), other.data.begin(),
                           other.data.end());
        return result;
    }

    PyList<T> operator*(int count) const {
        return PyList<T>(repeat_data(data, count));
    }

    PyList<T> &operator+=(const PyList<T> &other) {
        data.insert(data.end(), other.data.begin(), other.data.end());
        return *this;
    }

    PyList<T> &operator*=(int count) {
        data = repeat_data(data, count);
        return *this;
    }

    // Iterator support
    auto begin() { return data.begin(); }
    auto end() { return data.end(); }
    auto begin() const { return data.begin(); }
    auto end() const { return data.end(); }

    void print(std::ostream &os) const {
        os << "[";
        for (size_t i = 0; i < data.size(); ++i) {
            os << data[i];
            if (i != data.size() - 1)
                os << ", ";
        }
        os << "]";
    }

    void print() const {
        print(std::cout);
        std::cout << std::endl;
    }

    template <typename U>
    friend std::ostream &operator<<(std::ostream &os, const PyList<U> &list);
};

template <typename T>
std::ostream &operator<<(std::ostream &os, const PyList<T> &list) {
    list.print(os);
    return os;
}
