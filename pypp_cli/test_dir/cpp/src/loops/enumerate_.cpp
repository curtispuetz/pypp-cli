#include "loops/enumerate_.h"
#include "py_dict.h"
#include "py_enumerate.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
void enumerate_fn() {
    pypp::print(pypp::PyStr("ENUMERATE RESULTS:"));
    pypp::PyList<int> a({});
    for (const auto &[i, val] : pypp::PyEnumerate(pypp::PyList({1, 2, 3}))) {
        a.append(i);
        int v = val;
        a.append(std::move(v));
    }
    pypp::print(a);
    for (const auto &[i, val] : pypp::PyEnumerate(pypp::PySet({-1, -3}))) {
        a.append(i);
    }
    pypp::print(a);
    pypp::PyDict<int, int> d = {{0, 1}, {1, 2}};
    for (const auto &[i, val] : pypp::PyEnumerate(d.keys())) {
        a.append(i);
    }
    pypp::print(a);
    for (const auto &[i, val] : pypp::PyEnumerate(d.values())) {
        a.append(i);
    }
    pypp::print(a);
    for (const auto &[i, val] : pypp::PyEnumerate(d.items())) {
        a.append(i);
        int y = val.get<0>();
        a.append(std::move(y));
    }
    pypp::print(a);
    pypp::PyList<int> b({10, 20, 30});
    for (const auto &[i, val] : pypp::PyEnumerate(b)) {
        a.append(i);
        int v = val;
        a.append(std::move(v));
    }
    pypp::print(b);
    pypp::print(a);
}

} // namespace me