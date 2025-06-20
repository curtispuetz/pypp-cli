#pragma once

#include "py_enumerate.h"
#include "py_list.h"

void enumerate_fn();
void _enumerate_as_arg(PyEnumerate<PyList<int>> en);