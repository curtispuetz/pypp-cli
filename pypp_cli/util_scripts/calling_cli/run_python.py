import os

from pypp_cli.util_scripts.calling_cli.util import run_cli

dirname: str = os.path.dirname(__file__)
if __name__ == "__main__":
    # TODO later: Fix because this command is deleted
    main_file = os.path.join(dirname, "../../test_dir/python/main.py")
    run_cli(["run_python", main_file])
