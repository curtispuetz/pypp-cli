#include "src/dicts/operations.h"
#include "py_dict.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void dict_operations_fn() {
    pypp::print(pypp::PyStr("DICT OPERATIONS RESULTS:"));
    pypp::PyDict<int, pypp::PyStr> a = {{1, pypp::PyStr("one")},
                                        {2, pypp::PyStr("two")},
                                        {3, pypp::PyStr("three")}};
    if (a.contains(1)) {
        pypp::print(pypp::PyStr("1 in a"));
    }
    if (!a.contains(4)) {
        pypp::print(pypp::PyStr("4 not in a"));
    }
    pypp::print(a.len());
    pypp::print(a.min());
    pypp::print(a.max());
    pypp::PyDict<int, pypp::PyStr> b = {{1, pypp::PyStr("one")},
                                        {2, pypp::PyStr("two")},
                                        {3, pypp::PyStr("three")}};
    if (a == b) {
        pypp::print(pypp::PyStr("is equal"));
    }
    pypp::PyDict<int, pypp::PyStr> c = {{1, pypp::PyStr("one")},
                                        {2, pypp::PyStr("two")},
                                        {3, pypp::PyStr("thee")}};
    if (a != c) {
        pypp::print(pypp::PyStr("is not equal"));
    }
}

} // namespace me