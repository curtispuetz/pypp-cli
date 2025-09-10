#include "pass_by_value.h"
#include "pypp_util/print.h"

namespace me {
MyType my_type_factory(pypp::PyList<int> a) {
    return MyType(pypp::PyStr("first arg"), std::move(a));
}

void pass_by_value_test_fn() {
    pypp::print(pypp::PyStr("PASS BY VALUE RESULTS:"));
    MyType b = my_type_factory(pypp::PyList({1, 2, 3}));
    pypp::print(b.field2);
    pypp::PyList<int> c({4, 5, 6});
    MyType d = my_type_factory(std::move(c));
    pypp::print(d.field2);
    pypp::PyList<int> e({7, 8, 9});
    MyType f = my_type_factory(e);
    e.append(10);
    pypp::print(pypp::PyStr(
        std::format("{} (should be [7, 8, 9] with C++)", f.field2)));
    pypp::PyList<int> g({11, 12, 13});
    MyType i = my_type_factory(g.copy());
    g.append(-1);
    pypp::print(i.field2);
}

} // namespace me