#include "type_aliases.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

using Matrix = PyList<PyList<int>>;
void type_aliases_fn() {
    print(PyStr("TYPE ALIASES RESULTS:"));
    Matrix my_matrix =
        PyList({PyList({1, 2, 3}), PyList({4, 5, 6}), PyList({7, 8, 9})});
    print(PyStr(std::format("My matrix: {}", my_matrix)));
    int result = process_matrix(my_matrix);
    print(PyStr(std::format("first elem: {}", result)));
}
int process_matrix(const Matrix &m) { return m[0][0]; }