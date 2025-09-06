#include "custom_libs/bridge_lib_test_1/first.h"
#include "py_str.h"
#include "pypp_bridge_library_test_1/first.h"
#include "pypp_bridge_library_test_1/first_folder/third.h"
#include "pypp_bridge_library_test_1/fourth.h"
#include "pypp_bridge_library_test_1/second_other_name.h"
#include "pypp_util/print.h"

void bridge_lib_test_1_fn() {
    pypp::print(pypp::PyStr("pypp BRIDGE LIB TEST 1 RESULTS:"));
    pypp::print(pseudo_fn());
    pypp::print(pseudo_fn_a());
    pypp::print(pseudo_fn_b());
    pypp::print(pseudo_namespace::pseudo_fn_c());
}
