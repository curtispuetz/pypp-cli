#include "loops\zip_.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <any>
#include <utility>

void zip_fn() {
    print(PyStr("ZIP RESULTS:"));
    PyList<int> a = PyList<int>({});
    for (const auto &[x, z] : PyZip(PyList({1, 2}), PyList({3, 4}))) {
        a.append(std::move(x));
        a.append(std::move(z));
    }
    print(a);
    PyDict<double, int> b({{1.1, 4}, {2.2, 5}});
    for (const auto &[x, z, y, w] :
         PyZip(PyList({1, 2}), PySet({PyStr("a"), PyStr("b")}), PyStr("ab"),
               b.items())) {
        print(PyStr(std::format("{}, {}, {}, {}, {}", x, z, y, w.get<0>(),
                                w.get<0>())));
    }
}
