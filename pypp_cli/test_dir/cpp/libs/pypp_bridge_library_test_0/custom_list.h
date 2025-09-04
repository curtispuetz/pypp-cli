#pragma once
#include "py_list.h"

template <typename T>
class PseudoCustomList
{
public:
    PseudoCustomList(PyList<T> elements) : elements_(elements) {}

private:
    PyList<T> elements_;
};
