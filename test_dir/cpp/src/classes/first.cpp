#include "classes\first.h"
#include "pypp_util/print.h"

int ClassA::add(int c) { return a + c; }
class _PrivateClass {
  public:
    int a;
    _PrivateClass(int a_a) : a(std::move(a_a)) {}
};
void classes_fn() {
    print(PyStr("CLASSES RESULTS:"));
    PyStr a = PyStr("hello");
    ClassA b = ClassA(1, a);
    print(b.add(2));
    print(b.b);
    ClassWithPassByValue c = ClassWithPassByValue(1, PyStr("world"));
    print(c.b);
    PyStr d = PyStr("abc");
    ClassWithPassByValue e = ClassWithPassByValue(1, std::move(d));
    print(e.b);
    _PrivateClass f = _PrivateClass(3);
    print(f.a);
}