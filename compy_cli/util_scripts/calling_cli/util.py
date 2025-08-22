from pathlib import Path
import sys

from pypp_core.cli import main_cli

dirname = Path(__file__).parent


def run_cli(args):
    sys.argv = ["prog"] + args  # "prog" simulates the script name
    test_dir = dirname.parent.parent / "test_dir"
    main_cli(test_dir)
