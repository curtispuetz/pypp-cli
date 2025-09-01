#include "loops/for_.h"
#include "compy_util/print.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include <utility>

void for_loop_fn() {
    print(PyStr("FOR RESULTS:"));
    PyList<int> ret = PyList<int>({});
    for (int i = 2; i < 10; i += 2) {
        ret.append(std::move(i));
    }
    for (int j = 2; j < 4; j += 1) {
        ret.append(std::move(j));
    }
    for (int k = 0; k < 2; k += 1) {
        ret.append(std::move(k));
    }
    print(ret);
    PyList<int> a = PyList<int>({});
    for (const auto &val : ret) {
        int y = val;
        a.append(std::move(y));
    }
    print(a);
    PySet<int> b = PySet({10, 20, 30});
    for (const auto &val : b) {
        int y = val;
        a.append(std::move(y));
    }
    print(a);
    PyDict<int, int> c = {{0, 1}, {1, 2}};
    for (const auto &k : c.keys()) {
        int y = k;
        a.append(std::move(y));
    }
    print(a);
    for (const auto &v : c.values()) {
        int y = v;
        a.append(std::move(y));
    }
    print(a);
    for (const auto &[k, v] : c.items()) {
        int x = k;
        int y = v;
        a.append(std::move(x));
        a.append(std::move(y));
    }
    print(a);
    PyList<PyTup<int, int>> d = PyList({PyTup(1, 2), PyTup(3, 4)});
    for (const auto &[first, second] : d) {
        int x = first;
        int y = second;
        a.append(std::move(x));
        a.append(std::move(y));
    }
    print(a);
    print(d);
    PyDict<int, PyDict<int, PyDict<int, int>>> e = {
        {0, {{0, {{0, 1}, {2, 3}}}}}};
    for (const auto &[k1, v1] : e.items()) {
        for (const auto &[k2, v2] : v1.items()) {
            for (const auto &[k3, v3] : v2.items()) {
                int x = k3;
                int y = v3;
                a.append(std::move(x));
                a.append(std::move(y));
            }
        }
    }
    print(a);
}
