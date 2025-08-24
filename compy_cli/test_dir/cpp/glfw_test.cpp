#include "compy_util/main_error_handler.h"
#include "cstdlib"
#include "exceptions/exception.h"
#include "py_str.h"
#include <GLFW/glfw3.h>

void glfw_test() {
    if (!glfwInit()) {
        throw CompyException(PyStr("Failed to initialize GLFW").str());
    }
    GLFWwindow *window = glfwCreateWindow(
        640, 480, PyStr("Hello World").str().c_str(), NULL, NULL);
    if (!window) {
        glfwTerminate();
        throw CompyException(PyStr("Failed to create GLFW window").str());
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
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}