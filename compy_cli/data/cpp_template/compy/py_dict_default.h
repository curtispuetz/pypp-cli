#pragma once

#include "py_dict.h"
#include <functional>

// PyDefaultDict: a light wrapper around PyDict that mimics Python's
// collections.defaultdict Usage: PyDefaultDict<Key, Value> d([]{ return
// default_value; });
//        d[key] returns d[key] if present, else inserts and returns
//        default_value.
template <typename K, typename V, typename DefaultFactory = std::function<V()>>
class PyDefaultDict {
  public:
    PyDict<K, V> data;
    DefaultFactory default_factory;

    // Constructors
    PyDefaultDict(DefaultFactory factory) : default_factory(factory) {}

    // operator[]: returns value if present, else inserts default from factory
    V &operator[](const K &key) {
        auto it = data.data.find(key);
        if (it == data.data.end()) {
            V value = default_factory();
            auto [inserted_it, _] = data.data.emplace(key, std::move(value));
            return inserted_it->second;
        }
        return it->second;
    }

    // at/dg: like dict.get, but inserts default if missing
    V &dg(const K &key) { return (*this)[key]; }

    // Expose PyDict-like methods
    void clear() { data.clear(); }
    int len() const { return data.len(); }
    auto keys() const { return data.keys(); }
    auto values() const { return data.values(); }
    auto items() const { return data.items(); }
    bool contains(const K &key) const { return data.contains(key); }
    void update(PyDict<K, V> &&other) { data.update(std::move(other)); }
    V pop(const K &key) { return data.pop(key); }
    V pop(const K &key, const V &default_value) {
        return data.pop(key, default_value);
    }
    V &setdefault(const K &&key, V &&default_value) {
        return data.setdefault(std::move(key), std::move(default_value));
    }
    PyDefaultDict copy() const {
        return PyDefaultDict(default_factory, data.data);
    }

    // Print
    void print(std::ostream &os) const {
        os << "defaultdict(";
        data.print(os);
        os << ")";
    }

    // Stream output
    friend std::ostream &operator<<(std::ostream &os, const PyDefaultDict &d) {
        d.print(os);
        return os;
    }

    static PyDefaultDict bool_factory() {
        return PyDefaultDict([] { return false; });
    }
    static PyDefaultDict int_factory() {
        return PyDefaultDict([] { return 0; });
    }
    static PyDefaultDict float_factory() {
        // Note: this is double in C++, but float in Python.
        return PyDefaultDict([] { return 0.0; });
    }
    static PyDefaultDict str_factory() {
        return PyDefaultDict([] { return PyStr(); });
    }
    template <typename T2 = V> static PyDefaultDict list_factory() {
        return PyDefaultDict([] { return PyList<typename T2::value_type>(); });
    }
    template <typename T2 = V> static PyDefaultDict set_factory() {
        return PyDefaultDict([] { return PySet<typename T2::value_type>(); });
    }
    template <typename T2 = V> static PyDefaultDict dict_factory() {
        return PyDefaultDict([] {
            return PyDict<typename T2::key_type, typename T2::value_type>();
        });
    }
};
