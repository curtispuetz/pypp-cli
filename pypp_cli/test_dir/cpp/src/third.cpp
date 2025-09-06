#include "third.h"

pypp::PyStr using_inline_string() {
    if (pypp::PyStr("a") > pypp::PyStr("b")) {
        return pypp::PyStr("10");
    }
    return pypp::PyStr("5");
}
