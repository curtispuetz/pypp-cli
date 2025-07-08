#include "dataclasses\first.h"
#include "pypp_util/print.h"

struct _PrivateDataClass {
    int field1;
    _PrivateDataClass(int a_field1) : field1(std::move(a_field1)) {}
};

void dataclass_fn() {
    print(PyStr("DATACLASS RESULTS:"));
    FirstDataClass a =
        FirstDataClass(PyStr("the answer to the universe and everything:"), 42);
    print(a.field1, a.field2);
    PyStr b = PyStr("abc");
    DataClassWithReference c = DataClassWithReference(b, 1);
    print(c.field1, c.field2);
    PyStr d = PyStr("xyz");
    FirstDataClass e = FirstDataClass(std::move(d), 2);
    print(e.field1, e.field2);
    FrozenDataClass f = FrozenDataClass(PyStr("a"), 3);
    print(f.field1, f.field2);
    PyStr g = PyStr("abc");
    FrozenDataClassWithReference h = FrozenDataClassWithReference(g, 4);
    print(h.field1, h.field2);
    PyStr i = PyStr("xyz");
    FrozenDataClass j = FrozenDataClass(std::move(i), 5);
    print(j.field1, j.field2);
}
