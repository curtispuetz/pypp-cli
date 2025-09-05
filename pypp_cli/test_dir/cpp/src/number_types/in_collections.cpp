#include "number_types/in_collections.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <cstdint>

void _lists() {
    PyList<int8_t> a({1, 2, 3, 4});
    print(a);
    PyList<int16_t> b({5, 6, 7, 8});
    print(b);
    PyList<int32_t> c({9, 10, 11, 12});
    print(c);
    PyList<int64_t> d({13, 14, 15, 16});
    print(d);
    PyList<uint8_t> e({17, 18, 19, 20});
    print(e);
    PyList<uint16_t> f({21, 22, 23, 24});
    print(f);
    PyList<uint32_t> g({25, 26, 27, 28});
    print(g);
    PyList<uint64_t> h({29, 30, 31, 32});
    print(h);
    PyList<float> i({3.14, 2.71, 1.61});
    print(i);
}

void _sets() {
    PySet<int8_t> a({1, 2, 3, 4});
    print(a);
    PySet<int16_t> b({5, 6, 7, 8});
    print(b);
    PySet<int32_t> c({9, 10, 11, 12});
    print(c);
    PySet<int64_t> d({13, 14, 15, 16});
    print(d);
    PySet<uint8_t> e({17, 18, 19, 20});
    print(e);
    PySet<uint16_t> f({21, 22, 23, 24});
    print(f);
    PySet<uint32_t> g({25, 26, 27, 28});
    print(g);
    PySet<uint64_t> h({29, 30, 31, 32});
    print(h);
    PySet<float> i({3.14, 2.71, 1.61});
    print(i);
}

void _dicts() {
    PyDict<int8_t, PyStr> a = {{1, PyStr("a")}, {2, PyStr("b")}};
    print(a);
    PyDict<int16_t, PyStr> b = {{3, PyStr("c")}, {4, PyStr("d")}};
    print(b);
    PyDict<int32_t, PyStr> c = {{5, PyStr("e")}, {6, PyStr("f")}};
    print(c);
    PyDict<int64_t, PyStr> d = {{7, PyStr("g")}, {8, PyStr("h")}};
    print(d);
    PyDict<uint8_t, PyStr> e = {{9, PyStr("i")}, {10, PyStr("j")}};
    print(e);
    PyDict<uint16_t, PyStr> f = {{11, PyStr("k")}, {12, PyStr("l")}};
    print(f);
    PyDict<uint32_t, PyStr> g = {{13, PyStr("m")}, {14, PyStr("n")}};
    print(g);
    PyDict<uint64_t, PyStr> h = {{15, PyStr("o")}, {16, PyStr("p")}};
    print(h);
    PyDict<float, PyStr> i = {{3.14, PyStr("q")}, {2.71, PyStr("r")}};
    print(i);
    PyDict<int16_t, float> j = {{1, 3.14}, {2, 2.71}};
    print(j);
    PyDict<uint16_t, int32_t> k = {{1, 1}, {2, 2}};
    print(k);
}

PyList<uint16_t> _list_factory() {
    PyList<uint16_t> ret({1, 2, 3, 4});
    return ret;
}

PySet<uint16_t> _set_factory() {
    PySet<uint16_t> ret({1, 2, 3, 4});
    return ret;
}

PyDict<uint16_t, PyStr> _dict_factory() {
    return {{1, PyStr("a")}, {2, PyStr("b")}};
}

void number_types_in_collections_fn() {
    print(PyStr("NUMBER TYPES IN COLLECTIONS RESULTS:"));
    _lists();
    _sets();
    _dicts();
    print(_list_factory());
    print(_set_factory());
    print(_dict_factory());
}
