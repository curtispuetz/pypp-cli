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
    pypp::print(pypp::PyStr("pypp UNION RESULTS:"));
    pypp::Uni<int, double> a(3.14);
    if (a.isinst<double>()) {
        pypp::print(a.ug<double>());
    }
    if (!a.isinst<int>()) {
        pypp::print(pypp::PyStr("a is not an int"));
    }
    pypp::Uni<int, std::monostate> b(std::monostate{});
    if (b.is_none()) {
        pypp::print(pypp::PyStr("b is None"));
    }
    pypp::Uni<int, double> c(42);
    ClassWithUnion d = ClassWithUnion(c);
    pypp::print(d.calc());
    pypp::Uni<int, double> e(3.14);
    ClassWithUnionByValue f = ClassWithUnionByValue(std::move(e));
    pypp::print(&f);
}
