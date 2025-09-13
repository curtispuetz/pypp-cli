#pragma once

#include "exceptions/common.h"
#include "py_str.h"

namespace pypp {
inline void assert(bool condition, const PyStr msg) {
    if (!condition) {
        throw AssertionError(msg);
    }
}
} // namespace pypp