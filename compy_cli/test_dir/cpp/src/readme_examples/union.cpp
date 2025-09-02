#include "readme_examples/union.h"
#include "compy_union.h"
#include "compy_util/print.h"
#include "py_list.h"
#include "py_str.h"

void union_example() {
    Uni<int, double, PyList<int>> int_float_or_list(3.14);
    if (int_float_or_list.isinst<double>()) {
        double val = int_float_or_list.ug<double>();
        print(val);
    }
    Uni<int, std::monostate> b(std::monostate{});
    if (b.is_none()) {
        print(PyStr("b is None"));
    }
}
