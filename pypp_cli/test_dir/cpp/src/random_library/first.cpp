#include "random_library/first.h"
#include "py_str.h"
#include "pypp_random.h"
#include "pypp_util/print.h"

double _random_as_arg(random::Random &a) { return a.random(); }

class _RandomWrapper {
  public:
    random::Random &_r;
    _RandomWrapper(random::Random &a_r) : _r(a_r) {}
    double mult(random::Random &b) { return _r.random() * b.random(); }
};

void random_fn() {
    print(PyStr("pypp RANDOM RESULTS:"));
    random::Random a = random::Random(42);
    double b = a.random();
    print(b);
    print(_random_as_arg(a));
    _RandomWrapper c = _RandomWrapper(a);
    double d = c.mult(a);
    print(d);
}
