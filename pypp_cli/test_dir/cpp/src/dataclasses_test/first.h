#pragma once

#include "py_str.h"
#include <utility>

namespace me {
struct FirstDataClass {
    pypp::PyStr field1;
    int field2;
    FirstDataClass(pypp::PyStr a_field1, int a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};

struct DataClassWithReference {
    pypp::PyStr &field1;
    int field2;
    DataClassWithReference(pypp::PyStr &a_field1, int a_field2)
        : field1(a_field1), field2(std::move(a_field2)) {}
};

struct FrozenDataClass {
    const pypp::PyStr field1;
    const int field2;
    FrozenDataClass(pypp::PyStr a_field1, int a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};

struct FrozenDataClassWithReference {
    const pypp::PyStr &field1;
    const int field2;
    FrozenDataClassWithReference(pypp::PyStr &a_field1, int a_field2)
        : field1(a_field1), field2(std::move(a_field2)) {}
};

void dataclass_fn();
} // namespace me