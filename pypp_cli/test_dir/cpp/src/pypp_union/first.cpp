#include "pypp_union/first.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
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
    ClassWithUnionByValue g = ClassWithUnionByValue(pypp::Uni<int, double>(7));
    pypp::print(&g);
    auto h = pypp::Uni<int, double>(2.71);
    pypp::print(h);
    pypp::print(a == pypp::Uni<int, double>(3.14));
    pypp::print(a != pypp::Uni<int, double>(3.14));
}

} // namespace me