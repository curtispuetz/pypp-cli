#include "src/printing/first.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

namespace me {
void printing_fn() {
    pypp::print(pypp::PyStr("PRINTING RESULTS:"));
    pypp::print(1);
    pypp::print(1.2);
    pypp::print(true);
    pypp::print(pypp::PyList({1, 2, 3}));
    pypp::print(pypp::PySet({1, 2, 3}));
    pypp::PyDict<int, int> a = {{0, 1}, {1, 2}};
    pypp::print(a);
    pypp::print(pypp::PyList({pypp::PyList({pypp::PyList({-1})})}));
    pypp::print(pypp::PyTup(1, 2));
    pypp::print(1, 2, 3, 4);
    pypp::print(pypp::PyStr("multiple arguments:"), pypp::PyList({1, 2}), a,
                pypp::PySet({1, 2}), pypp::PyTup(5, 6), 3.14, a.keys(),
                a.values(), a.items());
    pypp::print(pypp::PyList({true, false}));
}

} // namespace me