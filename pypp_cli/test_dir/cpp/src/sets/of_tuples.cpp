#include "sets/of_tuples.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

void set_of_tuples_fn() {
    pypp::print(pypp::PyStr("SET OF TUPLES RESULTS:"));
    pypp::PySet<pypp::PyTup<int, int>> a(
        {pypp::PyTup(1, 2), pypp::PyTup(3, 4)});
    pypp::print(a);
}
