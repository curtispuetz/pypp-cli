#include "number_types/in_collections.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <cstdint>

void _lists() {
    pypp::PyList<int8_t> a({1, 2, 3, 4});
    pypp::print(a);
    pypp::PyList<int16_t> b({5, 6, 7, 8});
    pypp::print(b);
    pypp::PyList<int32_t> c({9, 10, 11, 12});
    pypp::print(c);
    pypp::PyList<int64_t> d({13, 14, 15, 16});
    pypp::print(d);
    pypp::PyList<uint8_t> e({17, 18, 19, 20});
    pypp::print(e);
    pypp::PyList<uint16_t> f({21, 22, 23, 24});
    pypp::print(f);
    pypp::PyList<uint32_t> g({25, 26, 27, 28});
    pypp::print(g);
    pypp::PyList<uint64_t> h({29, 30, 31, 32});
    pypp::print(h);
    pypp::PyList<float> i({3.14, 2.71, 1.61});
    pypp::print(i);
}

void _sets() {
    pypp::PySet<int8_t> a({1, 2, 3, 4});
    pypp::print(a);
    pypp::PySet<int16_t> b({5, 6, 7, 8});
    pypp::print(b);
    pypp::PySet<int32_t> c({9, 10, 11, 12});
    pypp::print(c);
    pypp::PySet<int64_t> d({13, 14, 15, 16});
    pypp::print(d);
    pypp::PySet<uint8_t> e({17, 18, 19, 20});
    pypp::print(e);
    pypp::PySet<uint16_t> f({21, 22, 23, 24});
    pypp::print(f);
    pypp::PySet<uint32_t> g({25, 26, 27, 28});
    pypp::print(g);
    pypp::PySet<uint64_t> h({29, 30, 31, 32});
    pypp::print(h);
    pypp::PySet<float> i({3.14, 2.71, 1.61});
    pypp::print(i);
}

void _dicts() {
    pypp::PyDict<int8_t, pypp::PyStr> a = {{1, pypp::PyStr("a")},
                                           {2, pypp::PyStr("b")}};
    pypp::print(a);
    pypp::PyDict<int16_t, pypp::PyStr> b = {{3, pypp::PyStr("c")},
                                            {4, pypp::PyStr("d")}};
    pypp::print(b);
    pypp::PyDict<int32_t, pypp::PyStr> c = {{5, pypp::PyStr("e")},
                                            {6, pypp::PyStr("f")}};
    pypp::print(c);
    pypp::PyDict<int64_t, pypp::PyStr> d = {{7, pypp::PyStr("g")},
                                            {8, pypp::PyStr("h")}};
    pypp::print(d);
    pypp::PyDict<uint8_t, pypp::PyStr> e = {{9, pypp::PyStr("i")},
                                            {10, pypp::PyStr("j")}};
    pypp::print(e);
    pypp::PyDict<uint16_t, pypp::PyStr> f = {{11, pypp::PyStr("k")},
                                             {12, pypp::PyStr("l")}};
    pypp::print(f);
    pypp::PyDict<uint32_t, pypp::PyStr> g = {{13, pypp::PyStr("m")},
                                             {14, pypp::PyStr("n")}};
    pypp::print(g);
    pypp::PyDict<uint64_t, pypp::PyStr> h = {{15, pypp::PyStr("o")},
                                             {16, pypp::PyStr("p")}};
    pypp::print(h);
    pypp::PyDict<float, pypp::PyStr> i = {{3.14, pypp::PyStr("q")},
                                          {2.71, pypp::PyStr("r")}};
    pypp::print(i);
    pypp::PyDict<int16_t, float> j = {{1, 3.14}, {2, 2.71}};
    pypp::print(j);
    pypp::PyDict<uint16_t, int32_t> k = {{1, 1}, {2, 2}};
    pypp::print(k);
}

pypp::PyList<uint16_t> _list_factory() {
    pypp::PyList<uint16_t> ret({1, 2, 3, 4});
    return ret;
}

pypp::PySet<uint16_t> _set_factory() {
    pypp::PySet<uint16_t> ret({1, 2, 3, 4});
    return ret;
}

pypp::PyDict<uint16_t, pypp::PyStr> _dict_factory() {
    return {{1, pypp::PyStr("a")}, {2, pypp::PyStr("b")}};
}

void number_types_in_collections_fn() {
    pypp::print(pypp::PyStr("NUMBER TYPES IN COLLECTIONS RESULTS:"));
    _lists();
    _sets();
    _dicts();
    pypp::print(_list_factory());
    pypp::print(_set_factory());
    pypp::print(_dict_factory());
}
