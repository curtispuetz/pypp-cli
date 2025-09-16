#pragma once

#include "py_list.h"

namespace me {
void modifying_a_ref(pypp::PyList<int> &l);
void reassigning_a_ref_fn();
} // namespace me