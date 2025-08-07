import os

from pypp_core.src.main_scripts.format import pypp_format
from pypp_core.src.main_scripts.transpile import pypp_transpile
import argparse


def main():
    parser = argparse.ArgumentParser(description="pypp CLI tool")
    parser.add_argument("directory", help="Path to the input directory")
    args = parser.parse_args()

    # Optionally, check that it exists and is a directory
    if not os.path.isdir(args.directory):
        parser.error(f"The path {args.directory} is not a valid directory.")

    files_added_or_modified = pypp_transpile()
    pypp_format(files_added_or_modified)


if __name__ == "__main__":
    main()
