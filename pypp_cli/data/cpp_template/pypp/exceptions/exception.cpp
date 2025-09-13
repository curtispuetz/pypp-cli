#include "exceptions/exception.h"
#include "py_str.h"

namespace pypp {
Exception::Exception(const PyStr &msg) : msg_("Exception: " + msg.str()) {}

const char *Exception::what() const noexcept { return msg_.c_str(); }
} // namespace pypp
