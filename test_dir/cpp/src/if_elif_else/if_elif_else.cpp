#include "if_elif_else\if_elif_else.h"

PyStr if_elif_else_fn(int a, int b) {
    PyStr ret;
    if (a < b) {
        ret = PyStr("less than");
    } else if (a == b) {
        ret = PyStr("equal");
    } else {
        ret = PyStr("greater than");
    }
    return ret;
}
PyStr if_elif_elif_else_fn(int a, int b) {
    PyStr ret;
    if (a < b) {
        ret = PyStr("less than");
    } else if (a == b) {
        ret = PyStr("equal");
    } else if (a > b) {
        ret = PyStr("dunno");
    } else {
        ret = PyStr("greater than");
    }
    return ret;
}