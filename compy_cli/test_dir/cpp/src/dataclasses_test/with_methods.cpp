#include "dataclasses_test/with_methods.h"
#include "py_str.h"
#include "pypp_util/print.h"

int DataClassWithMethods::add(int x) { return field1 + x; }

int DataClassWithMethods::subtract(int x) { return field1 - x; }

struct _PrivateDataClassWithMethods {
    int field1;
    _PrivateDataClassWithMethods(int a_field1) : field1(std::move(a_field1)) {}
    int add(int x) { return field1 + x; }
};

void dataclass_with_methods_fn() {
    print(PyStr("DATACLASS WITH METHODS RESULTS:"));
    DataClassWithMethods k = DataClassWithMethods(2);
    print(k.add(1), k.subtract(1));
    _PrivateDataClassWithMethods p = _PrivateDataClassWithMethods(3);
    print(p.add(2));
}
