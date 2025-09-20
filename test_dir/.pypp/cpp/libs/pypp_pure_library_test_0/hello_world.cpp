#include "pypp_pure_library_test_0/hello_world.h"
#include "pypp_util/print.h"

namespace pure_test_0 {
pypp::PyStr hello_world_fn() {
    pypp::print(pypp::PyStr("did something"));
    return pypp::PyStr("Hello, World!");
}

} // namespace pure_test_0