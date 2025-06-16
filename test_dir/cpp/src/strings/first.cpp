#include "strings\first.h"

void string_ops() {
    PyStr s = PyStr("  abd  ");
    s.print();
    to_pystr(s.len()).print();
    s[2].print();
    s[PySlice(2, 4, 1)].print();
    s[PySlice(0, 4, 1)].print();
    s[PySlice(3, std::nullopt, 1)].print();
    s[PySlice(2, 5, 2)].print();
    s[PySlice(2, std::nullopt, 2)].print();
    s[PySlice(0, std::nullopt, 1)].print();
    PyStr("invalid slice: ").print();
    s[PySlice(-6, -13421423, 1345)].print();
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
    s.print();
    s += PyStr("n");
    s += PyStr("");
    s.print();
    s *= 5;
    s.print();
    s *= -5;
    s.print();
    PyList<PyStr> l1 = PyStr("0,1,2").split(PyStr(","));
    l1.print();
    PyList<PyStr> l2 = PyStr("0 1 2").split();
    l2.print();
    PyStr(" ").join(PyList({PyStr("1"), PyStr("2"), PyStr("3")})).print();
    PyStr s_joined = PyStr(", ").join(
        PyList({PyStr("a"), PyStr("b"), PyStr("c"), PyStr("d")}));
    s_joined.print();
    PyStr a = PyStr("");
    a.print();
}