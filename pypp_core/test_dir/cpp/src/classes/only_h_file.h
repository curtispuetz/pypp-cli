#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"

class OnlyHClass {
  public:
    PyList<double> &field1;
    PyDict<PyStr, PySet<int>> &field2;
    OnlyHClass(PyList<double> &a_field1, PyDict<PyStr, PySet<int>> &a_field2)
        : field1(a_field1), field2(a_field2) {}
};
