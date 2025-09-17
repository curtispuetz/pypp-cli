import os
from pathlib import Path
import sys

from pypp_cli.cli import main_cli

dirname = Path(__file__).parent


def run_cli(args, test_dir: Path | None = None):
    sys.argv = ["prog"] + args  # "prog" simulates the script name
    if test_dir is None:
        test_dir = calc_test_dir()
    main_cli(test_dir)


def calc_test_dir() -> Path:
    # return dirname.parent.parent / "test_dir"
    return dirname.parent.parent.parent.parent / "pure-library-test-0"


def calc_test_dir_python_executable() -> str:
    return os.path.join(calc_test_dir(), ".venv/Scripts/python.exe")
