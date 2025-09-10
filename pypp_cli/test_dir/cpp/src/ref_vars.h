#pragma once

#include "py_list.h"

namespace me {
pypp::PyList<int> &repeat(pypp::PyList<int> &a);
pypp::PyList<int> repeat_new(pypp::PyList<int> &a);
void ref_vars_fn();
} // namespace me