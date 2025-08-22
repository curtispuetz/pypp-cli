#include "compy_util/main_error_handler.h"
#include "compy_util/print.h"
#include "cstdlib"
#include "py_str.h"

int main() {
    try {
        print(PyStr("hello world!"));
        return 0;
    } catch (...) {
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}