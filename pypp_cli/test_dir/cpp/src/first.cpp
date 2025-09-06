#include "first.h"

pypp::PyStr return_something(int a, int b) {
    pypp::PyStr ret;
    if (a > b) {
        ret = pypp::PyStr("abc");
    } else {
        ret = pypp::PyStr("xyz");
    }
    return ret;
}
