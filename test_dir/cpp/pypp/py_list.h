#pragma once

#include <vector>
#include <stdexcept>
#include <algorithm>
#include <iostream>

template<typename T>
class PyList {
private:
    std::vector<T> data;

public:
    // Constructors
    PyList() = default;
    PyList(std::initializer_list<T> init) : data(init) {}

    // Append
    void append(const T& value) {
        data.push_back(value);
    }

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
        if (index < 0) index += data.size();
        if (index < 0 || index >= static_cast<int>(data.size())) {
            throw std::out_of_range("pop index out of range");
        }
        T value = data[index];
        data.erase(data.begin() + index);
        return value;
    }

    // Insert
    void insert(int index, const T& value) {
        if (index < 0) index += data.size();
        if (index < 0) index = 0;
        if (index > static_cast<int>(data.size())) index = data.size();
        data.insert(data.begin() + index, value);
    }

    // Remove
    void remove(const T& value) {
        auto it = std::find(data.begin(), data.end(), value);
        if (it == data.end()) {
            throw std::invalid_argument("value not in list");
        }
        data.erase(it);
    }

    // Clear
    void clear() {
        data.clear();
    }

    // Index
    int index(const T& value) const {
        auto it = std::find(data.begin(), data.end(), value);
        if (it == data.end()) {
            throw std::invalid_argument("value not in list");
        }
        return it - data.begin();
    }

    // Count
    int count(const T& value) const {
        return std::count(data.begin(), data.end(), value);
    }

    // Reverse
    void reverse() {
        std::reverse(data.begin(), data.end());
    }

    // Size
    size_t len() const {
        return data.size();
    }

    // Operator []
    // So modifications of operators are allowed?
    T& operator[](int index) {
        if (index < 0) index += data.size();
        if (index < 0 || index >= static_cast<int>(data.size())) {
            throw std::out_of_range("list index out of range");
        }
        return data[index];
    }

    // Print
    void print() const {
        std::cout << "[";
        for (size_t i = 0; i < data.size(); ++i) {
            std::cout << data[i];
            if (i != data.size() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};
