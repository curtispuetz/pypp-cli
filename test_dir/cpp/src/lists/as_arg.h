#pragma once

#include "py_list.h"
#include "pypp_util/print.h"

void list_as_arg(const PyList<int> &a);
void list_as_mutable_arg(PyList<int> &a);