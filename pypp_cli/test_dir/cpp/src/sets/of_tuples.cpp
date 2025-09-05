#include "sets/of_tuples.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

void set_of_tuples_fn() {
    print(PyStr("SET OF TUPLES RESULTS:"));
    PySet<PyTup<int, int>> a({PyTup(1, 2), PyTup(3, 4)});
    print(a);
}
