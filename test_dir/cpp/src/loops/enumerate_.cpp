#include "loops\enumerate_.h"
#include "py_dict.h"
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
        a.append(val);
    }
    print(a);
    PyDict<int, int> d({{0, 1}, {1, 2}});
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(d.keys())) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
        a.append(val);
    }
    print(a);
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(d.values())) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
        a.append(val);
    }
    print(a);
    for (const auto &pypp_hardcoded_it_tup : PyEnumerate(d.items())) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
        a.append(val.get<0>());
        a.append(val.get<1>());
    }
    print(a);
    PyEnumerate e = PyEnumerate(PyList({1, 2}));
    for (const auto &pypp_hardcoded_it_tup : e) {
        auto &j = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(j);
        a.append(val);
    }
    print(a);
    _enumerate_as_arg(PyEnumerate(PyList({1, 2})));
}
void _enumerate_as_arg(PyEnumerate<PyList<int>> en) {
    PyList<int> a = PyList<int>({});
    for (const auto &pypp_hardcoded_it_tup : en) {
        auto &i = pypp_hardcoded_it_tup.get<0>();
        auto &val = pypp_hardcoded_it_tup.get<1>();
        a.append(i);
        a.append(val);
    }
    print(a);
}