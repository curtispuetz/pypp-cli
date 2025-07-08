#pragma once

#include "py_str.h"
#include <utility>

class ClassA {
  public:
    int a;
    PyStr &b;
    ClassA(int a_a, PyStr &a_b) : a(std::move(a_a)), b(a_b) {}
    int add(int c);
};

class ClassWithPassByValue {
  public:
    int a;
    PyStr b;
    ClassWithPassByValue(int a_a, PyStr a_b)
        : a(std::move(a_a)), b(std::move(a_b)) {}
};

void classes_fn();