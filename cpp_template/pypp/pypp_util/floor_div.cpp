#include "pypp_util/floor_div.h"

int py_floor_div(int a, int b) {
    int div = a / b;
    int rem = a % b;
    if ((rem != 0) && ((a < 0) != (b < 0))) {
        div -= 1;
    }
    return div;
}
