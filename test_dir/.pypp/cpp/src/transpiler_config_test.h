#pragma once

#include "py_str.h"
#include <utility>

namespace me {
void a_function_i_like();
void a_function_i_like_extra();
struct AnnAssignCustomType {
    pypp::PyStr x;
    AnnAssignCustomType(pypp::PyStr a_x) : x(std::move(a_x)) {}
};

struct AnnAssignOtherType {
    pypp::PyStr x;
    AnnAssignOtherType(pypp::PyStr a_x) : x(std::move(a_x)) {}
};

void transpiler_config_test_fn();
} // namespace me