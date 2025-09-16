#include "src/fourth.h"

namespace me {
pypp::PyStr string_as_argument(pypp::PyStr input_str) {
    if (input_str < pypp::PyStr("abc")) {
        return input_str;
    }
    return pypp::PyStr("abc");
}

} // namespace me