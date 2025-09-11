#pragma once

#include "py_str.h"

namespace me {
class InterfaceClass {
  public:
    virtual void speak(int a) = 0;
    virtual pypp::PyStr talk() = 0;
    virtual ~InterfaceClass() {}
};

struct Impl1 : public InterfaceClass {
    Impl1() {}
    void speak(int a);
    pypp::PyStr talk();
};

struct Impl2 : public InterfaceClass {
    Impl2() {}
    void speak(int a);
    pypp::PyStr talk();
};

void interfaces_fn();
} // namespace me