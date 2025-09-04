#include "math_library/first.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <cmath>
#include <numbers>

void math_library_fn() {
    print(PyStr("MATH LIBRARY RESULTS:"));
    double sqrt_result = std::sqrt(9);
    double hypot_result = std::hypot(3, 4);
    int floor_result = std::floor(3.5);
    int ceil_result = std::ceil(3.5);
    double pi_value = std::numbers::pi;
    double sin_result = std::sin(std::numbers::pi / 2);
    double cos_result = std::cos(std::numbers::pi / 4);
    double tan_result = std::tan(std::numbers::pi / 4);
    double radians_result = (std::numbers::pi / 180.0) * (90);
    print(sqrt_result);
    print(hypot_result);
    print(floor_result);
    print(ceil_result);
    print(pi_value);
    print(sin_result);
    print(cos_result);
    print(tan_result);
    print(radians_result);
}
