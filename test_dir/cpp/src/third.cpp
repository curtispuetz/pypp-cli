#include "third.h"

PyStr using_inline_string() {
    if (PyStr("a") > PyStr("b")) {
        return PyStr("10");
    }
    return PyStr("5");
}
