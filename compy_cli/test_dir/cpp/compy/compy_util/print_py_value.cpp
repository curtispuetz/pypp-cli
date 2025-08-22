#include "compy_util/print_py_value.h"
#include "py_str.h"

void print_py_value(std::ostream &os, const PyStr &value) {
    os << "'" << value << "'";
}