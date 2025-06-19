#include "strings\f_strings.h"
#include "np_arr.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_range.h"
#include "py_set.h"
#include "py_slice.h"
#include "py_str.h"
#include "pypp_util/print.h"

void f_strings_fn() {
    print(PyStr("F STRING RESULTS:"));
    PyStr a =
        PyStr(std::format("this {} my {}st test f string", PyStr("is"), 1));
    print(a);
    PySet<int> my_set = PySet({1, 2});
    PyDict<int, int> my_dict({{0, 1}});
    PyStr b = PyStr(std::format("list: {}, tuple: {}, set: {}, dict: {}, numpy "
                                "array: {}, slice: {}, range: {}",
                                PyList({1, 2}), PyTup(1, 2), my_set, my_dict,
                                pypp_np::zeros<float>(PyList({2})), PySlice(10),
                                PyRange(1)));
    print(b);
}