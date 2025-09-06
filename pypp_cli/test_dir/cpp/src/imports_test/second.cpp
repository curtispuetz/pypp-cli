#include "imports_test/second.h"
#include "constants.h"
#include "py_str.h"
#include "pypp_util/print.h"

void imports_test_fn2() {
    pypp::print(pypp::PyStr("IMPORTS TEST RESULTS 2:"));
    pypp::print(C);
    pypp::print(MyConfig2.a, MyConfig2.b);
}
