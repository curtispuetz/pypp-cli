#include "cstdlib"
#include "exceptions/exception.h"
#include "exceptions/stdexcept.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_bridge_lib_opengl/custom.h"
#include "pypp_util/main_error_handler.h"
#include <GLFW/glfw3.h>
#include <glad/gl.h>

PyStr vertex_shader_src =
    PyStr("\n#version 330 core\nlayout(location = 0) in vec3 "
          "position;\nlayout(location = 1) in vec3 color;\n\nout vec3 "
          "vertexColor;\n\nvoid main()\n{\n    gl_Position = vec4(position, "
          "1.0);\n    vertexColor = color;\n}\n");
PyStr fragment_shader_src = PyStr(
    "\n#version 330 core\nin vec3 vertexColor;\nout vec4 FragColor;\n\nvoid "
    "main()\n{\n    FragColor = vec4(vertexColor, 1.0);\n}\n");
GLuint compile_shader(PyStr &source, GLenum shader_type) {
    GLuint shader = glCreateShader(shader_type);
    gl_shader_source(shader, source);
    glCompileShader(shader);
    if (!gl_get_shader_iv(shader, GL_COMPILE_STATUS)) {
        throw PyppRuntimeError(PyStr("Shader compilation failed: ") +
                               gl_get_shader_info_log(shader));
    }
    return shader;
}

GLuint create_shader_program() {
    GLuint vertex_shader = compile_shader(vertex_shader_src, GL_VERTEX_SHADER);
    GLuint fragment_shader =
        compile_shader(fragment_shader_src, GL_FRAGMENT_SHADER);
    GLuint program = glCreateProgram();
    glAttachShader(program, vertex_shader);
    glAttachShader(program, fragment_shader);
    glLinkProgram(program);
    if (!gl_get_program_iv(program, GL_LINK_STATUS)) {
        throw PyppRuntimeError(PyStr("Program linking failed: ") +
                               gl_get_program_info_log(program));
    }
    glDeleteShader(vertex_shader);
    glDeleteShader(fragment_shader);
    return program;
}

void opengl_test() {
    if (!glfwInit()) {
        throw PyppException(PyStr("Failed to initialize GLFW"));
    }
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    GLFWwindow *window = glfwCreateWindow(
        800, 600, PyStr("PyOpenGL Triangle").str().c_str(), NULL, NULL);
    if (!window) {
        glfwTerminate();
        throw PyppException(PyStr("Failed to create GLFW window"));
    }
    glfwMakeContextCurrent(window);
    if (!gladLoadGL(glfwGetProcAddress)) {
        throw PyppException(PyStr("Failed to initialize GLAD"));
    }
    PyList<float> vertices({-0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.5, -0.5, 0.0, 0.0,
                            1.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 1.0});
    GLuint vao = gl_gen_vertex_array();
    GLuint vbo = gl_gen_buffer();
    glBindVertexArray(vao);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, vertices.len() * sizeof(GLfloat),
                 vertices.data_ref().data(), GL_STATIC_DRAW);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat),
                          (void *)(0));
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat),
                          (void *)(3 * sizeof(GLfloat)));
    glEnableVertexAttribArray(1);
    GLuint shader_program = create_shader_program();
    while (!glfwWindowShouldClose(window)) {
        glfwPollEvents();
        glClearColor(0.2, 0.3, 0.3, 1.0);
        glClear(GL_COLOR_BUFFER_BIT);
        glUseProgram(shader_program);
        glBindVertexArray(vao);
        glDrawArrays(GL_TRIANGLES, 0, 3);
        glfwSwapBuffers(window);
    }
    gl_delete_vertex_array(vao);
    gl_delete_buffer(vbo);
    glfwTerminate();
}

int main() {
    try {
        opengl_test();
        return 0;
    } catch (...) {
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}