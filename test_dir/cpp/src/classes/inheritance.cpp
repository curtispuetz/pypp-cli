#include "classes\inheritance.h"
#include "py_str.h"
#include "pypp_util/print.h"

int BaseClass::add(int val) { return a + val; }
int BaseClass::add2(int val) { return a + val; }
int ChildClass::add(int val) { return add2(val); }
int ChildClass::multiply(int val) { return (a * b) * val; }
void class_inheritance_fn() {
    print(PyStr("CLASS INHERITANCE RESULTS:"));
    ChildClass a = ChildClass(2, 2);
    print(a.add(3));
    print(a.multiply(3));
}