#include "loops/zip_.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
void zip_fn() {
    pypp::print(pypp::PyStr("ZIP RESULTS:"));
    pypp::PyList<int> a({});
    for (const auto &[x, z] :
         pypp::PyZip(pypp::PyList({1, 2}), pypp::PyList({3, 4}))) {
        int xx = x;
        int zz = z;
        a.append(std::move(xx));
        a.append(std::move(zz));
    }
    pypp::print(a);
    for (const auto &[x, z, y] :
         pypp::PyZip(pypp::PyList({1, 2}),
                     pypp::PySet({pypp::PyStr("a"), pypp::PyStr("b")}),
                     pypp::PyStr("ab"))) {
        pypp::print(pypp::PyStr(std::format("{}, {}, {}", x, z, y)));
    }
}

} // namespace me