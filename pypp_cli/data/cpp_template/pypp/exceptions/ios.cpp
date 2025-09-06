#include "ios.h"
#include <py_str.h>

namespace pypp {

PyppIOError::PyppIOError(const PyStr &msg)
    : std::ios_base::failure("PyppIOError: " + msg.str()) {}

PyppIOError::PyppIOError(const std::string &msg)
    : std::ios_base::failure("PyppIOError: " + msg) {}
} // namespace pypp