#include "operations.h"
#include "py_str.h"
#include "pypp_util/math.h"
#include "pypp_util/print.h"
#include <cmath>

void operations_fn() {
    print(PyStr("OPERATIONS RESULTS:"));
    double a = std::pow(2, 3);
    print(PyStr(std::format("float power: {}", a)));
    int b = int_pow(2, 3);
    print(PyStr(std::format("int power: {}", b)));
    int c = 10 % 3;
    print(PyStr(std::format("mod: {}", c)));
}
