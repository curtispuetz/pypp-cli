from pathlib import Path
from pypp_cli.util_scripts.calling_cli.util import run_cli


if __name__ == "__main__":
    run_cli(
        ["init_bridge_lib", "pypp-bridge-lib-opengl"],
        Path(r"C:\Users\puetz\PycharmProjects\bridge-lib-opengl"),
    )
