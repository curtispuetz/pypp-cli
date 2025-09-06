#pragma once

#include "slice/py_slice.h"
#include <optional>

namespace pypp {

inline PySlice py_slice(std::optional<int> stop) { return PySlice(0, stop, 1); }

inline PySlice py_slice(std::optional<int> start, std::optional<int> stop,
                        int step = 1) {
    return PySlice(start, stop, step);
}
} // namespace pypp