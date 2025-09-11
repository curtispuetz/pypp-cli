#include "using_pass.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void fn_that_uses_pass() {}

void ClassWithMethodThatUsesPass::method() {}

void fn_with_if_that_uses_pass(int x) {
    if (x > 0) {
    } else {
        pypp::print(pypp::PyStr("x is not greater than 0"));
    }
}

void fn_with_loop_that_uses_pass() {
    for (int i = 0; i < 10; i += 1) {
    }
}

void fn_with_try_except_finally_that_uses_pass() {
    try {
        throw pypp::PyppValueError(pypp::PyStr("An error occurred"));
    } catch (const pypp::PyppValueError &) {
    }
}

void pass_fn() {
    pypp::print(pypp::PyStr("PASS RESULTS:"));
    fn_that_uses_pass();
    auto obj2 = ClassWithMethodThatUsesPass(pypp::PyList({1, 2, 3}));
    obj2.method();
    fn_with_if_that_uses_pass(5);
    fn_with_loop_that_uses_pass();
    fn_with_try_except_finally_that_uses_pass();
}

} // namespace me