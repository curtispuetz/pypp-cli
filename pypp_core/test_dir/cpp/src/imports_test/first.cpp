#include "imports_test\first.h"
#include "constants.h"
#include "py_str.h"
#include "pypp_util/print.h"

void imports_test_fn() {
    print(PyStr("IMPORTS TEST RESULTS:"));
    print(C);
    print(MyConfig2.a, MyConfig2.b);
}
