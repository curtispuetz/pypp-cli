#include "ios.h"
#include <py_str.h>

namespace pypp {

IOError::IOError(const PyStr &msg)
    : std::ios_base::failure("IOError: " + msg.str()) {}

IOError::IOError(const std::string &msg)
    : std::ios_base::failure("IOError: " + msg) {}
} // namespace pypp