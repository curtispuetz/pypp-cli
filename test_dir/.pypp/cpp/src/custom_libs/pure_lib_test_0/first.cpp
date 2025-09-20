#include "src/custom_libs/pure_lib_test_0/first.h"
#include "py_str.h"
#include "pypp_pure_library_test_0.h"
#include "pypp_util/print.h"

namespace me {
void pure_lib_test_0_fn() {
    pypp::print(pypp::PyStr("PURE LIB TEST 0 RESULTS:"));
    pure_test_0::first_fn();
    pure_test_0::hello_world_fn();
}

} // namespace me