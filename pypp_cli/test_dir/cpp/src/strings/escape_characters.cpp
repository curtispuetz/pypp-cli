#include "strings/escape_characters.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void string_esc_chars_fn() {
    pypp::print(pypp::PyStr("STRING ESC CHARS RESULTS:"));
    pypp::PyStr a = pypp::PyStr("\n");
    pypp::PyStr b = pypp::PyStr("abcd\n");
    pypp::PyStr c = pypp::PyStr("\t");
    pypp::PyStr d = pypp::PyStr("abcd\t");
    pypp::PyStr e = pypp::PyStr("\r");
    pypp::PyStr f = pypp::PyStr("abcd\r");
    pypp::PyStr g = pypp::PyStr("\b");
    pypp::PyStr h = pypp::PyStr("abcd\b");
    pypp::PyStr i = pypp::PyStr("\f");
    pypp::PyStr j = pypp::PyStr("abcd\f");
    pypp::PyStr k = pypp::PyStr("\\");
    pypp::PyStr l1 = pypp::PyStr("abcd\\");
    pypp::print(((((((((((a + b) + c) + d) + e) + f) + g) + h) + i) + j) + k) +
                l1);
    pypp::PyStr m = pypp::PyStr("abcd\\\\");
    pypp::print(m);
}

} // namespace me