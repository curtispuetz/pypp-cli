#include "lists\comprehensions.h"
#include "py_list.h"
#include "py_range.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"

int square(int x) { return x * x; }
void list_comprehension_fn() {
    print(PyStr("LIST COMPREHENSION RESULTS:"));
    PyList<int> squares;
    for (int x = 0; x < 10; x += 1) {
        squares.append(x * x);
    }
    print(PyStr(std::format("Squares: {}", squares)));
    PyList<int> squares_func;
    for (int x = 0; x < 10; x += 1) {
        squares_func.append(square(x));
    }
    print(PyStr(std::format("Squares using function: {}", squares_func)));
    PyList<int> fibonacci;
    for (const auto &[x, y] : PyZip(PyList({0, 1}), PyList({1, 2}))) {
        fibonacci.append(x + y);
    }
    print(PyStr(std::format("Fibonacci: {}", fibonacci)));
}