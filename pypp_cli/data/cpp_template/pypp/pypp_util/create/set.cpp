#include "pypp_util/create/set.h"

namespace pypp {
PySet<PyStr> set(const PyStr &s) {
    PySet<PyStr> chars;
    for (auto c : s) {
        chars.add(std::move(c));
    }
    return chars;
}
} // namespace pypp