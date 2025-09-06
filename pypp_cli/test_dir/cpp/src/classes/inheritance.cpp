#include "classes/inheritance.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
int BaseClass::add(int val) { return a + val; }

int BaseClass::add2(int val) { return a + val; }

int BaseClass2::mult2(int val) { return (2 * z) * val; }

int ChildClass::add(int val) { return add2(val); }

int ChildClass::multiply(int val) { return (a * b) * val; }

int ChildClass2::add(int val) { return add2(val); }

int ChildMultiple::add(int val) { return (a + z) + val; }

void class_inheritance_fn() {
    pypp::print(pypp::PyStr("CLASS INHERITANCE RESULTS:"));
    ChildClass a = ChildClass(2, 2);
    pypp::print(a.add(3));
    pypp::print(a.multiply(3));
    ChildClass2 b = ChildClass2(3, 3, 3);
    pypp::print(b.add(4));
    ChildMultiple c = ChildMultiple(4, 4, 4);
    pypp::print(c.add(5));
    pypp::print(c.mult2(5));
}

} // namespace me