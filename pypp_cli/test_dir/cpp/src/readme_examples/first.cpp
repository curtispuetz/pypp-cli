#include "readme_examples/first.h"
#include "py_str.h"
#include "pypp_assert.h"

namespace me {
pypp::PyList<int> my_function(pypp::PyList<int> &a, pypp::PyList<int> &b) {
    pypp::PyList<int> ret({1, 2, 3});
    pypp::assert(a.len() == b.len(),
                 pypp::PyStr("List lengths should be equal"));
    for (int i = 0; i < a.len(); i += 1) {
        ret.append(a[i] + b[i]);
    }
    return ret;
}

} // namespace me