#include "interfaces\first.h"
#include "pypp_util/print.h"

class _PrivateInterface {
  public:
    virtual void a() = 0;
    virtual ~_PrivateInterface() {}
};

void Impl1::speak(int a) { print(PyStr("number given:"), a); }

PyStr Impl1::talk() { return PyStr("hello"); }

void Impl2::speak(int a) { print(PyStr("number given times 2:"), 2 * a); }

PyStr Impl2::talk() { return PyStr("hello there"); }

void _fn_that_accepts_interface(InterfaceClass &i) {
    i.speak(2);
    print(i.talk());
}

void interfaces_fn() {
    print(PyStr("INTERFACES RESULTS:"));
    Impl1 a = Impl1(-1);
    a.speak(42);
    print(a.talk());
    Impl2 b = Impl2(-1);
    b.speak(43);
    _fn_that_accepts_interface(a);
    _fn_that_accepts_interface(b);
}
