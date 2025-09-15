#include "src/ranges/first.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_range.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
static void _iter_and_print(pypp::PyRange &arg1) {
    pypp::PyList<int> a1({});
    for (const auto &i : arg1) {
        int y = i;
        a1.append(std::move(y));
    }
    pypp::print(a1);
}

static pypp::PyRange _range_as_return() { return pypp::PyRange(9, 1, -2); }

void ranges_fn() {
    pypp::print(pypp::PyStr("RANGE RESULTS:"));
    pypp::PyRange a = pypp::PyRange(10);
    _iter_and_print(a);
    pypp::PyRange a0 = _range_as_return();
    _iter_and_print(a0);
    for (int i = 10; i < 5; i += 1) {
        pypp::print(i);
    }
    pypp::print(pypp::PyRange(10));
    pypp::print(pypp::PyRange(5, 10));
    pypp::print(pypp::PyRange(10, 5, -1));
    pypp::print(pypp::PyRange(5, 10, 1));
    pypp::PyDict<pypp::PyRange, int> b = {{a, 1}, {pypp::PyRange(1, 4), 2}};
    pypp::print(b);
}

} // namespace me