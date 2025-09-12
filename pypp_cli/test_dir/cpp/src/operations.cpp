#include "operations.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/math.h"
#include "pypp_util/print.h"
#include <cmath>

namespace me {
void operations_fn() {
    pypp::print(pypp::PyStr("OPERATIONS RESULTS:"));
    double a = std::pow(2, 3);
    pypp::print(pypp::PyStr(std::format("float power: {}", a)));
    int b = pypp::int_pow(2, 3);
    pypp::print(pypp::PyStr(std::format("int power: {}", b)));
    int c = 10 % 3;
    pypp::print(pypp::PyStr(std::format("mod: {}", c)));
    int d = 1 << 2;
    pypp::print(pypp::PyStr(std::format("left shift: {}", d)));
    int e = 4 >> 1;
    pypp::print(pypp::PyStr(std::format("right shift: {}", e)));
    int f = 1 | 2;
    pypp::print(pypp::PyStr(std::format("bitwise or: {}", f)));
    int g = 1 ^ 2;
    pypp::print(pypp::PyStr(std::format("bitwise xor: {}", g)));
    int h = 1 & 2;
    pypp::print(pypp::PyStr(std::format("bitwise and: {}", h)));
    bool i = !true;
    pypp::print(pypp::PyStr(std::format("not: {}", i)));
    int j = -5;
    pypp::print(pypp::PyStr(std::format("usub: {}", j)));
    int k = +5;
    pypp::print(pypp::PyStr(std::format("uadd: {}", k)));
    int l1 = ~5;
    pypp::print(pypp::PyStr(std::format("invert: {}", l1)));
    pypp::PyList<int> t1({1, 2});
    pypp::PyList<int> &t2 = t1;
    bool m = &t1 == &t2;
    pypp::print(pypp::PyStr(std::format("same objects: {}", m)));
    bool n = &t1 != &t2;
    pypp::print(pypp::PyStr(std::format("different objects: {}", n)));
    bool o = pypp::PyList({1, 5}).contains(5);
    pypp::print(pypp::PyStr(std::format("in: {}", o)));
    bool p = pypp::PySet({1, 5}).contains(5);
    pypp::print(pypp::PyStr(std::format("in set: {}", p)));
    pypp::PyDict<int, pypp::PyStr> test_dict = {{1, pypp::PyStr("a")},
                                                {5, pypp::PyStr("b")}};
    bool q = test_dict.contains(5);
    pypp::print(pypp::PyStr(std::format("in dict: {}", q)));
    bool r = pypp::PyTup(1, 5).contains(5);
    pypp::print(pypp::PyStr(std::format("in tuple: {}", r)));
    bool s = pypp::PyStr("zzabczz").contains(pypp::PyStr("abc"));
    pypp::print(pypp::PyStr(std::format("in string: {}", s)));
    bool t = !pypp::PyList({1, 2}).contains(5);
    pypp::print(pypp::PyStr(std::format("not in: {}", t)));
    bool u = !pypp::PySet({1, 2}).contains(5);
    pypp::print(pypp::PyStr(std::format("not in set: {}", u)));
    bool v = !test_dict.contains(5);
    pypp::print(pypp::PyStr(std::format("not in dict: {}", v)));
    bool w = !pypp::PyTup(1, 2).contains(5);
    pypp::print(pypp::PyStr(std::format("not in tuple: {}", w)));
    bool x = !pypp::PyStr("zzxyz").contains(pypp::PyStr("abc"));
    pypp::print(pypp::PyStr(std::format("not in string: {}", x)));
    pypp::print(pypp::PyStr("printing reference:"));
    pypp::print(&x);
}

} // namespace me