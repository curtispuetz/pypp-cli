#include "other_src/first.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void hello_world() { pypp::print(pypp::PyStr("Hello, World!")); }

} // namespace me