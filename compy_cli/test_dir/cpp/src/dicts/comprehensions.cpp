#include "dicts/comprehensions.h"
#include "compy_util/print.h"
#include "py_dict.h"
#include "py_range.h"
#include "py_str.h"
#include <utility>

void dict_comprehension_fn() {
    print(PyStr("DICT COMPREHENSION RESULTS:"));
    PyDict<int, int> squares;
    for (int x = 0; x < 4; x += 1) {
        squares[std::move(x)] = x * x;
    }
    print(PyStr(std::format("Squares: {}", squares)));
}
