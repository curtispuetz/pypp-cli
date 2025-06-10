#include "py_list.h"
#include "py_str.h"
#include "src/dicts/first.h"
#include "src/first.h"
#include "src/fourth.h"
#include "src/if_elif_else/if_elif_else.h"
#include "src/lists/as_arg.h"
#include "src/lists/lists.h"
#include "src/numbers/first.h"
#include "src/second.h"
#include "src/strings/first.h"
#include "src/third.h"
#include "src/tuples/first.h"

int main() {
    return_something(1, 9).print();
    return_friend().print();
    using_inline_string().print();
    string_as_argument(PyStr("hello")).print();
    if_elif_else_fn(6, 6).print();
    number_ops();
    list_fn();
    string_ops();
    PyList<int> my_list = PyList({1, 2, 3, 4});
    list_as_arg(my_list);
    list_as_mutable_arg(my_list);
    my_list.print();
    PyList<PyStr> str_list = PyList({PyStr("ab"), PyStr("cd")});
    str_list.print();
    tuples_fn();
    dict_fn();
    return 0;
}