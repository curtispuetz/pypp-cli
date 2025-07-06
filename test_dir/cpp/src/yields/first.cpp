#include "yields\first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

Generator<int> yield_123() {
    co_yield 1;
    co_yield 2;
    co_yield 3;
}
Generator<int> yield_over_list() {
    for (const auto &i : PyList({1, 2, 3})) {
        co_yield i;
    }
}
Generator<int> yield_from_example() { CO_YIELD_FROM(yield_over_list()); }
void yield_fn() {
    print(PyStr("YIELD RESULTS:"));
    PyList<int> a = PyList<int>({});
    for (const auto &i : yield_123()) {
        int y = i;
        a.append(std::move(y));
    }
    print(a);
    for (const auto &i : yield_over_list()) {
        int y = i;
        a.append(std::move(y));
    }
    print(a);
    for (const auto &i : yield_from_example()) {
        int y = i;
        a.append(std::move(y));
    }
    print(a);
}