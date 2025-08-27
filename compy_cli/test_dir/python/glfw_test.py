import glfw
from compy_bridge_lib_glfw.d_types import GLFWwindowPtr
from compy_python.nones import NULL
from compy_python.strings import to_c_string


def glfw_test():
    # Initialize the library
    if not glfw.init():
        raise Exception("Failed to initialize GLFW")
    # Create a windowed mode window and its OpenGL context
    window: GLFWwindowPtr = glfw.create_window(
        640, 480, to_c_string("Hello World"), NULL, NULL
    )
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    glfw_test()
