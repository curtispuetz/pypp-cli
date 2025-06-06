#include "first.h"

std::string return_something(int a, int b) {
    std::string ret;
    if (a > b) {
        ret = "abc";
    } else {
        ret = "xyz";
    }
    return ret;
}