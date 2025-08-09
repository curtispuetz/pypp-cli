import os

from pypp_core.util_scripts.calling_cli.util import run_cli

dirname: str = os.path.dirname(__file__)
if __name__ == "__main__":
    main_file = os.path.join(
        dirname, "../../../../../pypp_test_dir/main_test_proj/python/main.py"
    )
    run_cli(["run_python", main_file])
