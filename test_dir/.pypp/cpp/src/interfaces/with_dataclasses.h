#pragma once

#include "py_str.h"
#include <utility>

namespace me {
class GreeterInterface {
  public:
    virtual void greet(int a) = 0;
    virtual ~GreeterInterface() {}
};

struct GreeterImpl : public GreeterInterface {
    pypp::PyStr name;
    GreeterImpl(pypp::PyStr a_name) : name(std::move(a_name)) {}
    void greet(int a);
};

void interface_with_dataclasses_fn();
} // namespace me