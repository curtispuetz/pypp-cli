#include "pypp_util/main_error_handler.h"
#include <cstdlib>
#include <exception>
#include <iostream>

void handle_fatal_exception() {
    try {
        throw; // Re-throw current exception
    } catch (const std::exception &e) {
        std::cerr << "\nUnhandled exception: \n" << e.what() << std::endl;
    } catch (...) {
        std::cerr << "Unhandled unknown exception." << std::endl;
    }
}
