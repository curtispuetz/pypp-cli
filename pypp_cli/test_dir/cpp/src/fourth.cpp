#include "fourth.h"

pypp::PyStr string_as_argument(pypp::PyStr input_str) {
    if (input_str < pypp::PyStr("abc")) {
        return input_str;
    }
    return pypp::PyStr("abc");
}
