#include "inconsistent_behviour/editing_a_reference.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void editing_a_reference_fn() {
    pypp::print(pypp::PyStr("INCONSISTENT BEHAVIOR RESULTS:"));
    pypp::PyList<int> a({1, 2, 3});
    pypp::PyList<int> b = a;
    b.append(4);
    pypp::print(pypp::PyStr(std::format("inconsistent behavior: {}", a)));
    pypp::PyList<int> c({1, 2, 3});
    pypp::PyList<int> d = update_and_return_new(c);
    d[-1] = 99;
    pypp::print(pypp::PyStr(std::format("inconsistent behavior: {}", c)));
}

pypp::PyList<int> update_and_return_new(pypp::PyList<int> &l1) {
    l1.append(4);
    return l1;
}

} // namespace me