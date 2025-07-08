#include "fn_as_vars\first.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <functional>

PyStr _test_fn(int a, int b) { return PyStr(std::format("{} {}", a, b)); }

void fn_as_vars_fn() {
    print(PyStr("FN_AS_VARS RESULTS:"));
    std::function<PyStr(int, int)> fn_var = _test_fn;
    print(fn_var(1, 2));
}
