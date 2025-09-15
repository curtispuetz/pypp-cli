#include "src/imports_test/second.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "src/constants.h"

namespace me {
void imports_test_fn2() {
    pypp::print(pypp::PyStr("IMPORTS TEST RESULTS 2:"));
    pypp::print(me::C);
    pypp::print(me::MyConfig2.a, me::MyConfig2.b);
}

} // namespace me