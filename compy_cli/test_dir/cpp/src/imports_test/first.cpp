#include "imports_test/first.h"
#include "compy_util/print.h"
#include "constants.h"
#include "py_str.h"

void imports_test_fn() {
    print(PyStr("IMPORTS TEST RESULTS:"));
    print(C);
    print(MyConfig2.a, MyConfig2.b);
}
