#include "triple_quote_strings.h"
#include "py_str.h"
#include "pypp_util/print.h"

void triple_quote_strings_fn() {
    pypp::print(pypp::PyStr("TRIPLE QUOTE STRINGS RESULTS:"));
    pypp::PyStr a = pypp::PyStr("This is a triple-quoted string.");
    pypp::print(a);
    pypp::PyStr b = pypp::PyStr("\nline 1\nline 2\nother stuff\n");
    pypp::print(b);
}
