#include "loops\for_.h"

void for_loop_fn() {
    print(PyStr("FOR RESULTS:"));
    PyList<int> ret = PyList<int>({});
    for (int i = 2; i < 10; i += 2) {
        ret.append(i);
    }
    for (int j = 2; j < 4; j += 1) {
        ret.append(j);
    }
    for (int k = 0; k < 2; k += 1) {
        ret.append(k);
    }
    print(ret);
    PyList<int> a = PyList<int>({});
    for (const auto &val : ret) {
        a.append(val);
    }
    print(a);
    PySet<int> b = PySet({10, 20, 30});
    for (const auto &val : b) {
        a.append(val);
    }
    print(a);
    PyDict<int, int> c({{0, 1}, {1, 2}});
    for (const auto &k : c.keys()) {
        a.append(k);
    }
    print(a);
    for (const auto &v : c.values()) {
        a.append(v);
    }
    print(a);
    for (const auto &pypp_hardcoded_it_tup : c.items()) {
        auto &k = pypp_hardcoded_it_tup.get<0>();
        auto &v = pypp_hardcoded_it_tup.get<1>();
        a.append(k);
        a.append(v);
    }
    print(a);
    PyList<PyTup<int, int>> d = PyList({PyTup(1, 2), PyTup(3, 4)});
    for (const auto &pypp_hardcoded_it_tup : d) {
        auto &first = pypp_hardcoded_it_tup.get<0>();
        auto &second = pypp_hardcoded_it_tup.get<1>();
        a.append(first);
        a.append(second);
    }
    print(a);
    print(d);
    PyDict<int, PyDict<int, PyDict<int, int>>> e(
        {{0, {{0, {{0, 1}, {2, 3}}}}}});
    for (const auto &pypp_hardcoded_it_tup : e.items()) {
        auto &k1 = pypp_hardcoded_it_tup.get<0>();
        auto &v1 = pypp_hardcoded_it_tup.get<1>();
        for (const auto &pypp_hardcoded_it_tup : v1.items()) {
            auto &k2 = pypp_hardcoded_it_tup.get<0>();
            auto &v2 = pypp_hardcoded_it_tup.get<1>();
            for (const auto &pypp_hardcoded_it_tup : v2.items()) {
                auto &k3 = pypp_hardcoded_it_tup.get<0>();
                auto &v3 = pypp_hardcoded_it_tup.get<1>();
                a.append(k3);
                a.append(v3);
            }
        }
    }
    print(a);
}