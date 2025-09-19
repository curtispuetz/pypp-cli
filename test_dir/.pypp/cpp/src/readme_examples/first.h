#pragma once

#include "py_list.h"

namespace me {
pypp::PyList<int> list_add(pypp::PyList<int> &a, pypp::PyList<int> &b,
                           int mult_factor);
}