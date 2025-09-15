#include "src/imports_test/first.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "src/constants.h"

namespace me {
void imports_test_fn() {
    pypp::print(pypp::PyStr("IMPORTS TEST RESULTS:"));
    pypp::print(me::C);
    pypp::print(me::MyConfig2.a, me::MyConfig2.b);
}

} // namespace me