#include "loops\enumerate_.h"
#include "py_dict.h"
#include "py_enumerate.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <any>

void enumerate_fn() {
    print(PyStr("ENUMERATE RESULTS:"));
    PyList<int> a = PyList<int>({});
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(PyList({1, 2, 3}))) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
        a.append(val);
    }
    print(a);
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(PySet({-1, -3}))) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
    }
    print(a);
    PyDict<int, int> d({{0, 1}, {1, 2}});
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(d.keys())) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
    }
    print(a);
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(d.values())) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
    }
    print(a);
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(d.items())) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
        a.append(val.get<0>());
    }
    print(a);
}