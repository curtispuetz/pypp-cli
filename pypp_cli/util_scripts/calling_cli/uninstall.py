import subprocess

from pypp_cli.util_scripts.calling_cli.util import calc_test_dir_python_executable

if __name__ == "__main__":
    libs = [
        "pypp_bridge_library_test_0",
        "pypp_bridge_library_test_1",
        "pypp_pure_library_test_0",
        "pypp_bridge_lib_glfw",
        "pypp_bridge_lib_opengl",
        # "pypp_python"
    ]
    subprocess.check_call(
        [
            calc_test_dir_python_executable(),
            "-m",
            "pip",
            "uninstall",
            "-y",
            *libs,
        ]
    )
