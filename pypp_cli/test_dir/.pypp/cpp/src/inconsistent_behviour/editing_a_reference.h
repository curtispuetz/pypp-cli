#pragma once

#include "py_list.h"

namespace me {
void editing_a_reference_fn();
pypp::PyList<int> update_and_return_new(pypp::PyList<int> &l1);
} // namespace me