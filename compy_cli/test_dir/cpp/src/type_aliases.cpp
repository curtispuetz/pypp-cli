#include "type_aliases.h"
#include "compy_util/print.h"
#include "py_str.h"
#include "py_tuple.h"

using _PrivateType = PyTup<int, PyList<PyStr>, double>;
void type_aliases_fn() {
    print(PyStr("TYPE ALIASES RESULTS:"));
    Matrix my_matrix =
        PyList({PyList({1, 2, 3}), PyList({4, 5, 6}), PyList({7, 8, 9})});
    print(PyStr(std::format("My matrix: {}", my_matrix)));
    int result = process_matrix(my_matrix);
    print(PyStr(std::format("first elem: {}", result)));
    _PrivateType private_data =
        PyTup(42, PyList({PyStr("example"), PyStr("data")}), 3.14);
    print(PyStr(std::format("Private data: {}", private_data)));
    L a = PyList({1, 2, 3});
    print(a);
}

int process_matrix(Matrix &m) { return m[0][0]; }
