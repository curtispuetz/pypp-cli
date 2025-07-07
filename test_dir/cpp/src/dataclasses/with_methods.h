#pragma once

#include <utility>

struct DataClassWithMethods {
    int field1;
    DataClassWithMethods(int a_field1) : field1(std::move(a_field1)) {}
    int add(int x);
    int subtract(int x);
};
void dataclass_with_methods_fn();