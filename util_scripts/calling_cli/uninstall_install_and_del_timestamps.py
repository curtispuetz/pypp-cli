from util_scripts.calling_cli.util import run_cli


if __name__ == "__main__":
    package = r"C:\Users\puetz\PycharmProjects\bridge-lib-opengl"
    name = "pypp_bridge_lib_opengl"
    run_cli(["uninstall", name])
    run_cli(["install", package])
    run_cli(["delete_timestamps"])
