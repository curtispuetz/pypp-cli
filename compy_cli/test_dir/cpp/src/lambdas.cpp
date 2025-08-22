#include "lambdas.h"
#include "compy_util/floor_div.h"
#include "compy_util/print.h"
#include "py_str.h"
#include <functional>

void lambdas_fn() {
    print(PyStr("LAMBDA RESULTS:"));
    std::function<int(int)> a = [](auto x) { return py_floor_div(x, 2); };
    print(a(5));
}
