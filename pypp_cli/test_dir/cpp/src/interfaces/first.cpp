#include "interfaces/first.h"
#include "pypp_util/print.h"

class _PrivateInterface {
  public:
    virtual void a() = 0;
    virtual ~_PrivateInterface() {}
};

void Impl1::speak(int a) { pypp::print(pypp::PyStr("number given:"), a); }

pypp::PyStr Impl1::talk() { return pypp::PyStr("hello"); }

void Impl2::speak(int a) {
    pypp::print(pypp::PyStr("number given times 2:"), 2 * a);
}

pypp::PyStr Impl2::talk() { return pypp::PyStr("hello there"); }

void _fn_that_accepts_interface(InterfaceClass &i) {
    i.speak(2);
    pypp::print(i.talk());
}

void interfaces_fn() {
    pypp::print(pypp::PyStr("INTERFACES RESULTS:"));
    Impl1 a = Impl1();
    a.speak(42);
    pypp::print(a.talk());
    Impl2 b = Impl2();
    b.speak(43);
    _fn_that_accepts_interface(a);
    _fn_that_accepts_interface(b);
}
