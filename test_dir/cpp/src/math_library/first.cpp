#include "math_library\first.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <cmath>
#include <numbers>

void math_library_fn() {
    print(PyStr("MATH LIBRARY RESULTS:"));
    print(std::sqrt(9));
    print(std::hypot(3, 4));
    print(std::floor(3.5));
    print(std::ceil(3.5));
    print(std::numbers::pi);
    print(std::sin(std::numbers::pi / 2));
    print(std::cos(std::numbers::pi / 4));
    print(std::tan(std::numbers::pi / 4));
    double a = (std::numbers::pi / 180.0) * (90);
    print(a);
}