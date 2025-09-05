#include "operations.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
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
    PyList<int> t1({1, 2});
    PyList<int> &t2 = t1;
    bool m = t1 == t2;
    print(PyStr(std::format("is: {}", m)));
    bool n = t1 != t2;
    print(PyStr(std::format("is not: {}", n)));
    bool o = PyList({1, 5}).contains(5);
    print(PyStr(std::format("in: {}", o)));
    bool p = PySet({1, 5}).contains(5);
    print(PyStr(std::format("in set: {}", p)));
    PyDict<int, PyStr> test_dict = {{1, PyStr("a")}, {5, PyStr("b")}};
    bool q = test_dict.contains(5);
    print(PyStr(std::format("in dict: {}", q)));
    bool r = PyTup(1, 5).contains(5);
    print(PyStr(std::format("in tuple: {}", r)));
    bool s = PyStr("zzabczz").contains(PyStr("abc"));
    print(PyStr(std::format("in string: {}", s)));
    bool t = !PyList({1, 2}).contains(5);
    print(PyStr(std::format("not in: {}", t)));
    bool u = !PySet({1, 2}).contains(5);
    print(PyStr(std::format("not in set: {}", u)));
    bool v = !test_dict.contains(5);
    print(PyStr(std::format("not in dict: {}", v)));
    bool w = !PyTup(1, 2).contains(5);
    print(PyStr(std::format("not in tuple: {}", w)));
    bool x = !PyStr("zzxyz").contains(PyStr("abc"));
    print(PyStr(std::format("not in string: {}", x)));
    print(PyStr("printing reference:"));
    print(&x);
}
