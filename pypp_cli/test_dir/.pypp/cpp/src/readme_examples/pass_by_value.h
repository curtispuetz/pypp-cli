#pragma once

#include "py_list.h"

namespace me {
pypp::PyList<int> pass_by_value_fn(pypp::PyList<int> a, pypp::PyList<int> _b);
} // namespace me