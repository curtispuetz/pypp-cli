#include "fourth.h"

std::string string_as_argument(const std::string &input) {
    if (input < "abc") {
        return input;
    }
    return "abc";
}