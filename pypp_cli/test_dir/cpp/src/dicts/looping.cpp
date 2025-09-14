#include "dicts/looping.h"
#include "py_dict.h"
#include "py_enumerate.h"
#include "py_list.h"
#include "py_str.h"
#include "py_zip.h"
#include "pypp_util/print.h"

namespace me {
void dict_looping_fn() {
    pypp::print(pypp::PyStr("DICT LOOPING RESULTS:"));
    pypp::PyDict<int, int> d = {{0, 1}, {1, 2}, {2, 3}};
    for (const auto &[i, k] : pypp::PyEnumerate(d.keys())) {
        pypp::print(pypp::PyStr(std::format("{}: {} -> {}", i, k, d[k])));
    }
    for (const auto &[i, k, v] :
         pypp::PyZip(pypp::PyList({1, 2, 3}), d.keys(), d.values())) {
        pypp::print(pypp::PyStr(std::format("{}: {} -> {}", i, k, v)));
    }
}

} // namespace me