#include "src/transpiler_config_test.h"
#include "pypp_util/print.h"
#include <string>
#include <vector>

namespace me {
void a_function_i_like() { pypp::print(pypp::PyStr("I like functions!")); }

void a_function_i_like_extra() {
    pypp::print(pypp::PyStr("I like functions!"));
}

struct __PseudoPyppName_ConfigClassA {
    int a = 10;
};
inline __PseudoPyppName_ConfigClassA _ConfigClassA;

struct __PseudoPyppName_ConfigClassB {
    int b = 20;
};
inline __PseudoPyppName_ConfigClassB _ConfigClassB;

void transpiler_config_test_fn() {
    pypp::print(pypp::PyStr("TRANSPILER CONFIG TEST:"));
    pypp::PyStr crazy_name_extra = pypp::PyStr("crazy");
    pypp::print(crazy_name_extra);
    a_function_i_like_extra();
    AnnAssignOtherType a = AnnAssignOtherType(pypp::PyStr("hello"));
    pypp::print(a.x);
    pypp::print(_ConfigClassB.b);
}

} // namespace me