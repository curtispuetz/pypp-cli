#include "strings\first.h"

void string_ops() {
    PyStr s = PyStr("  abd  ");
    s.print();
    to_pystr(s.len()).print();
    s[2].print();
    s[PySlice(2, 4, 1)].print();
    s[PySlice(0, 4, 1)].print();
    s[PySlice(3, -1, 1)].print();
    s[PySlice(2, 5, 2)].print();
    s[PySlice(2, -1, 2)].print();
    s[PySlice(0, -1, 1)].print();
    PyStr s_concat = PyStr("Hello ") + PyStr("World");
    s_concat.print();
    (((PyStr("Hello") + PyStr(" ")) + PyStr("World")) + PyStr("!")).print();
    (PyStr("A") + PyStr("B")).print();
    (PyStr("AB") * 5).print();
    PyStr("ab").upper().print();
    PyStr("AB").lower().print();
    to_pystr(PyStr("abcdefg").find(PyStr("b"))).print();
    to_pystr(PyStr("abcbc").index(PyStr("bc"))).print();
    to_pystr(PyStr("abab").rindex(PyStr("ab"))).print();
    to_pystr(PyStr("ababab").count(PyStr("ab"))).print();
    to_pystr(PyStr("abab").startswith(PyStr("ab"))).print();
    to_pystr(PyStr("abab").endswith(PyStr("ab"))).print();
    PyStr("abcdab").replace(PyStr("ab"), PyStr("xy")).print();
    PyStr("abcdab").replace(PyStr("ab"), PyStr("xy"), 1).print();
    s.strip().print();
    s.lstrip().print();
    s.rstrip().print();
    to_pystr(PyStr("a") == PyStr("a")).print();
    to_pystr(PyStr("a") > PyStr("a")).print();
    to_pystr(PyStr("a") >= PyStr("a")).print();
    to_pystr(PyStr("a") < PyStr("a")).print();
    to_pystr(PyStr("a") <= PyStr("a")).print();
    to_pystr(PyStr("a") != PyStr("a")).print();
}