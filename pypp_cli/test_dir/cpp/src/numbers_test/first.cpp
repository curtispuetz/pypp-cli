#include "numbers_test/first.h"
#include "py_str.h"
#include "pypp_util/floor_div.h"
#include "pypp_util/print.h"

namespace me {
void number_ops() {
    pypp::print(pypp::PyStr("NUMBER RESULTS:"));
    int a = 1 + 2;
    pypp::print(a);
    pypp::print(2 + 2);
    pypp::print(2 * 2);
    pypp::print(4 / 2);
    double b = (4 + 10) - ((5 * 5.0) / 2);
    pypp::print(b);
    int c = ((5 + 10) * (2 + 2)) * ((5 + 4) + 10);
    pypp::print(c);
    int d = ((10 * 40) + ((4 + (2 * 4)) + 4)) * (10 * 2);
    int e = (4 + (2 * 4)) + 4;
    pypp::print(d);
    pypp::print(e);
    int f = pypp::py_floor_div(10, 5);
    pypp::print(f);
    pypp::print(pypp::py_floor_div(-7, 2));
    int g = pypp::py_floor_div((pypp::py_floor_div(-14, 2)), ((-2 + 4) * 1));
    pypp::print(g);
    double h = -4.1;
    h += 2;
    pypp::print(h);
    h -= 2;
    pypp::print(h);
    h *= 5;
    pypp::print(h);
    h /= 5;
    pypp::print(h);
}

} // namespace me