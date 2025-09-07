#pragma once

#include "py_list.h"

namespace me {
void list_as_arg(pypp::PyList<int> &a);
void list_as_mutable_arg(pypp::PyList<int> &a);
} // namespace me