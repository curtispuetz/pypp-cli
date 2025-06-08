#include "fourth.h"

PyStr string_as_argument(const PyStr &input) {
    if (input < PyStr("abc")) {
        return input;
    }
    return PyStr("abc");
}