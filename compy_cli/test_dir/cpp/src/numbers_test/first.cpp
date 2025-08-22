#include "numbers_test/first.h"
#include "compy_util/floor_div.h"
#include "compy_util/print.h"
#include "py_str.h"

void number_ops() {
    print(PyStr("NUMBER RESULTS:"));
    int a = 1 + 2;
    print(a);
    print(2 + 2);
    print(2 * 2);
    print(4 / 2);
    double b = (4 + 10) - ((5 * 5.0) / 2);
    print(b);
    int c = ((5 + 10) * (2 + 2)) * ((5 + 4) + 10);
    print(c);
    int d = ((10 * 40) + ((4 + (2 * 4)) + 4)) * (10 * 2);
    int e = (4 + (2 * 4)) + 4;
    print(d);
    print(e);
    int f = py_floor_div(10, 5);
    print(f);
    print(py_floor_div(-7, 2));
    int g = py_floor_div((py_floor_div(-14, 2)), ((-2 + 4) * 1));
    print(g);
    double h = -4.1;
    h += 2;
    print(h);
    h -= 2;
    print(h);
    h *= 5;
    print(h);
    h /= 5;
    print(h);
}
