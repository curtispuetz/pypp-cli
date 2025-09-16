#pragma once

#include "py_list.h"
#include "py_str.h"

namespace me {
void pseudo_fn(pypp::PyList<int> &integers, pypp::PyList<pypp::PyStr> &strings);
} // namespace me