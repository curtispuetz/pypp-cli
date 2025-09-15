#include "src/lists/operations.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void list_operations_fn() {
    pypp::print(pypp::PyStr("LIST OPERATIONS RESULTS:"));
    pypp::PyList<int> a({1, 2, 3});
    if (a.contains(1)) {
        pypp::print(pypp::PyStr("1 in a"));
    }
    if (!a.contains(4)) {
        pypp::print(pypp::PyStr("4 not in a"));
    }
    pypp::print(a.len());
    pypp::print(a + pypp::PyList({4, 5}));
    a += pypp::PyList({6, 7});
    pypp::print(a);
    pypp::print(pypp::PyList({1, 2}) * 3);
    a *= 2;
    pypp::print(a);
    pypp::print(a.min());
    pypp::print(a.max());
}

} // namespace me