#pragma once

#include <utility>

class BaseClass {
  public:
    int a;
    BaseClass(int a_a) : a(std::move(a_a)) {}
    int add(int val);
    int add2(int val);
};
class BaseClass2 {
  public:
    int z;
    BaseClass2(int a_z) : z(std::move(a_z)) {}
    int mult2(int val);
};
class ChildClass : public BaseClass {
  public:
    int b;
    ChildClass(int a_a, int a_b) : BaseClass(a_a), b(std::move(a_b)) {}
    int add(int val);
    int multiply(int val);
};
class ChildClass2 : public ChildClass {
  public:
    int c;
    ChildClass2(int a_a, int a_b, int a_c)
        : ChildClass(a_a, a_b), c(std::move(a_c)) {}
    int add(int val);
};
class ChildMultiple : public BaseClass, public BaseClass2 {
  public:
    int c;
    ChildMultiple(int a_a, int a_b, int a_c)
        : BaseClass(a_a), BaseClass2(a_b), c(std::move(a_c)) {}
    int add(int val);
};
void class_inheritance_fn();