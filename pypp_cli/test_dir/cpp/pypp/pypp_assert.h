#pragma once

#include "exceptions/stdexcept.h"
#include "py_str.h"

namespace pypp {
inline void assert(bool condition, const PyStr msg) {
    if (!condition) {
        throw PyppAssertionError(msg);
    }
}
} // namespace pypp