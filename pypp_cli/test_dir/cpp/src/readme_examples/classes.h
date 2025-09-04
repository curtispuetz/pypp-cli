#pragma once

#include "py_str.h"

class Greeter {
  public:
    PyStr &name;
    PyStr &prefix;
    Greeter(PyStr &a_name, PyStr &a_prefix) : name(a_name), prefix(a_prefix) {}
    PyStr greet();
};
