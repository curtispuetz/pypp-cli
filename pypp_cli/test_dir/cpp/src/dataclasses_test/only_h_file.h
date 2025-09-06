#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include <utility>

struct OnlyHDataClass {
    pypp::PyList<double> field1;
    pypp::PyDict<pypp::PyStr, pypp::PySet<int>> field2;
    OnlyHDataClass(pypp::PyList<double> a_field1,
                   pypp::PyDict<pypp::PyStr, pypp::PySet<int>> a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};
