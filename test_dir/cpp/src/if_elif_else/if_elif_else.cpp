#include "if_elif_else\if_elif_else.h"

std::string if_elif_else_fn(int a, int b) {
    std::string ret;
    if (a < b) {
        ret = "less than";
    } else if (a == b) {
        ret = "equal";
    } else {
        ret = "greater than";
    }
    return ret;
}
std::string if_elif_elif_else_fn(int a, int b) {
    std::string ret;
    if (a < b) {
        ret = "less than";
    } else if (a == b) {
        ret = "equal";
    } else if (a > b) {
        ret = "dunno";
    } else {
        ret = "greater than";
    }
    return ret;
}