#include "empty_return.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void _void_fn() {
    for (int i = 0; i < 3; i += 1) {
        if (i == 1) {
            pypp::print(pypp::PyStr("finished"));
            return;
        }
    }
}

void empty_return_fn() {
    pypp::print(pypp::PyStr("EMPTY RETURN RESULTS:"));
    _void_fn();
}

} // namespace me