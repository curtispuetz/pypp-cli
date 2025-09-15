#include "src/readme_examples/union.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_union.h"
#include "pypp_util/print.h"

namespace me {
void union_example() {
    pypp::Uni<int, double, pypp::PyList<int>> int_float_or_list(3.14);
    if (int_float_or_list.isinst<double>()) {
        double val = int_float_or_list.ug<double>();
        pypp::print(val);
    }
    pypp::Uni<int, std::monostate> b(std::monostate{});
    if (b.is_none()) {
        pypp::print(pypp::PyStr("b is None"));
    }
}

} // namespace me