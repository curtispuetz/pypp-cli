#pragma once

#include "py_list.h"

using Matrix = PyList<PyList<int>>;
void type_aliases_fn();
int process_matrix(Matrix &m);