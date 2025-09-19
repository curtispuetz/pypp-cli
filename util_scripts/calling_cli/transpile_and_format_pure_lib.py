from pathlib import Path
from util_scripts.calling_cli.util import run_cli


if __name__ == "__main__":
    run_cli(
        ["do_pure_lib", "transpile", "format"],
        Path(r"C:\Users\puetz\PycharmProjects\pypp-pure-library-test-0"),
    )
