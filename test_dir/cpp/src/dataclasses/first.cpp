#include "dataclasses\first.h"
#include "pypp_util/print.h"

void dataclass_fn() {
    FirstDataClass a =
        FirstDataClass(PyStr("the answer to the universe and everything"), 42);
    print(PyStr(std::format("field1: {}, field2: {}", a.field1, a.field2)));
}