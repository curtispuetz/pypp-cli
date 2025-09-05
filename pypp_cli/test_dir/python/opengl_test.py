import glfw
import OpenGL.GL as GL
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


def compile_shader(source: str, shader_type: GL.GLenum) -> int:
    shader: GL.GLuint = GL.glCreateShader(shader_type)
    GL.glShaderSource(shader, source)
    GL.glCompileShader(shader)
    if not GL.glGetShaderiv(shader, GL.GL_COMPILE_STATUS):
        raise RuntimeError(
            "Shader compilation failed: " + GL.glGetShaderInfoLog(shader)
        )
    return shader


def create_shader_program():
    vertex_shader: GL.GLuint = compile_shader(VERTEX_SHADER, GL.GL_VERTEX_SHADER)
    fragment_shader: GL.GLuint = compile_shader(FRAGMENT_SHADER, GL.GL_FRAGMENT_SHADER)

    program: GL.GLuint = GL.glCreateProgram()
    GL.glAttachShader(program, vertex_shader)
    GL.glAttachShader(program, fragment_shader)
    GL.glLinkProgram(program)

    if not GL.glGetProgramiv(program, GL.GL_LINK_STATUS):
        raise RuntimeError("Program linking failed: " + GL.glGetProgramInfoLog(program))

    GL.glDeleteShader(vertex_shader)
    GL.glDeleteShader(fragment_shader)

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
    VAO: GL.GLuint = GL.glGenVertexArrays(1)
    VBO: GL.GLuint = GL.glGenBuffers(1)

    GL.glBindVertexArray(VAO)

    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
    GL.glBufferData(
        GL.GL_ARRAY_BUFFER,
        len(vertices) * GL.sizeof(GL.GLfloat),
        np_arr(vertices),
        GL.GL_STATIC_DRAW,
    )

    # Position attribute
    GL.glVertexAttribPointer(
        0, 3, GL.GL_FLOAT, GL.GL_FALSE, 6 * GL.sizeof(GL.GLfloat), ctypes.c_void_p(0)
    )
    GL.glEnableVertexAttribArray(0)

    # Color attribute
    GL.glVertexAttribPointer(
        1,
        3,
        GL.GL_FLOAT,
        GL.GL_FALSE,
        6 * GL.sizeof(GL.GLfloat),
        ctypes.c_void_p(3 * GL.sizeof(GL.GLfloat)),
    )
    GL.glEnableVertexAttribArray(1)

    # Build shader program
    shader_program: GL.GLuint = create_shader_program()

    # Main render loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        GL.glClearColor(0.2, 0.3, 0.3, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glUseProgram(shader_program)
        GL.glBindVertexArray(VAO)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    # Cleanup
    GL.glDeleteVertexArrays(1, [VAO])
    GL.glDeleteBuffers(1, [VBO])
    glfw.terminate()


if __name__ == "__main__":
    opengl_test()
