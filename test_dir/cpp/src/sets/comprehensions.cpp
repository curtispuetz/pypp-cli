#include "sets\comprehensions.h"
#include "py_range.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"

void set_comprehension_fn() {
    print(PyStr("SET COMPREHENSION RESULTS:"));
    PySet<int> squares;
    for (int x = 0; x < 4; x += 1) {
        squares.add(x * x);
    }
    print(PyStr(std::format("Squares: {}", squares)));
}