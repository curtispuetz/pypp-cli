#include "ternary_op.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void ternary_op_fn() {
    pypp::print(pypp::PyStr("TERNARY OP RESULTS:"));
    int a = 5;
    int b = 10;
    int max_value = (a > b) ? a : b;
    pypp::print(max_value);
}

} // namespace me