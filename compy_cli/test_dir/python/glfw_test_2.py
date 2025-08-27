import glfw
from compy_python.nones import NULL
from compy_python.strings import to_c_string
from compy_bridge_lib_glfw.d_types import GLFWwindowPtr


def key_callback(
    _window: GLFWwindowPtr, key: int, _scancode: int, action: int, _mods: int
):
    if action == glfw.PRESS:
        print(f"Key {key} pressed")
    elif action == glfw.RELEASE:
        print(f"Key {key} released")


def mouse_button_callback(_window: GLFWwindowPtr, button: int, action: int, _mods: int):
    if action == glfw.PRESS:
        print(f"Mouse button {button} pressed")
    elif action == glfw.RELEASE:
        print(f"Mouse button {button} released")


def cursor_position_callback(_window: GLFWwindowPtr, xpos: float, ypos: float):
    print(f"Mouse moved to ({xpos}, {ypos})")


def glfw_test_2():
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

    # Set input callbacks
    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using pyOpenGL

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    glfw_test_2()
