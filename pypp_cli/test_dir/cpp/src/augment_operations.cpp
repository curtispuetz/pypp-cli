#include "augment_operations.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void augment_operations_fn() {
    pypp::print(pypp::PyStr("AUGMENT OPERATIONS RESULTS:"));
    int a = 1000;
    double b = 2.5;
    a += 3;
    pypp::print(a);
    a -= 2;
    pypp::print(a);
    a *= 4;
    pypp::print(a);
    b /= 3;
    pypp::print(b);
    a %= 3;
    pypp::print(a);
    a <<= 2;
    pypp::print(a);
    a >>= 1;
    pypp::print(a);
    a &= 6;
    pypp::print(a);
}

} // namespace me