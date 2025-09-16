#include "src/sets/operations.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void set_operations_fn() {
    pypp::print(pypp::PyStr("SET OPERATIONS RESULTS:"));
    pypp::PySet<int> a({1, 2, 3});
    if (a.contains(1)) {
        pypp::print(pypp::PyStr("1 in a"));
    }
    if (!a.contains(4)) {
        pypp::print(pypp::PyStr("4 not in a"));
    }
    pypp::print(a.len());
    pypp::print(a.min());
    pypp::print(a.max());
}

} // namespace me