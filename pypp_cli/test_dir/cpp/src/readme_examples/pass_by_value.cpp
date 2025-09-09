#include "readme_examples/pass_by_value.h"

namespace me {
pypp::PyList<int> pass_by_value_fn(pypp::PyList<int> a, pypp::PyList<int> _b) {
    return a;
}

} // namespace me