#include "type_aliases.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

namespace me {
using _PrivateType = pypp::PyTup<int, pypp::PyList<pypp::PyStr>, double>;
void type_aliases_fn() {
    pypp::print(pypp::PyStr("TYPE ALIASES RESULTS:"));
    Matrix my_matrix({pypp::PyList({1, 2, 3}), pypp::PyList({4, 5, 6}),
                      pypp::PyList({7, 8, 9})});
    pypp::print(pypp::PyStr(std::format("My matrix: {}", my_matrix)));
    int result = process_matrix(my_matrix);
    pypp::print(pypp::PyStr(std::format("first elem: {}", result)));
    _PrivateType private_data = pypp::PyTup(
        42, pypp::PyList({pypp::PyStr("example"), pypp::PyStr("data")}), 3.14);
    pypp::print(pypp::PyStr(std::format("Private data: {}", private_data)));
    using L = pypp::PyList<int>;
    L a({1, 2, 3});
    pypp::print(a);
}

int process_matrix(Matrix &m) { return m[0][0]; }

} // namespace me