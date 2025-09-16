#include "cstdlib"
#include "exceptions/exception.h"
#include "py_str.h"
#include "pypp_util/main_error_handler.h"
#include <GLFW/glfw3.h>

void glfw_test() {
    if (!glfwInit()) {
        throw pypp::Exception(pypp::PyStr("Failed to initialize GLFW"));
    }
    GLFWwindow *window = glfwCreateWindow(
        640, 480, pypp::PyStr("Hello World").str().c_str(), NULL, NULL);
    if (!window) {
        glfwTerminate();
        throw pypp::Exception(pypp::PyStr("Failed to create GLFW window"));
    }
    glfwMakeContextCurrent(window);
    while (!glfwWindowShouldClose(window)) {
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
}

int main() {
    try {
        glfw_test();
        return 0;
    } catch (...) {
        pypp::handle_fatal_exception();
        return EXIT_FAILURE;
    }
}