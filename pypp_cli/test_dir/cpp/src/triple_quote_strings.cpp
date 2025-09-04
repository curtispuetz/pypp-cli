#include "triple_quote_strings.h"
#include "py_str.h"
#include "pypp_util/print.h"

void triple_quote_strings_fn() {
    PyStr a = PyStr("This is a triple-quoted string.");
    print(a);
    PyStr b = PyStr("\nline 1\nline 2\nother stuff\n");
    print(b);
}
