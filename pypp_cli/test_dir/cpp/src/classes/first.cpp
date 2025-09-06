#include "classes/first.h"
#include "pypp_util/print.h"

namespace me {
int ClassA::add(int c) { return a + c; }

class _PrivateClass {
  public:
    int a;
    _PrivateClass(int a_a) : a(std::move(a_a)) {}
};

void classes_fn() {
    pypp::print(pypp::PyStr("CLASSES RESULTS:"));
    pypp::PyStr a = pypp::PyStr("hello");
    ClassA b = ClassA(1, a);
    pypp::print(b.add(2));
    pypp::print(b.b);
    ClassWithPassByValue c = ClassWithPassByValue(1, pypp::PyStr("world"));
    pypp::print(c.b);
    pypp::PyStr d = pypp::PyStr("abc");
    ClassWithPassByValue e = ClassWithPassByValue(1, std::move(d));
    pypp::print(e.b);
    _PrivateClass f = _PrivateClass(3);
    pypp::print(f.a);
}

} // namespace me