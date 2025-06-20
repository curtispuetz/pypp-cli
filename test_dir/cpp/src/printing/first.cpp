#include "printing\first.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "pypp_util/print.h"

void printing_fn() {
    print(1);
    print(1.2);
    print(true);
    print(PyList({1, 2, 3}));
    print(PySet({1, 2, 3}));
    PyDict<int, int> a({{0, 1}, {1, 2}});
    print(a);
    print(PyList({PyList({PyList({-1})})}));
    print(PyTup(1, 2));
}