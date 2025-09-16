#include "src/loops/reversed_.h"
#include "py_list.h"
#include "py_reversed.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
void reversed_fn() {
    pypp::print(pypp::PyStr("REVERSED RESULTS:"));
    pypp::PyList<int> a({});
    for (const auto &x : pypp::PyReversed(pypp::PyList({1, 2, 3}))) {
        int y = x;
        a.append(std::move(y));
    }
    pypp::print(a);
    pypp::PyList<pypp::PyStr> b({});
    for (const auto &x : pypp::PyReversed(pypp::PyStr("abcd"))) {
        pypp::PyStr y = x;
        b.append(std::move(y));
    }
    pypp::print(b);
    for (const auto &[x, z] :
         pypp::PyZip(pypp::PyReversed(pypp::PyList({1, 2, 3})),
                     pypp::PyReversed(pypp::PyStr("abc")))) {
        pypp::print(pypp::PyStr(std::format("{}, {}", x, z)));
    }
}

} // namespace me