#include "strings\escape_characters.h"

void string_esc_chars_fn() {
    PyStr a = PyStr("\n");
    PyStr b = PyStr("abcd\n");
    PyStr c = PyStr("\t");
    PyStr d = PyStr("abcd\t");
    PyStr e = PyStr("\r");
    PyStr f = PyStr("abcd\r");
    PyStr g = PyStr("\b");
    PyStr h = PyStr("abcd\b");
    PyStr i = PyStr("\f");
    PyStr j = PyStr("abcd\f");
    PyStr k = PyStr("\\");
    PyStr l1 = PyStr("abcd\\");
    (((((((((((a + b) + c) + d) + e) + f) + g) + h) + i) + j) + k) + l1)
        .print();
    PyStr m = PyStr("abcd\\\\");
    m.print();
}