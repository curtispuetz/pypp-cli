#include "fn_as_vars\first.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <functional>

PyStr _test_fn(int a, int b) { return PyStr(std::format("{} {}", a, b)); }

void _test_fn2(std::function<double()> &fn) { print(fn()); }

double _test_fn3() { return 2.71; }

void _test_fn4(int a) { print(a); }

void _test_fn5() { print(PyStr("test fn5 called")); }

void fn_as_vars_fn() {
    print(PyStr("FN_AS_VARS RESULTS:"));
    std::function<PyStr(int, int)> fn_var = _test_fn;
    print(fn_var(1, 2));
    std::function<double()> a = _test_fn3;
    _test_fn2(a);
    std::function<void(int)> b = _test_fn4;
    b(5);
    std::function<void()> c = _test_fn5;
    c();
}
