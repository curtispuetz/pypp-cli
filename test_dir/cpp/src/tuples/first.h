#pragma once

#include "py_str.h"
#include "py_tuple.h"

void tuples_fn();
void _inline_tuple(const PyTup<double, PyStr> &tup);
PyTup<int, double> get_tup();