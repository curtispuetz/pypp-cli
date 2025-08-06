#include "exceptions\assert_.h"
#include "py_str.h"
#include "pypp_assert.h"
#include "pypp_util/print.h"

void assert_fn() {
    print(PyStr("ASSERT TESTS"));
    assert(1 == 1, PyStr("should not fail"));
    assert(1 == 1, PyStr(""));
}
