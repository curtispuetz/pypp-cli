#include "printing\first.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"

void printing_fn() {
    print(PyStr("PRINTING RESULTS:"));
    print(1);
    print(1.2);
    print(true);
    print(PyList({1, 2, 3}));
    print(PySet({1, 2, 3}));
    PyDict<int, int> a({{0, 1}, {1, 2}});
    print(a);
    print(PyList({PyList({PyList({-1})})}));
    print(PyTup(1, 2));
    print(1, 2, 3, 4);
    print(PyStr("multiple arguments:"), PyList({1, 2}), a, PySet({1, 2}),
          PyTup(5, 6), 3.14, a.keys(), a.values(), a.items());
    print(PyList({true, false}));
}