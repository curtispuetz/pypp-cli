#include "excpetions\assert_.h"
#include "exceptions/stdexcept.h"
#include "pypp_util/print.h"

void assert_fn() {
    print(PyStr("ASSERT TESTS"));
    if (!(1 == 1)) {
        throw PyppAssertionError(PyStr("should not fail").str());
    }
    if (!(1 == 1)) {
        throw PyppAssertionError(PyStr("").str());
    }
}