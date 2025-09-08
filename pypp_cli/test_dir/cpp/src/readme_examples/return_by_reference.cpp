#include "readme_examples/return_by_reference.h"

namespace me {
pypp::PyList<int> &return_by_reference_fn(pypp::PyList<int> &a,
                                          pypp::PyList<int> &b) {
    return a;
}

} // namespace me