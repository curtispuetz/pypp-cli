#pragma once

#include <utility>

class BaseClass {
  public:
    int a;
    BaseClass(int a_a) : a(std::move(a_a)) {}
    int add(int val);
    int add2(int val);
};
class ChildClass : public BaseClass {
  public:
    int b;
    ChildClass(int a_a, int a_b) : BaseClass(a_a), b(std::move(a_b)) {}
    int add(int val);
    int multiply(int val);
};
void class_inheritance_fn();