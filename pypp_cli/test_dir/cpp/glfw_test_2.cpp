#include "cstdlib"
#include "exceptions/exception.h"
#include "py_str.h"
#include "pypp_util/main_error_handler.h"
#include "pypp_util/print.h"
#include <GLFW/glfw3.h>

void key_callback(GLFWwindow *_window, int key, int _scancode, int action,
                  int _mods) {
    if (action == GLFW_PRESS) {
        print(PyStr(std::format("Key {} pressed", key)));
    } else if (action == GLFW_RELEASE) {
        print(PyStr(std::format("Key {} released", key)));
    }
}

void mouse_button_callback(GLFWwindow *_window, int button, int action,
                           int _mods) {
    if (action == GLFW_PRESS) {
        print(PyStr(std::format("Mouse button {} pressed", button)));
    } else if (action == GLFW_RELEASE) {
        print(PyStr(std::format("Mouse button {} released", button)));
    }
}

void cursor_position_callback(GLFWwindow *_window, double xpos, double ypos) {
    print(PyStr(std::format("Mouse moved to ({}, {})", xpos, ypos)));
}

void glfw_test_2() {
    if (!glfwInit()) {
        throw PyppException(PyStr("Failed to initialize GLFW"));
    }
    GLFWwindow *window = glfwCreateWindow(
        640, 480, PyStr("Hello World").str().c_str(), NULL, NULL);
    if (!window) {
        glfwTerminate();
        throw PyppException(PyStr("Failed to create GLFW window"));
    }
    glfwMakeContextCurrent(window);
    glfwSetKeyCallback(window, key_callback);
    glfwSetMouseButtonCallback(window, mouse_button_callback);
    glfwSetCursorPosCallback(window, cursor_position_callback);
    while (!glfwWindowShouldClose(window)) {
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
}

int main() {
    try {
        glfw_test_2();
        return 0;
    } catch (...) {
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}