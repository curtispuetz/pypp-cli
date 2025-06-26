#include "strings\f_strings.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_range.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "slice/creators.h"

void f_strings_fn() {
    print(PyStr("F STRING RESULTS:"));
    PyStr a =
        PyStr(std::format("this {} my {}st test f string", PyStr("is"), 1));
    print(a);
    PySet<int> my_set = PySet({1, 2});
    PyDict<int, int> my_dict({{0, 1}});
    PyStr b = PyStr(std::format(
        "list: {}, tuple: {}, set: {}, dict: {}, slice: {}, range: {}",
        PyList({1, 2}), PyTup(1, 2), my_set, my_dict, py_slice(10),
        PyRange(1)));
    print(b);
}