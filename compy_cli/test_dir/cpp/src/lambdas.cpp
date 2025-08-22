#include "lambdas.h"
#include "py_str.h"
#include "pypp_util/floor_div.h"
#include "pypp_util/print.h"
#include <functional>

void lambdas_fn() {
    print(PyStr("LAMBDA RESULTS:"));
    std::function<int(int)> a = [](auto x) { return py_floor_div(x, 2); };
    print(a(5));
}
