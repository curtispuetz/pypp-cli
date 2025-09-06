#pragma once

#include "py_str.h"

class Greeter {
  public:
    pypp::PyStr &name;
    pypp::PyStr &prefix;
    Greeter(pypp::PyStr &a_name, pypp::PyStr &a_prefix)
        : name(a_name), prefix(a_prefix) {}
    pypp::PyStr greet();
};
