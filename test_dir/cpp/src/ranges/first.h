#pragma once

#include "py_list.h"
#include "py_range.h"
#include "py_str.h"
#include "pypp_util/print.h"

void ranges_fn();
void _iter_and_print(PyRange arg1);
PyRange _range_as_return();