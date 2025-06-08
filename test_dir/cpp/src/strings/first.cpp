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
}