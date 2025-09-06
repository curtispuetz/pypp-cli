#include "loops/zip_.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <utility>

void zip_fn() {
    pypp::print(pypp::PyStr("ZIP RESULTS:"));
    pypp::PyList<int> a({});
    for (const auto &[x, z] :
         pypp::PyZip(pypp::PyList({1, 2}), pypp::PyList({3, 4}))) {
        a.append(std::move(x));
        a.append(std::move(z));
    }
    pypp::print(a);
    pypp::PyDict<double, int> b = {{1.1, 4}, {2.2, 5}};
    for (const auto &[x, z, y, w] :
         pypp::PyZip(pypp::PyList({1, 2}),
                     pypp::PySet({pypp::PyStr("a"), pypp::PyStr("b")}),
                     pypp::PyStr("ab"), b.items())) {
        pypp::print(pypp::PyStr(std::format("{}, {}, {}, {}, {}", x, z, y,
                                            w.get<0>(), w.get<0>())));
    }
}
