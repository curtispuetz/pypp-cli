#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include <utility>

struct OnlyHDataClass {
    PyList<double> field1;
    PyDict<PyStr, PySet<int>> field2;
    OnlyHDataClass(PyList<double> a_field1, PyDict<PyStr, PySet<int>> a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};