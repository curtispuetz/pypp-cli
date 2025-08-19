#include "pypp_util/print.h"
#include "py_str.h"

template <typename T>
class PseudoGeneric
{
public:
    PseudoGeneric(T value)
    {
        _value = value;
    }

    static PseudoGeneric<PyStr> string_factory()
    {
        return PseudoGeneric<PyStr>(PyStr("default string"));
    }

    void print_value() const
    {
        print(_value);
    }

private:
    T _value;
};
