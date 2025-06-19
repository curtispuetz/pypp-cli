#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"

void dict_fn();
void _fn_dict_arg(const PyDict<int, int> &d);