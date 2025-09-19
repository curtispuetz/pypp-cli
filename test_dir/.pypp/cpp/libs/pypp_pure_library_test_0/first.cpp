#include "pypp_pure_library_test_0/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_pure_library_test_0/hello_world.h"
#include "pypp_util/print.h"

namespace pure_test_0 {
void first_fn() {
    pypp::print(pypp::PyStr("Hello from first_fn()"));
    pypp::PyList<int> a({1, 2, 3});
    pypp::print(a);
    pure_test_0::hello_world_fn();
}

} // namespace pure_test_0