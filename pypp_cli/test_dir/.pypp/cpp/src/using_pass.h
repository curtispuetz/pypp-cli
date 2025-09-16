#pragma once

#include "py_list.h"
#include <utility>

namespace me {
void fn_that_uses_pass();
struct ClassWithMethodThatUsesPass {
    pypp::PyList<int> my_list;
    ClassWithMethodThatUsesPass(pypp::PyList<int> a_my_list)
        : my_list(std::move(a_my_list)) {}
    void method();
};

void fn_with_if_that_uses_pass(int x);
void fn_with_loop_that_uses_pass();
void fn_with_try_except_finally_that_uses_pass();
void pass_fn();
} // namespace me