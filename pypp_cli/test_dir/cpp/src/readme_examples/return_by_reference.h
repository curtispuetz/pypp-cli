#pragma once

#include "py_list.h"

namespace me {
pypp::PyList<int> &return_by_reference_fn(pypp::PyList<int> &a,
                                          pypp::PyList<int> &b);
} // namespace me