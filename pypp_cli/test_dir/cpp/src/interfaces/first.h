#pragma once

#include "py_str.h"

class InterfaceClass {
  public:
    virtual void speak(int a) = 0;
    virtual PyStr talk() = 0;
    virtual ~InterfaceClass() {}
};

class Impl1 : public InterfaceClass {
  public:
    void speak(int a);
    PyStr talk();
};

class Impl2 : public InterfaceClass {
  public:
    void speak(int a);
    PyStr talk();
};

void interfaces_fn();