#pragma once

#include <unordered_map>
#include <vector>
#include <optional>
#include <stdexcept>
#include <iostream>
#include <utility>
#include <initializer_list>
#include "py_list.h"
#include "py_tuple.h"


template<typename K, typename V>
class PyDict {
public:
    // Underlying map
    std::unordered_map<K, V> data;

    // Constructors
    PyDict() = default;
    PyDict(std::initializer_list<std::pair<const K, V>> init) : data(init) {}

    // clear()
    void clear() {
        data.clear();
    }

    // keys()
    PyList<K> keys() const {
        std::vector<K> result;
        for (const auto& [key, _] : data)
            result.push_back(key);
        return PyList(result);
    }

    // values()
    PyList<V> values() const {
        std::vector<V> result;
        for (const auto& [_, value] : data)
            result.push_back(value);
        return PyList(result);
    }

    // items()
    PyList<PyTup<K, V>> items() const {
        std::vector<PyTup<K, V>> result;
        for (const auto& pair : data)
            result.push_back(PyTup(pair.first, pair.second));
        return PyList(result);
    }

    // get(key)
    std::optional<V> get(const K& key) const {
        auto it = data.find(key);
        if (it != data.end())
            return it->second;
        return std::nullopt;
    }

    V get(const K& key, const V& default_value) const {
        auto it = data.find(key);
        if (it != data.end())
            return it->second;
        return default_value;
    }

    // update(other_dict)
    void update(const PyDict<K, V>& other) {
        for (const auto& [key, value] : other.data)
            data[key] = value;
    }

    // pop(key, default)
    V pop(const K& key, const V& default_value) {
        auto it = data.find(key);
        if (it != data.end()) {
            V value = it->second;
            data.erase(it);
            return value;
        }
        return default_value;
    }

    // setdefault(key, default)
    V& setdefault(const K& key, const V& default_value) {
        auto [it, inserted] = data.emplace(key, default_value);
        return it->second;
    }

    // contains(key)
    // TODO: will I use this instead of IN?
    bool contains(const K& key) const {
        return data.find(key) != data.end();
    }

    // operator[] access/assignment like Python
    V& operator[](const K& key) {
        return data[key];
    }
    const V& operator[](const K& key) const {
        auto it = data.find(key);
        if (it == data.end()) throw std::out_of_range("Key not found");
        return it->second;
    }

    // Size
    size_t len() const {
        return data.size();
    }

    // copy()
    PyDict<K, V> copy() const {
        PyDict<K, V> new_dict;
        new_dict.data = data;
        return new_dict;
    }

    // static fromkeys()
    static PyDict<K, V> fromkeys(const std::vector<K>& keys, const V& value) {
        PyDict<K, V> new_dict;
        for (const auto& key : keys)
            new_dict.data[key] = value;
        return new_dict;
    }

    // popitem()
    std::pair<K, V> popitem() {
        if (data.empty())
            throw std::out_of_range("popitem(): dictionary is empty");
        auto it = data.begin();
        auto item = *it;
        data.erase(it);
        return item;
    }

    // Print
    void print() const {
        std::cout << "{";
        bool first = true;
        for (const auto& [key, value] : data) {
            if (!first) std::cout << ", ";
            first = false;
            std::cout << key << ": " << value;
        }
        std::cout << "}" << std::endl;
    }
};
