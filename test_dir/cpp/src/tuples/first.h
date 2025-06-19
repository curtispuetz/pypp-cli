#pragma once

#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <any>

void tuples_fn();
void _inline_tuple(const PyTup<double, PyStr> &tup);