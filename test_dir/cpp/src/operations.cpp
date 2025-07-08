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
    int d = 1 << 2;
    print(PyStr(std::format("left shift: {}", d)));
    int e = 4 >> 1;
    print(PyStr(std::format("right shift: {}", e)));
    int f = 1 | 2;
    print(PyStr(std::format("bitwise or: {}", f)));
    int g = 1 ^ 2;
    print(PyStr(std::format("bitwise xor: {}", g)));
    int h = 1 & 2;
    print(PyStr(std::format("bitwise and: {}", h)));
    bool i = !true;
    print(PyStr(std::format("not: {}", i)));
    int j = -5;
    print(PyStr(std::format("usub: {}", j)));
    int k = +5;
    print(PyStr(std::format("uadd: {}", k)));
    int l1 = ~5;
    print(PyStr(std::format("invert: {}", l1)));
}
