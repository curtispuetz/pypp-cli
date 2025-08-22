#include "pypp_union/first.h"
#include "py_str.h"
#include "pypp_util/print.h"

int ClassWithUnion::calc() {
    if (value.isinst<int>()) {
        return value.ug<int>() * 2;
    }
    return 0;
}

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
    Uni<int, double> c(42);
    ClassWithUnion d = ClassWithUnion(c);
    print(d.calc());
    Uni<int, double> e(3.14);
    ClassWithUnionByValue f = ClassWithUnionByValue(std::move(e));
    print(&f);
}
