#include "src/custom_libs/pure_lib_test_0/first.h"
#include "py_str.h"
#include "pypp_pure_library_test_0/first.h"
#include "pypp_util/print.h"

namespace me {
void pure_lib_test_0_fn() {
    pypp::print(pypp::PyStr("PURE LIB TEST 0 RESULTS:"));
    first_fn();
}

} // namespace me