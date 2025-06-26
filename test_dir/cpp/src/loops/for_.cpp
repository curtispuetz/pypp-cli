#include "loops\for_.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_range.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"

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
    for (const auto &[k, v] : c.items()) {
        a.append(k);
        a.append(v);
    }
    print(a);
    PyList<PyTup<int, int>> d = PyList({PyTup(1, 2), PyTup(3, 4)});
    for (const auto &[first, second] : d) {
        a.append(first);
        a.append(second);
    }
    print(a);
    print(d);
    PyDict<int, PyDict<int, PyDict<int, int>>> e(
        {{0, {{0, {{0, 1}, {2, 3}}}}}});
    for (const auto &[k1, v1] : e.items()) {
        for (const auto &[k2, v2] : v1.items()) {
            for (const auto &[k3, v3] : v2.items()) {
                a.append(k3);
                a.append(v3);
            }
        }
    }
    print(a);
}