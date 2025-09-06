#pragma once

#include "pypp_union.h"
#include <utility>

class ClassWithUnion {
  public:
    pypp::Uni<int, double> &value;
    ClassWithUnion(pypp::Uni<int, double> &a_value) : value(a_value) {}
    int calc();
};

class ClassWithUnionByValue {
  public:
    pypp::Uni<int, double> value;
    ClassWithUnionByValue(pypp::Uni<int, double> a_value)
        : value(std::move(a_value)) {}
};

void pypp_union_fn();