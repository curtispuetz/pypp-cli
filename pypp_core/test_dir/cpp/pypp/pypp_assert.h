#pragma once

#include "exceptions/stdexcept.h"
#include "py_str.h"

inline void assert(bool condition, const PyStr msg) {
    if (!condition) {
        throw PyppAssertionError(msg.str());
    }
}