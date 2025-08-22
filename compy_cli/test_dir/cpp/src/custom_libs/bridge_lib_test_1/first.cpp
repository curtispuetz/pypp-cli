#include "custom_libs/bridge_lib_test_1/first.h"
#include "compy_bridge_library_test_1/first.h"
#include "compy_bridge_library_test_1/first_folder/third.h"
#include "compy_bridge_library_test_1/fourth.h"
#include "compy_bridge_library_test_1/second_other_name.h"
#include "py_str.h"
#include "pypp_util/print.h"

void bridge_lib_test_1_fn() {
    print(PyStr("compy BRIDGE LIB TEST 1 RESULTS:"));
    print(pseudo_fn());
    print(pseudo_fn_a());
    print(pseudo_fn_b());
    print(pseudo_namespace::pseudo_fn_c());
}
