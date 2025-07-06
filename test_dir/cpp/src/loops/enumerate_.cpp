#include "loops\enumerate_.h"
#include "py_dict.h"
#include "py_enumerate.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <any>
#include <utility>

void enumerate_fn() {
    print(PyStr("ENUMERATE RESULTS:"));
    PyList<int> a = PyList<int>({});
    for (const auto &[i, val] : PyEnumerate(PyList({1, 2, 3}))) {
        a.append(i);
        a.append(std::move(val));
    }
    print(a);
    for (const auto &[i, val] : PyEnumerate(PySet({-1, -3}))) {
        a.append(i);
    }
    print(a);
    PyDict<int, int> d({{0, 1}, {1, 2}});
    for (const auto &[i, val] : PyEnumerate(d.keys())) {
        a.append(i);
    }
    print(a);
    for (const auto &[i, val] : PyEnumerate(d.values())) {
        a.append(i);
    }
    print(a);
    for (const auto &[i, val] : PyEnumerate(d.items())) {
        a.append(i);
        int y = val.get<0>();
        a.append(std::move(y));
    }
    print(a);
}