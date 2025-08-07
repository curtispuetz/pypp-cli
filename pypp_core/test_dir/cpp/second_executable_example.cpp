#include "py_str.h"
#include "pypp_util/main_error_handler.h"
#include "pypp_util/print.h"

int main() {
    try {
        print(PyStr("hello world!"));
        return 0;
    } catch (...) {
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}