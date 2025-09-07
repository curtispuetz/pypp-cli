#include "lists/as_arg.h"
#include "pypp_util/print.h"

namespace me {
void list_as_arg(pypp::PyList<int> &a) {
    pypp::PyList<int> b = a * 2;
    pypp::print(b);
}

void list_as_mutable_arg(pypp::PyList<int> &a) {
    a *= 3;
    pypp::print(a);
}

} // namespace me