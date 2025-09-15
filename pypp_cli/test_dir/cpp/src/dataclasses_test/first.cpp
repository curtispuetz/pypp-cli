#include "src/dataclasses_test/first.h"
#include "pypp_util/print.h"

namespace me {
struct _PrivateDataClass {
    int field1;
    _PrivateDataClass(int a_field1) : field1(std::move(a_field1)) {}
};

pypp::PyStr WithoutAnyFields::method() { return pypp::PyStr("method called"); }

void dataclass_fn() {
    pypp::print(pypp::PyStr("DATACLASS RESULTS:"));
    FirstDataClass a = FirstDataClass(
        pypp::PyStr("the answer to the universe and everything:"), 42);
    pypp::print(a.field1, a.field2);
    pypp::PyStr b = pypp::PyStr("abc");
    DataClassWithReference c = DataClassWithReference(b, 1);
    pypp::print(c.field1, c.field2);
    pypp::PyStr d = pypp::PyStr("xyz");
    FirstDataClass e = FirstDataClass(std::move(d), 2);
    pypp::print(e.field1, e.field2);
    FrozenDataClass f = FrozenDataClass(pypp::PyStr("a"), 3);
    pypp::print(f.field1, f.field2);
    pypp::PyStr g = pypp::PyStr("abc");
    FrozenDataClassWithReference h = FrozenDataClassWithReference(g, 4);
    pypp::print(h.field1, h.field2);
    pypp::PyStr i = pypp::PyStr("xyz");
    FrozenDataClass j = FrozenDataClass(std::move(i), 5);
    pypp::print(j.field1, j.field2);
    WithoutAnyFields k = WithoutAnyFields();
    pypp::print(k.method());
}

} // namespace me