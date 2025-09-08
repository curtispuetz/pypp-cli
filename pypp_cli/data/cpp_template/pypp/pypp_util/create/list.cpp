#include "pypp_util/create/list.h"

namespace pypp {
PyList<PyStr> list(const PyStr &s) {
    PyList<PyStr> chars;
    for (auto c : s) {
        chars.append(std::move(c));
    }
    return chars;
}
} // namespace pypp