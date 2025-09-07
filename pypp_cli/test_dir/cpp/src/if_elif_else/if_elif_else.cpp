#include "if_elif_else/if_elif_else.h"

namespace me {
pypp::PyStr if_elif_else_fn(int a, int b) {
    pypp::PyStr ret;
    if (a < b) {
        ret = pypp::PyStr("less than");
    } else if (a == b) {
        ret = pypp::PyStr("equal");
    } else {
        ret = pypp::PyStr("greater than");
    }
    return ret;
}

pypp::PyStr if_elif_elif_else_fn(int a, int b) {
    pypp::PyStr ret;
    if (a < b) {
        ret = pypp::PyStr("less than");
    } else if (a == b) {
        ret = pypp::PyStr("equal");
    } else if (a > b) {
        ret = pypp::PyStr("dunno");
    } else {
        ret = pypp::PyStr("greater than");
    }
    return ret;
}

} // namespace me