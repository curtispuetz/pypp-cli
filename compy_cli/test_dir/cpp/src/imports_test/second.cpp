#include "imports_test/second.h"
#include "compy_util/print.h"
#include "constants.h"
#include "py_str.h"

void imports_test_fn2() {
    print(PyStr("IMPORTS TEST RESULTS 2:"));
    print(C);
    print(MyConfig2.a, MyConfig2.b);
}
