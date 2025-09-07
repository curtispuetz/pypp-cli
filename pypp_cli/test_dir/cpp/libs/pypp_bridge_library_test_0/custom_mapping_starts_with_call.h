#pragma once

#include "py_str.h"
#include "pypp_util/print.h"

template <typename T>
class PseudoGeneric
{
public:
    PseudoGeneric(T value) { _value = value; }

    static PseudoGeneric<pypp::PyStr> string_factory()
    {
        return PseudoGeneric<pypp::PyStr>(pypp::PyStr("default string"));
    }

    void print_value() const { pypp::print(_value); }

private:
    T _value;
};
