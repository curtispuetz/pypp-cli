#include "lists/comprehensions.h"
#include "py_list.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
int square(int x) { return x * x; }

void list_comprehension_fn() {
    pypp::print(pypp::PyStr("LIST COMPREHENSION RESULTS:"));
    pypp::PyList<int> squares;
    for (int x = 0; x < 10; x += 1) {
        squares.append(x * x);
    }
    pypp::print(pypp::PyStr(std::format("Squares: {}", squares)));
    pypp::PyList<int> squares_func;
    for (int x = 0; x < 10; x += 1) {
        squares_func.append(square(x));
    }
    pypp::print(
        pypp::PyStr(std::format("Squares using function: {}", squares_func)));
    pypp::PyList<int> fibonacci;
    for (const auto &[x, y] :
         pypp::PyZip(pypp::PyList({0, 1}), pypp::PyList({1, 2}))) {
        fibonacci.append(x + y);
    }
    pypp::print(pypp::PyStr(std::format("Fibonacci: {}", fibonacci)));
    pypp::PyList<int> a;
    for (int i = 0; i < 10; i += 1) {
        a.append(std::move(i));
    }
    pypp::print(a);
}

} // namespace me