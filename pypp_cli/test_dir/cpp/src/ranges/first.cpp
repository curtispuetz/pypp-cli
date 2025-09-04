#include "ranges/first.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_range.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

void _iter_and_print(PyRange arg1) {
    PyList<int> a1 = PyList<int>({});
    for (const auto &i : arg1) {
        int y = i;
        a1.append(std::move(y));
    }
    print(a1);
}

PyRange _range_as_return() { return PyRange(9, 1, -2); }

void ranges_fn() {
    print(PyStr("RANGE RESULTS:"));
    PyRange a = PyRange(10);
    _iter_and_print(a);
    _iter_and_print(PyRange(10, 19));
    _iter_and_print(_range_as_return());
    for (int i = 10; i < 5; i += 1) {
        print(i);
    }
    print(PyRange(10));
    print(PyRange(5, 10));
    print(PyRange(10, 5, -1));
    print(PyRange(5, 10, 1));
    PyDict<PyRange, int> b = {{a, 1}, {PyRange(1, 4), 2}};
    print(b);
}
