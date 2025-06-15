#pragma once

#include "py_list.h"
#include "py_tuple.h"
#include <initializer_list>
#include <iostream>
#include <optional>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>

template <typename K, typename V> class PyDict {
  public:
    // Underlying map
    std::unordered_map<K, V> data;

    // Constructors
    PyDict() = default;
    PyDict(std::initializer_list<std::pair<const K, V>> init) : data(init) {}

    // clear()
    void clear() { data.clear(); }

    // keys()
    PyList<K> keys() const {
        std::vector<K> result;
        for (const auto &[key, _] : data)
            result.push_back(key);
        return PyList(result);
    }

    // values()
    PyList<V> values() const {
        std::vector<V> result;
        for (const auto &[_, value] : data)
            result.push_back(value);
        return PyList(result);
    }

    // items()
    PyList<PyTup<K, V>> items() const {
        std::vector<PyTup<K, V>> result;
        for (const auto &pair : data)
            result.push_back(PyTup(pair.first, pair.second));
        return PyList(result);
    }

    // get(key)
    std::optional<V> get(const K &key) const {
        auto it = data.find(key);
        if (it != data.end())
            return it->second;
        return std::nullopt;
    }

    V get(const K &key, const V &default_value) const {
        auto it = data.find(key);
        if (it != data.end())
            return it->second;
        return default_value;
    }

    // update(other_dict)
    void update(const PyDict<K, V> &other) {
        for (const auto &[key, value] : other.data)
            data[key] = value;
    }

    // pop(key, default)
    V pop(const K &key) {
        auto it = data.find(key);
        if (it != data.end()) {
            V value = it->second;
            data.erase(it);
            return value;
        }
        throw std::invalid_argument("key not in dict");
    }

    V pop(const K &key, const V &default_value) {
        auto it = data.find(key);
        if (it != data.end()) {
            V value = it->second;
            data.erase(it);
            return value;
        }
        return default_value;
    }

    // setdefault(key, default)
    V &setdefault(const K &key, const V &default_value) {
        auto [it, inserted] = data.emplace(key, default_value);
        return it->second;
    }

    // contains(key)
    bool contains(const K &key) const { return data.find(key) != data.end(); }

    // operator[] access/assignment like Python
    V &operator[](const K &key) { return data[key]; }
    const V &operator[](const K &key) const {
        auto it = data.find(key);
        if (it == data.end())
            throw std::out_of_range("Key not found");
        return it->second;
    }

    // Size
    int len() const { return data.size(); }

    // copy()
    PyDict<K, V> copy() const {
        PyDict<K, V> new_dict;
        new_dict.data = data;
        return new_dict;
    }

    // TODO later: support dict.fromkeys
    // NOTE: the popitem() method is not supported because this map is not
    // ordered by the insertion order of the items like the Python dict is.

    // Print
    void print(std::ostream &os) const {
        os << "{";
        bool first = true;
        for (const auto &[key, value] : data) {
            if (!first)
                os << ", ";
            first = false;
            os << key << ": " << value;
        }
        os << "}";
    }

    void print() const {
        print(std::cout);
        std::cout << std::endl;
    }

    template <typename U, typename Z>
    friend std::ostream &operator<<(std::ostream &os, const PyDict<U, Z> &dict);
};

template <typename K, typename V>
std::ostream &operator<<(std::ostream &os, const PyDict<K, V> &dict) {
    dict.print(os);
    return os;
}
