import os
import sys

from pypp_core.cli import main_cli

dirname: str = os.path.dirname(__file__)


def run_cli(args):
    sys.argv = ["prog"] + args  # "prog" simulates the script name
    test_dir = os.path.join(dirname, "../../../../../pypp_test_dir/main_test_proj")
    main_cli(test_dir)
