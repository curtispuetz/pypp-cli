#pragma once

#include "py_str.h"
#include <utility>

struct FirstDataClass {
    PyStr field1;
    int field2;
    FirstDataClass(PyStr a_field1, int a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};
struct DataClassWithReference {
    PyStr &field1;
    int field2;
    DataClassWithReference(PyStr &a_field1, int a_field2)
        : field1(a_field1), field2(std::move(a_field2)) {}
};
struct FrozenDataClass {
    const PyStr field1;
    const int field2;
    FrozenDataClass(PyStr a_field1, int a_field2)
        : field1(std::move(a_field1)), field2(std::move(a_field2)) {}
};
struct FrozenDataClassWithReference {
    const PyStr &field1;
    const int field2;
    FrozenDataClassWithReference(PyStr &a_field1, int a_field2)
        : field1(a_field1), field2(std::move(a_field2)) {}
};
void dataclass_fn();