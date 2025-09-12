#include "inconsistent_behviour/reassigning_a_ref.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void modifying_a_ref(pypp::PyList<int> &l) {
    l = pypp::PyList({-1, 3});
    pypp::print(l);
}

void reassigning_a_ref_fn() {
    pypp::print(pypp::PyStr("REASSIGNING A REF RESULTS:"));
    pypp::PyList<int> a({1, 2, 3});
    pypp::PyList<int> &b = a;
    b.append(4);
    pypp::print(a);
    pypp::print(b);
    b = pypp::PyList({10, 20, 30});
    pypp::print(
        pypp::PyStr(std::format("{} (should be [10, 20, 30] in C++)", a)));
    pypp::print(b);
    pypp::PyList<int> c({1, 2, 3});
    modifying_a_ref(c);
    pypp::print(pypp::PyStr(std::format("{} (should be [-1, 3] in C++)", c)));
}

} // namespace me