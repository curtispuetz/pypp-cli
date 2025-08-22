#include "exceptions/assert_.h"
#include "compy_assert.h"
#include "compy_util/print.h"
#include "py_str.h"

void assert_fn() {
    print(PyStr("ASSERT TESTS"));
    assert(1 == 1, PyStr("should not fail"));
    assert(1 == 1, PyStr(""));
}
