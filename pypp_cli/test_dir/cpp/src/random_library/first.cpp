#include "random_library/first.h"
#include "exceptions/common.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_random.h"
#include "pypp_util/print.h"
#include <string>

namespace me {
static double _random_as_arg(pypp::random::Random &a) { return a.random(); }

struct _RandomWrapper {
    pypp::random::Random &_r;
    _RandomWrapper(pypp::random::Random &a__r) : _r(a__r) {}
    double mult(pypp::random::Random &b) { return _r.random() * b.random(); }
};

void random_fn() {
    pypp::print(pypp::PyStr("pypp RANDOM RESULTS:"));
    pypp::random::Random a = pypp::random::Random(42);
    a.seed(123);
    double b = a.random();
    pypp::print(b);
    pypp::print(_random_as_arg(a));
    _RandomWrapper c = _RandomWrapper(a);
    double d = c.mult(a);
    pypp::print(d);
    int e = a.randint(1, 10);
    pypp::print(e);
    pypp::PyList<int> f({1, 2, 3});
    a.shuffle(f);
    pypp::print(f);
    int g = a.choice(f);
    pypp::print(g);
    try {
        pypp::PyList<int> empty_list({});
        a.choice(empty_list);
    } catch (const pypp::IndexError &pypp_pseudo_name_ex) {
        std::string ex = pypp_pseudo_name_ex.msg_;
        pypp::print(pypp::PyStr(
            std::format("Caught random.Random.choice exception: {}", ex)));
    }
    pypp::print(pypp::PyStr("Expected: [0.052, 1, [1, 3, 2], 3] for Python:"));
    pypp::print(pypp::PyStr("Excepted: [0.713, 8, [2, 1, 3], 3] for C++:"));
    pypp::print(pypp::PyStr(std::format("[{}, {}, {}, {}]", b, e, f, g)));
}

} // namespace me