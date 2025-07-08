#include "fn_as_vars\first.h"
#include "pypp_util/print.h"

PyStr _test_fn(int a, int b) { return PyStr(std::format("{} {}", a, b)); }

void _test_fn2(std::function<double()> &fn) { print(fn()); }

double _test_fn3() { return 2.71; }

void _test_fn4(int a) { print(a); }

void _test_fn5() { print(PyStr("test fn5 called")); }

void _test_fn6(std::function<PyStr(int, int)> fn) { print(fn(1, 2)); }

void TestClass::t(std::function<void()> &fn) { fn(); }

void TestDataClass::t(std::function<void()> &fn) { fn(); }

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
    TestClass d = TestClass();
    d.t(c);
    TestDataClass e = TestDataClass(1);
    e.t(c);
    std::function<PyStr(int, int)> f = [](auto x, auto y) {
        return PyStr(
            std::format("Lambda {}", PyTup(std::move(x), std::move(y))));
    };
    print(f(3, 4));
    _test_fn6([](auto x, auto y) {
        return PyStr(
            std::format("Lambda {}", PyTup(std::move(x), std::move(y))));
    });
}
