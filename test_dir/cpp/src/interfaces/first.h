#pragma once

#include "py_str.h"
#include <utility>

class InterfaceClass {
  public:
    virtual void speak(int a) = 0;
    virtual PyStr talk() = 0;
    virtual ~InterfaceClass() {}
};

class Impl1 : public InterfaceClass {
  public:
    int dummy;
    Impl1(int a_dummy) : dummy(std::move(a_dummy)) {}
    void speak(int a);
    PyStr talk();
};

class Impl2 : public InterfaceClass {
  public:
    int dummy;
    Impl2(int a_dummy) : dummy(std::move(a_dummy)) {}
    void speak(int a);
    PyStr talk();
};

void interfaces_fn();