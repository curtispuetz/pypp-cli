#include "fourth.h"

PyStr string_as_argument(PyStr input_str) {
    if (input_str < PyStr("abc")) {
        return input_str;
    }
    return PyStr("abc");
}
