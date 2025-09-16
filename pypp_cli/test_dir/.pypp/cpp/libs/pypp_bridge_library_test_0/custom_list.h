#pragma once
#include "py_list.h"

template <typename T>
class PseudoCustomList
{
public:
    PseudoCustomList(pypp::PyList<T> elements) : elements_(elements) {}

private:
    pypp::PyList<T> elements_;
};
