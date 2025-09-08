#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_tuple.h"

namespace pypp {

template <typename T, typename U> PyDict<T, U> dict(const PyDict<T, U> &dict) {
    return PyDict<T, U>(dict.data.begin(), dict.data.end());
}

// TODO: check if I need to use .template get in Py++ generated code.
template <typename T, typename U>
PyDict<T, U> dict(const PyList<PyTup<T, U>> &lst_of_tuples) {
    PyDict<T, U> dict;
    for (const auto &tup : lst_of_tuples) {
        dict[std::move(tup.template get<0>())] =
            std::move(tup.template get<1>());
    }
    return dict;
}

template <typename T, typename U> PyDict<T, U> dict() { return PyDict<T, U>(); }

} // namespace pypp