#pragma once

#include "py_list.h"
#include "py_str.h"
#include <utility>

namespace me {
struct MyType {
    const pypp::PyStr field1;
    const pypp::PyList<int> field2;
    MyType(pypp::PyStr a_field1, pypp::PyList<int> a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};

MyType my_type_factory(pypp::PyList<int> a);
void pass_by_value_test_fn();
} // namespace me