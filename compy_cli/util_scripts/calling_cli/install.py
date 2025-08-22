from pypp_core.util_scripts.calling_cli.util import run_cli

if __name__ == "__main__":
    run_cli(
        [
            "install",
            r"C:\Users\puetz\PycharmProjects\pypp-bridge-library-test-0"
            r"\dist\pypp_bridge_library_test_0-0.0.0-py3-none-any.whl",
            r"C:\Users\puetz\PycharmProjects\pypp-bridge-library-test-1"
            r"\dist\pypp_bridge_library_test_1-0.0.0-py3-none-any.whl",
        ]
    )
