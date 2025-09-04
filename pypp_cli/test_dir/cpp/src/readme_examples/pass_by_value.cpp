#include "readme_examples/pass_by_value.h"
#include "py_str.h"
#include "pypp_assert.h"

PyList<int> my_function(PyList<int> a, PyList<int> b) {
    PyList<int> ret = PyList({1, 2, 3});
    assert(a.len() == b.len(), PyStr("List lengths should be equal"));
    for (int i = 0; i < a.len(); i += 1) {
        ret.append(a[i] + b[i]);
    }
    return ret;
}
