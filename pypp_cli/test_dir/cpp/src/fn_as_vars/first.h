#pragma once

#include <functional>
#include <utility>

namespace me {
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
} // namespace me