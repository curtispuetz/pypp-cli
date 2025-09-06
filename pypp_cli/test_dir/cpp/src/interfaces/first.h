#pragma once

#include "py_str.h"

namespace me {
class InterfaceClass {
  public:
    virtual void speak(int a) = 0;
    virtual pypp::PyStr talk() = 0;
    virtual ~InterfaceClass() {}
};

class Impl1 : public InterfaceClass {
  public:
    void speak(int a);
    pypp::PyStr talk();
};

class Impl2 : public InterfaceClass {
  public:
    void speak(int a);
    pypp::PyStr talk();
};

void interfaces_fn();
} // namespace me