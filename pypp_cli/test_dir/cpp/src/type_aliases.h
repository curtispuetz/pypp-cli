#pragma once

#include "py_list.h"

using Matrix = pypp::PyList<pypp::PyList<int>>;
void type_aliases_fn();
using L = pypp::PyList<int>;
int process_matrix(Matrix &m);