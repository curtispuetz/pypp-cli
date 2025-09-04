from pathlib import Path
from pypp_cli.util_scripts.calling_cli.util import run_cli


if __name__ == "__main__":
    run_cli(
        ["init_pure_lib", "pypp-pure-library-test-0"],
        Path(r"C:\Users\puetz\PycharmProjects\pypp-pure-library-test-0"),
    )
