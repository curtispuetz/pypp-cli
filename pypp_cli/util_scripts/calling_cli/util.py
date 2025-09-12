import os
from pathlib import Path
import sys

from pypp_cli.cli import main_cli

dirname = Path(__file__).parent


def run_cli(args, test_dir: Path | None = None):
    sys.argv = ["prog"] + args  # "prog" simulates the script name
    if test_dir is None:
        test_dir = dirname.parent.parent / "test_dir"
    main_cli(test_dir)


def calc_test_dir_python_executable() -> str:
    return os.path.join(dirname, "../../test_dir/python/.venv/Scripts/python.exe")
