#pragma once

#include "py_list.h"
#include "py_slice.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"

void list_fn();
void _test_fn(const PyList<PyStr> &arg1);