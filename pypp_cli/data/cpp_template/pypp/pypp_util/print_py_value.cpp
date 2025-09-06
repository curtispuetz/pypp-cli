#include "pypp_util/print_py_value.h"
#include "py_str.h"

namespace pypp {

void print_py_value(std::ostream &os, const PyStr &value) {
    os << "'" << value << "'";
}

} // namespace pypp