import subprocess
from pypp_cli.util_scripts.calling_cli.util import calc_test_dir_python_executable

if __name__ == "__main__":
    libs = [
        # r"C:\Users\puetz\PycharmProjects\bridge-library-test-0",
        # r"C:\Users\puetz\PycharmProjects\bridge-library-test-1",
        # r"C:\Users\puetz\PycharmProjects\bridge-lib-glfw",
        # r"C:\Users\puetz\PycharmProjects\pure-library-test-0",
        r"C:\Users\puetz\PycharmProjects\bridge-lib-opengl",
        # r"C:\Users\puetz\PycharmProjects\pypp-python",
    ]
    subprocess.check_call(
        [
            calc_test_dir_python_executable(),
            "-m",
            "pip",
            "install",
            *libs,
        ]
    )
