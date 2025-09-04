import glfw
from OpenGL.GL import (
    glCreateShader,
    glShaderSource,
    glCompileShader,
    glGetShaderiv,
    GL_COMPILE_STATUS,
    glGetShaderInfoLog,
    glCreateProgram,
    glAttachShader,
    glLinkProgram,
    glGetProgramiv,
    GL_LINK_STATUS,
    glGetProgramInfoLog,
    glDeleteShader,
    glGenVertexArrays,
    glGenBuffers,
    glBindVertexArray,
    glBindBuffer,
    GL_ARRAY_BUFFER,
    glBufferData,
    GL_STATIC_DRAW,
    glVertexAttribPointer,
    glEnableVertexAttribArray,
    GL_FLOAT,
    GL_FALSE,
    glClearColor,
    glClear,
    GL_COLOR_BUFFER_BIT,
    glUseProgram,
    glDrawArrays,
    GL_TRIANGLES,
    GL_VERTEX_SHADER,
    GL_FRAGMENT_SHADER,
    glDeleteVertexArrays,
    glDeleteBuffers,
    sizeof,
    GLfloat,
    GLuint,
    GLenum,
)
import numpy as np
import ctypes

# TODO: change this to remove the ".d_types" part
from pypp_bridge_lib_glfw.d_types import GLFWwindowPtr
from pypp_python import to_c_string, NULL, float32

# Vertex shader source
VERTEX_SHADER: str = """
#version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;

out vec3 vertexColor;

void main()
{
    gl_Position = vec4(position, 1.0);
    vertexColor = color;
}
"""

# Fragment shader source
FRAGMENT_SHADER: str = """
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vertexColor, 1.0);
}
"""


def compile_shader(source: str, shader_type: GLenum) -> int:
    shader: int = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise RuntimeError("Shader compilation failed: " + glGetShaderInfoLog(shader))
    return shader


def create_shader_program():
    vertex_shader: int = compile_shader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fragment_shader: int = compile_shader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)

    program: int = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    if not glGetProgramiv(program, GL_LINK_STATUS):
        raise RuntimeError("Program linking failed: " + glGetProgramInfoLog(program))

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program


def np_arr(data: list[float32]):
    return np.array(data, dtype=np.float32)


def glad_load_gl_loader():
    pass


def opengl_test():
    # Initialize GLFW
    if not glfw.init():
        raise Exception("Failed to initialize GLFW")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create window
    window: GLFWwindowPtr = glfw.create_window(
        800, 600, to_c_string("PyOpenGL Triangle"), NULL, NULL
    )
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")

    glfw.make_context_current(window)

    glad_load_gl_loader()

    # Vertex data (positions + colors)
    # fmt: off
    vertices: list[float32] = [
        -0.5, -0.5, 0.0, 
        1.0, 0.0, 0.0,  # bottom left (red)
        0.5, -0.5, 0.0,
        0.0, 1.0, 0.0,  # bottom right (green)
        0.0, 0.5, 0.0,
        0.0, 0.0, 1.0,  # top (blue)
    ]
    # fmt: on

    # Create VAO and VBO
    VAO: GLuint = glGenVertexArrays(1)
    VBO: GLuint = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(
        GL_ARRAY_BUFFER,
        len(vertices) * sizeof(GLfloat),
        np_arr(vertices),
        GL_STATIC_DRAW,
    )

    # Position attribute
    glVertexAttribPointer(
        0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), ctypes.c_void_p(0)
    )
    glEnableVertexAttribArray(0)

    # Color attribute
    glVertexAttribPointer(
        1,
        3,
        GL_FLOAT,
        GL_FALSE,
        6 * sizeof(GLfloat),
        ctypes.c_void_p(3 * sizeof(GLfloat)),
    )
    glEnableVertexAttribArray(1)

    # Build shader program
    shader_program: int = create_shader_program()

    # Main render loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    # Cleanup
    glDeleteVertexArrays(1, [VAO])
    glDeleteBuffers(1, [VBO])
    glfw.terminate()


if __name__ == "__main__":
    opengl_test()
