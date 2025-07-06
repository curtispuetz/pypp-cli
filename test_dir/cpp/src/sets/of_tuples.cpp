#include "sets\of_tuples.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"
#include <utility>

void set_of_tuples_fn() {
    print(PyStr("SET OF TUPLES RESULTS:"));
    PySet<PyTup<int, int>> a = PySet({PyTup(1, 2), PyTup(3, 4)});
    print(a);
    PyTup<int, int> mov_tup = PyTup(1, 2);
    PySet<PyTup<int, int>> b = PySet({std::move(mov_tup), PyTup(5, 6)});
    print(b);
    print(mov_tup);
}