#include "pypp_util/main_error_handler.h"
#include "exceptions/exception.h"
#include <cstdlib>
#include <iostream>

namespace pypp {

void handle_fatal_exception() {
    try {
        throw; // Re-throw current exception
    } catch (const Exception &e) {
        std::cerr << "\nUnhandled exception: \n" << e.what() << std::endl;
    } catch (...) {
        std::cerr << "Unhandled unknown exception." << std::endl;
    }
}

} // namespace pypp
