#include "src/dataclasses_test/nested_dependencies.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
struct _ClassA {
    int a;
    _ClassA(int a_a) : a(std::move(a_a)) {}
};

struct _ClassB {
    int b;
    _ClassA &class_a;
    _ClassB(int a_b, _ClassA &a_class_a)
        : b(std::move(a_b)), class_a(a_class_a) {}
};

struct _ClassC {
    int c;
    _ClassB &class_b;
    _ClassC(int a_c, _ClassB &a_class_b)
        : c(std::move(a_c)), class_b(a_class_b) {}
    int access() { return class_b.class_a.a; }
};

void dataclass_nested_dependencies_fn() {
    pypp::print(pypp::PyStr("DATACLASS NESTED DEPENDENCIES RESULTS:"));
    _ClassA class_a = _ClassA(1);
    _ClassB class_b = _ClassB(2, class_a);
    _ClassC class_c = _ClassC(3, class_b);
    pypp::print(class_c.access());
}

} // namespace me