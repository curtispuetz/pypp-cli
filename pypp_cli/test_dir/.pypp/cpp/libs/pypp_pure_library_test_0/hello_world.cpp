#include "pypp_pure_library_test_0/hello_world.h"

namespace me {
pypp::PyStr hello_world_fn() { return pypp::PyStr("Hello, World!"); }

} // namespace me