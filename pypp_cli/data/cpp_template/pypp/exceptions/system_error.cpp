#include "system_error.h"
#include <py_str.h>

PyppOSError::PyppOSError(const PyStr &msg, std::error_code ec)
    : std::system_error(ec, "PyppOsError: " + msg.str()) {}

PyppOSError::PyppOSError(const std::string &msg, std::error_code ec)
    : std::system_error(ec, "PyppOsError: " + msg) {}

PyppSystemError::PyppSystemError(const PyStr &msg, std::error_code ec)
    : std::system_error(ec, "PyppSystemError: " + msg.str()) {}

PyppSystemError::PyppSystemError(const std::string &msg, std::error_code ec)
    : std::system_error(ec, "PyppSystemError: " + msg) {}
