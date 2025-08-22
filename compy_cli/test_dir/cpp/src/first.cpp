#include "first.h"

PyStr return_something(int a, int b) {
    PyStr ret;
    if (a > b) {
        ret = PyStr("abc");
    } else {
        ret = PyStr("xyz");
    }
    return ret;
}
