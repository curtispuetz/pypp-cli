#pragma once

#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"

void set_fn();
void _inline_set(const PySet<double> &s);