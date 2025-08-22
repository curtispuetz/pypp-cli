#pragma once

#include "compy_union.h"
#include <utility>

class ClassWithUnion {
  public:
    Uni<int, double> &value;
    ClassWithUnion(Uni<int, double> &a_value) : value(a_value) {}
    int calc();
};

class ClassWithUnionByValue {
  public:
    Uni<int, double> value;
    ClassWithUnionByValue(Uni<int, double> a_value)
        : value(std::move(a_value)) {}
};

void compy_union_fn();