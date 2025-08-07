#pragma once

#include "py_str.h"
#include "py_tuple.h"
#include <functional>
#include <utility>

class TestClass {
  public:
    void t(std::function<void()> &fn);
};

struct TestDataClass {
    int a;
    TestDataClass(int a_a) : a(std::move(a_a)) {}
    void t(std::function<void()> &fn);
};

void fn_as_vars_fn();