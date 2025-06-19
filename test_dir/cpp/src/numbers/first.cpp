#include "numbers\first.h"

void number_ops() {
    print(PyStr("NUMBER RESULTS:"));
    int a = 1 + 2;
    print(to_pystr(a));
    print(to_pystr(2 + 2));
    print(to_pystr(2 * 2));
    print(to_pystr(4 / 2));
    double b = (4 + 10) - ((5 * 5.0) / 2);
    print(to_pystr(b));
    int c = ((5 + 10) * (2 + 2)) * ((5 + 4) + 10);
    print(to_pystr(c));
    int d = ((10 * 40) + ((4 + (2 * 4)) + 4)) * (10 * 2);
    int e = (4 + (2 * 4)) + 4;
    print(to_pystr(d));
    print(to_pystr(e));
    int f = py_floor_div(10, 5);
    print(to_pystr(f));
    print(to_pystr(py_floor_div(-7, 2)));
    int g = py_floor_div((py_floor_div(-14, 2)), ((-2 + 4) * 1));
    print(to_pystr(g));
    g += 2;
    print(to_pystr(g));
    g -= 2;
    print(to_pystr(g));
    g *= 5;
    print(to_pystr(g));
    g /= 5;
    print(to_pystr(g));
    std::cout << 1 << std::endl;
}