#pragma once

#include "exceptions/stdexcept.h"
#include "pypp_util/print_py_value.h"
#include "slice/py_slice.h"
#include <algorithm>
#include <format>
#include <iostream>
#include <optional>
#include <sstream>
#include <vector>

template <typename T> class PyList {
  private:
    std::vector<T> data;

    static std::vector<T> repeat_data(const std::vector<T> &input, int count) {
        if (input.size() == 1) {
            // Optimization for the common [1] * count case
            return std::vector(count, input[0]);
        }
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
    // This one is only used internally and not by users of Pypp.
    PyList(const std::vector<T> &&vec) : data(std::move(vec)) {}
    PyList(std::initializer_list<T> init) : data(init) {}
    PyList(const int size, const T &value) : data(size, value) {}
    PyList(const int size) : data(size) {}

    void append(T &&value) { data.push_back(std::move(value)); }

    // Pop
    T pop(int index = -1) {
        if (data.empty()) {
            throw PyppIndexError("pop from empty list");
        }
        if (index == -1) {
            T ret = std::move(data[data.size() - 1]);
            data.pop_back();
            return ret;
        }
        if (index < 0)
            index += data.size();
        if (index < 0 || index >= static_cast<int>(data.size())) {
            throw PyppIndexError("list.pop(x): x out of range");
        }
        T value = std::move(data[index]);
        data.erase(data.begin() + index);
        return value;
    }

    // Insert
    void insert(int index, T &&value) {
        if (index < 0)
            index += data.size();
        if (index < 0)
            index = 0;
        if (index > static_cast<int>(data.size()))
            index = data.size();
        data.insert(data.begin() + index, std::move(value));
    }

    // Extend: add all elements from another PyList
    void extend(PyList<T> &&other) {
        data.insert(data.end(), std::make_move_iterator(other.data.begin()),
                    std::make_move_iterator(other.data.end()));
        other.data.clear();
    }

    // Remove
    void remove(const T &value) {
        auto it = std::find(data.begin(), data.end(), value);
        if (it == data.end()) {
            throw PyppValueError("list.remove(x): x not in list");
        }
        data.erase(it);
    }

    void reserve(int size) { data.reserve(size); }

    // Clear
    void clear() { data.clear(); }

    // Index
    int index(const T &value) const {
        auto it = std::find(data.begin(), data.end(), value);
        if (it == data.end()) {
            throw PyppValueError("list.index(x): x not in list");
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
            throw PyppIndexError("list index out of range");
        }
        return data[index];
    }

    // TODO later: delete this because I think I don't need it.
    const T &operator[](int index) const {
        if (index < 0)
            index += data.size();
        if (index < 0 || index >= data.size()) {
            throw PyppIndexError("list index out of range");
        }
        return data[index];
    }

    PyList<T> operator[](const PySlice &sl) const {
        PyList<T> result;
        PyTup<int, int, int> indices =
            sl.indices(static_cast<int>(data.size()));
        int start = indices.get<0>();
        int stop = indices.get<1>();
        int step = indices.get<2>();
        if (step > 0) {
            for (int i = start; i < stop; i += step) {
                result.data.push_back(data[i]);
            }
        } else {
            for (int i = start; i > stop; i += step) {
                result.data.push_back(data[i]);
            }
        }
        return result;
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

    // Check membership
    bool contains(const T &value) const {
        return std::find(data.begin(), data.end(), value) != data.end();
    }

    std::vector<T> &data_ref() { return data; }

    // Iterator support
    auto begin() { return data.begin(); }
    auto end() { return data.end(); }
    auto begin() const { return data.begin(); }
    auto end() const { return data.end(); }
    // Reverse iterator support
    auto rbegin() { return data.rbegin(); }
    auto rend() { return data.rend(); }
    auto rbegin() const { return data.crbegin(); } // Const version
    auto rend() const { return data.crend(); }     // Const version

    void print(std::ostream &os) const {
        os << "[";
        for (size_t i = 0; i < data.size(); ++i) {
            print_py_value(os, data[i]);
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

namespace std {
// Hash function for usage as a key in PyDict and PySet
template <typename T> struct hash<PyList<T>> {
    std::size_t operator()(const PyList<T> &p) const noexcept {
        std::size_t seed = 0;
        for (const auto &item : p) {
            seed ^=
                std::hash<T>()(item) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};
// Formatter for std::format
template <typename T> struct formatter<PyList<T>, char> {
    constexpr auto parse(format_parse_context &ctx) { return ctx.begin(); }

    template <typename FormatContext>
    auto format(const PyList<T> &p, FormatContext &ctx) const {
        std::ostringstream oss;
        p.print(oss);
        return std::format_to(ctx.out(), "{}", oss.str());
    }
};
} // namespace std

// This can be used as a helper function to create the PyList so that the
// mapping from Python to C++ is more clear.
template <typename T>
PyList<T> create_list_full(const int size, const T &value) {
    return PyList<T>(size, value);
}