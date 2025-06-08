#include "py_str.h"
#include "src/first.h"
#include "src/fourth.h"
#include "src/if_elif_else/if_elif_else.h"
#include "src/lists/lists.h"
#include "src/numbers/first.h"
#include "src/second.h"
#include "src/strings/first.h"
#include "src/third.h"

int main() {
    return_something(1, 9).print();
    return_friend().print();
    using_inline_string().print();
    string_as_argument(PyStr("hello")).print();
    if_elif_else_fn(6, 6).print();
    string_ops();
    list_fn();
    number_ops();
    return 0;
}