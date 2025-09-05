from pypp_cli.util_scripts.calling_cli.util import run_cli

if __name__ == "__main__":
    run_cli(
        [
            "uninstall",
            # "pypp_bridge_library_test_0",
            # "pypp_bridge_library_test_1",
            # "pypp_pure_library_test_0",
            # "pypp_bridge_lib_glfw",
            "pypp_bridge_lib_opengl",
        ]
    )
