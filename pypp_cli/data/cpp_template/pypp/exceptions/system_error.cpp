#include "system_error.h"
#include <py_str.h>

namespace pypp {
OSError::OSError(const PyStr &msg, std::error_code ec)
    : std::system_error(ec, "OsError: " + msg.str()) {}

OSError::OSError(const std::string &msg, std::error_code ec)
    : std::system_error(ec, "OsError: " + msg) {}

SystemError::SystemError(const PyStr &msg, std::error_code ec)
    : std::system_error(ec, "SystemError: " + msg.str()) {}

SystemError::SystemError(const std::string &msg, std::error_code ec)
    : std::system_error(ec, "SystemError: " + msg) {}

} // namespace pypp