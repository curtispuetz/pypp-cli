#include "src/exceptions/assert_.h"
#include "py_str.h"
#include "pypp_assert.h"
#include "pypp_util/print.h"

namespace me {
void assert_fn() {
    pypp::print(pypp::PyStr("ASSERT TESTS"));
    pypp::assert(1 == 1, pypp::PyStr("should not fail"));
    pypp::assert(1 == 1, pypp::PyStr(""));
}

} // namespace me