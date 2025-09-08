#pragma once

#include "py_dict.h"
#include "py_dict_default.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"

namespace pypp {
template <typename T> PyList<T> list(const PySet<T> &set) {
    return PyList<T>(set.begin(), set.end());
}

template <typename T> PyList<T> list(const PyList<T> &lst) {
    return PyList<T>(lst);
}

template <typename T, typename U> PyList<T> list(const PyDict<T, U> &dict) {
    auto keys = dict.keys();
    return PyList<T>(keys.begin(), keys.end());
}

template <typename T, typename U>
PyList<T> list(const PyDefaultDict<T, U> &dict) {
    auto keys = dict.keys();
    return PyList<T>(keys.begin(), keys.end());
}

PyList<PyStr> list(const PyStr &s);

template <typename T> PyList<T> list() { return PyList<T>(); }

} // namespace pypp
