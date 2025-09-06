#include "sets/comprehensions.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
void set_comprehension_fn() {
    pypp::print(pypp::PyStr("SET COMPREHENSION RESULTS:"));
    pypp::PySet<int> squares;
    for (int x = 0; x < 4; x += 1) {
        squares.add(x * x);
    }
    pypp::print(pypp::PyStr(std::format("Squares: {}", squares)));
    pypp::PySet<int> a;
    for (int i = 0; i < 4; i += 1) {
        a.add(std::move(i));
    }
    pypp::print(a);
}

} // namespace me