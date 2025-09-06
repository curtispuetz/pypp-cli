#include "imports_test/first.h"
#include "constants.h"
#include "py_str.h"
#include "pypp_util/print.h"

void imports_test_fn() {
    pypp::print(pypp::PyStr("IMPORTS TEST RESULTS:"));
    pypp::print(C);
    pypp::print(MyConfig2.a, MyConfig2.b);
}
