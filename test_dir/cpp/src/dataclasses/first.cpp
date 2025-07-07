#include "dataclasses\first.h"
#include "pypp_util/print.h"

void dataclass_fn() {
    FirstDataClass a =
        FirstDataClass(PyStr("the answer to the universe and everything"), 42);
    print(PyStr(std::format("field1: {}, field2: {}", a.field1, a.field2)));
    PyStr b = PyStr("abc");
    DataClassWithReference c = DataClassWithReference(b, 1);
    print(PyStr(std::format("field1: {}, field2: {}", c.field1, c.field2)));
    PyStr d = PyStr("xyz");
    FirstDataClass e = FirstDataClass(std::move(d), 2);
    print(PyStr(std::format("field1: {}, field2: {}", e.field1, e.field2)));
}