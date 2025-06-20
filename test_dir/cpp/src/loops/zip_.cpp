#include "loops\zip_.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <any>

void zip_fn() {
    print(PyStr("ZIP RESULTS:"));
    PyList<int> a = PyList<int>({});
    for (const auto &pypp_hardcoded_it_tup :
         PyZip(PyList({1, 2}), PyList({3, 4}))) {
        auto &x = pypp_hardcoded_it_tup.get<0>();
        auto &z = pypp_hardcoded_it_tup.get<1>();
        a.append(x);
        a.append(z);
    }
    print(a);
    PyDict<double, int> b({{1.1, 4}, {2.2, 5}});
    for (const auto &pypp_hardcoded_it_tup :
         PyZip(PyList({1, 2}), PySet({PyStr("a"), PyStr("b")}), PyStr("ab"),
               b.items())) {
        auto &x = pypp_hardcoded_it_tup.get<0>();
        auto &z = pypp_hardcoded_it_tup.get<1>();
        auto &y = pypp_hardcoded_it_tup.get<2>();
        auto &w = pypp_hardcoded_it_tup.get<3>();
        print(PyStr(std::format("{}, {}, {}, {}, {}", x, z, y, w.get<0>(),
                                w.get<0>())));
    }
}