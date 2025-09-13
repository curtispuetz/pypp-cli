#include "exceptions/exception.h"
#include "py_str.h"

namespace pypp {
Exception::Exception(const PyStr &msg) : msg_("Exception: " + msg.str()) {}

} // namespace pypp
