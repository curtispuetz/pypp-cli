#include "pypp_union\first.h"
#include "py_str.h"
#include "pypp_union.h"
#include "pypp_util/print.h"

void pypp_union_fn() {
    print(PyStr("PYPP UNION RESULTS:"));
    Uni<int, double> a(3.14);
    if (a.isinst<double>()) {
        print(a.ug<double>());
    }
    if (!a.isinst<int>()) {
        print(PyStr("a is not an int"));
    }
    Uni<int, std::monostate> b(std::monostate{});
    if (b.is_none()) {
        print(PyStr("b is None"));
    }
}
