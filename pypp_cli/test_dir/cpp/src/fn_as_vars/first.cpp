#include "fn_as_vars/first.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

pypp::PyStr _test_fn(int a, int b) {
    return pypp::PyStr(std::format("{} {}", a, b));
}

void _test_fn2(std::function<double()> &fn) { pypp::print(fn()); }

double _test_fn3() { return 2.71; }

void _test_fn4(int a) { pypp::print(a); }

void _test_fn5() { pypp::print(pypp::PyStr("test fn5 called")); }

void _test_fn6(std::function<pypp::PyStr(int, int)> fn) {
    pypp::print(fn(1, 2));
}

void TestClass::t(std::function<void()> &fn) { fn(); }

void TestDataClass::t(std::function<void()> &fn) { fn(); }

void fn_as_vars_fn() {
    pypp::print(pypp::PyStr("FN_AS_VARS RESULTS:"));
    std::function<pypp::PyStr(int, int)> fn_var = _test_fn;
    pypp::print(fn_var(1, 2));
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
    std::function<pypp::PyStr(int, int)> f = [](auto x, auto y) {
        return pypp::PyStr(std::format("Lambda {}", pypp::PyTup(x, y)));
    };
    pypp::print(f(3, 4));
    _test_fn6([](auto x, auto y) {
        return pypp::PyStr(std::format("Lambda {}", pypp::PyTup(x, y)));
    });
    std::function<pypp::PyStr()> g = []() {
        return pypp::PyStr("Lambda without args");
    };
    pypp::print(g());
}
