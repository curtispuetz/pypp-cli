from compy_cli.util_scripts.calling_cli.util import run_cli

if __name__ == "__main__":
    run_cli(
        [
            "uninstall",
            r"C:\Users\puetz\PycharmProjects\compy-bridge-library-test-0"
            r"\dist\compy_bridge_library_test_0-0.0.0-py3-none-any.whl",
            r"C:\Users\puetz\PycharmProjects\compy-bridge-library-test-1"
            r"\dist\compy_bridge_library_test_1-0.0.0-py3-none-any.whl",
        ]
    )
