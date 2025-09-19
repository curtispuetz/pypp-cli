#include "src/yields/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
pypp::Generator<int> yield_123() {
    co_yield 1;
    co_yield 2;
    co_yield 3;
}

pypp::Generator<int> yield_over_list() {
    for (const auto &i : pypp::PyList({1, 2, 3})) {
        co_yield i;
    }
}

pypp::Generator<int> yield_from_example() {
    PYPP_CO_YIELD_FROM(yield_over_list());
}

void yield_fn() {
    pypp::print(pypp::PyStr("YIELD RESULTS:"));
    pypp::PyList<int> a({});
    for (const auto &i : yield_123()) {
        int y = i;
        a.append(std::move(y));
    }
    pypp::print(a);
    for (const auto &i : yield_over_list()) {
        int y = i;
        a.append(std::move(y));
    }
    pypp::print(a);
    for (const auto &i : yield_from_example()) {
        int y = i;
        a.append(std::move(y));
    }
    pypp::print(a);
}

} // namespace me