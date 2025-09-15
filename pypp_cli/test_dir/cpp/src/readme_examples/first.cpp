#include "src/readme_examples/first.h"
#include "py_str.h"
#include "pypp_assert.h"

namespace me {
pypp::PyList<int> list_add(pypp::PyList<int> &a, pypp::PyList<int> &b,
                           int mult_factor) {
    pypp::assert(a.len() == b.len(),
                 pypp::PyStr("List lengths should be equal"));
    pypp::PyList<int> ret({});
    for (int i = 0; i < a.len(); i += 1) {
        ret.append(mult_factor * (a[i] + b[i]));
    }
    return ret;
}

} // namespace me