#pragma once

#include "exceptions/stdexcept.h"
#include "py_list.h"
#include "py_tuple.h"
#include "pypp_optional.h"
#include <format>
#include <initializer_list>
#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>

// PyDictKeys
template <typename K, typename V> class PyDictKeys {
    using MapType = std::unordered_map<K, V>;
    const MapType &map;

  public:
    explicit PyDictKeys(const MapType &m) : map(m) {}

    class iterator {
        using ItType = typename MapType::const_iterator;
        ItType it;

      public:
        using iterator_category = std::forward_iterator_tag;
        using value_type = const K;
        using difference_type = std::ptrdiff_t;
        using pointer = const K *;
        using reference = const K &;

        iterator(ItType i) : it(i) {}
        reference operator*() const { return it->first; }
        pointer operator->() const { return &(it->first); }
        iterator &operator++() {
            ++it;
            return *this;
        }
        iterator operator++(int) {
            iterator tmp = *this;
            ++it;
            return tmp;
        }
        bool operator==(const iterator &other) const { return it == other.it; }
        bool operator!=(const iterator &other) const { return it != other.it; }
    };

    iterator begin() const { return iterator(map.begin()); }
    iterator end() const { return iterator(map.end()); }

    friend std::ostream &operator<<(std::ostream &os, const PyDictKeys &keys) {
        os << "dict_keys([";
        bool first = true;
        for (const auto &key : keys) {
            if (!first)
                os << ", ";
            os << key;
            first = false;
        }
        os << "])";
        return os;
    }
};

// PyDictValues
template <typename K, typename V> class PyDictValues {
    using MapType = std::unordered_map<K, V>;
    const MapType &map;

  public:
    explicit PyDictValues(const MapType &m) : map(m) {}

    class iterator {
        using ItType = typename MapType::const_iterator;
        ItType it;

      public:
        using iterator_category = std::forward_iterator_tag;
        using value_type = const V;
        using difference_type = std::ptrdiff_t;
        using pointer = const V *;
        using reference = const V &;

        iterator(ItType i) : it(i) {}
        reference operator*() const { return it->second; }
        pointer operator->() const { return &(it->second); }
        iterator &operator++() {
            ++it;
            return *this;
        }
        iterator operator++(int) {
            iterator tmp = *this;
            ++it;
            return tmp;
        }
        bool operator==(const iterator &other) const { return it == other.it; }
        bool operator!=(const iterator &other) const { return it != other.it; }
    };

    iterator begin() const { return iterator(map.begin()); }
    iterator end() const { return iterator(map.end()); }

    friend std::ostream &operator<<(std::ostream &os,
                                    const PyDictValues &values) {
        os << "dict_values([";
        bool first = true;
        for (const auto &value : values) {
            if (!first)
                os << ", ";
            os << value;
            first = false;
        }
        os << "])";
        return os;
    }
};

// PyDictItems
template <typename K, typename V> class PyDictItems {
    using MapType = std::unordered_map<K, V>;
    const MapType &map;

  public:
    explicit PyDictItems(const MapType &m) : map(m) {}

    class iterator {
        using ItType = typename MapType::const_iterator;
        ItType it;

      public:
        using iterator_category = std::forward_iterator_tag;
        using value_type = PyTup<const K &, const V &>;
        using difference_type = std::ptrdiff_t;
        using pointer = void;
        using reference = PyTup<const K &, const V &>;

        iterator(ItType i) : it(i) {}
        reference operator*() const { return {it->first, it->second}; }
        iterator &operator++() {
            ++it;
            return *this;
        }
        iterator operator++(int) {
            iterator tmp = *this;
            ++it;
            return tmp;
        }
        bool operator==(const iterator &other) const { return it == other.it; }
        bool operator!=(const iterator &other) const { return it != other.it; }
    };

    iterator begin() const { return iterator(map.begin()); }
    iterator end() const { return iterator(map.end()); }

    friend std::ostream &operator<<(std::ostream &os,
                                    const PyDictItems &items) {
        os << "dict_items([";
        bool first = true;
        for (const auto &kv : items) {
            if (!first)
                os << ", ";
            os << "(" << kv.get<0>() << ", " << kv.get<1>() << ")";
            first = false;
        }
        os << "])";
        return os;
    }
};

template <typename K, typename V> class PyDict {
  public:
    // Underlying map
    std::unordered_map<K, V> data;

    // Constructors
    PyDict() = default;
    PyDict(std::initializer_list<std::pair<const K, V>> init) : data(init) {}

    // clear()
    void clear() { data.clear(); }

    // Note: dict is not ordered. Reverse iterators are not meaningful.
    PyDictKeys<K, V> keys() const { return PyDictKeys<K, V>(data); }
    PyDictValues<K, V> values() const { return PyDictValues<K, V>(data); }
    PyDictItems<K, V> items() const { return PyDictItems<K, V>(data); }

    // opeartor[] allows for read-only access, like Python's dict[x]
    // dg == dict get. matches pypp's naming
    V &dg(const K &key) {
        auto it = data.find(key);
        if (it == data.end())
            throw PyppKeyError("dict[x]: x not in dict");
        return it->second;
    }

    // get_opt(key)
    PyppOpt<V> dg_opt(const K &key) {
        auto it = data.find(key);
        if (it != data.end())
            return PyppOpt<V>(it->second);
        return PyppOpt<V>();
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
        throw PyppKeyError("dict.pop(x): x not in dict");
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

    // operator[] allows for assignment, like Pythons dict[x] = y
    V &operator[](const K &key) { return data[key]; }

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

namespace std {
// formatter for std::format
template <typename K, typename V> struct formatter<PyDict<K, V>, char> {
    constexpr auto parse(format_parse_context &ctx) { return ctx.begin(); }

    template <typename FormatContext>
    auto format(const PyDict<K, V> &dict, FormatContext &ctx) const {
        std::ostringstream oss;
        dict.print(oss);
        return std::format_to(ctx.out(), "{}", oss.str());
    }
};
} // namespace std