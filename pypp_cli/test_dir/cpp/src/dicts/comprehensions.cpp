#include "dicts/comprehensions.h"
#include "py_dict.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
void dict_comprehension_fn() {
    pypp::print(pypp::PyStr("DICT COMPREHENSION RESULTS:"));
    pypp::PyDict<int, int> squares;
    for (int x = 0; x < 4; x += 1) {
        squares[std::move(x)] = x * x;
    }
    pypp::print(pypp::PyStr(std::format("Squares: {}", squares)));
}

} // namespace me