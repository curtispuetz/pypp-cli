#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"

namespace pypp {
template <typename T> PySet<T> set(const PySet<T> &set) {
    return PySet<T>(set.begin(), set.end());
}

template <typename T> PySet<T> set(const PyList<T> &lst) {
    return PySet<T>(lst.begin(), lst.end());
}

template <typename T, typename U> PySet<T> set(const PyDict<T, U> &dict) {
    auto keys = dict.keys();
    return PySet<T>(keys.begin(), keys.end());
}

PySet<PyStr> set(const PyStr &s);

}