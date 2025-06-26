#include "lists\comprehensions.h"
#include "py_list.h"
#include "py_range.h"
#include "py_str.h"
#include "pypp_util/print.h"

void list_comprehension_fn() {
    PyList<int> squares;
    for (int x = 0; x < 10; x += 1) {
        squares.append(x * x);
    }
    print(PyStr(std::format("Squares: {}", squares)));
}