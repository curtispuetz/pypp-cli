#include "src/lambdas.h"
#include "py_str.h"
#include "pypp_util/floor_div.h"
#include "pypp_util/print.h"
#include <functional>

namespace me {
void lambdas_fn() {
    pypp::print(pypp::PyStr("LAMBDA RESULTS:"));
    std::function<int(int)> a = [](auto x) { return pypp::py_floor_div(x, 2); };
    pypp::print(a(5));
}

} // namespace me