#include "random_library/first.h"
#include "py_str.h"
#include "pypp_random.h"
#include "pypp_util/print.h"

double _random_as_arg(pypp::random::Random &a) { return a.random(); }

class _RandomWrapper {
  public:
    pypp::random::Random &_r;
    _RandomWrapper(pypp::random::Random &a_r) : _r(a_r) {}
    double mult(pypp::random::Random &b) { return _r.random() * b.random(); }
};

void random_fn() {
    pypp::print(pypp::PyStr("pypp RANDOM RESULTS:"));
    pypp::random::Random a = pypp::random::Random(42);
    double b = a.random();
    pypp::print(b);
    pypp::print(_random_as_arg(a));
    _RandomWrapper c = _RandomWrapper(a);
    double d = c.mult(a);
    pypp::print(d);
}
