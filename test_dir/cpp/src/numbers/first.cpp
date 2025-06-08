#include "numbers\first.h"

void number_ops() {
    int a = 1 + 2;
    to_pystr(a).print();
    to_pystr(2 + 2).print();
    to_pystr(2 * 2).print();
    to_pystr(4 / 2).print();
    double b = (4 + 10) - ((5 * 5.0) / 2);
    to_pystr(b).print();
    int c = ((5 + 10) * (2 + 2)) * ((5 + 4) + 10);
    to_pystr(c).print();
    int d = ((10 * 40) + ((4 + (2 * 4)) + 4)) * (10 * 2);
    int e = (4 + (2 * 4)) + 4;
    to_pystr(d).print();
    to_pystr(e).print();
}