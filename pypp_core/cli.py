import os

import argparse

from pypp_core.src.config import PyppDirs
from pypp_core.src.main_scripts.do import pypp_do
from pypp_core.src.main_scripts.init import pypp_init
from pypp_core.src.main_scripts.install import pypp_install
from pypp_core.src.main_scripts.remove_timestamps import pypp_remove_timestamps


def main():
    parser = argparse.ArgumentParser(description="pypp CLI tool.")
    subparsers = parser.add_subparsers(dest="mode", required=False)
    subparsers.add_parser(
        "init", help="Initialize a new Py++ project in the given directory."
    )
    parser_install = subparsers.add_parser("install", help="Install pypp libraries")
    parser_install.add_argument("library", help="Specify the library to install.")
    subparsers.add_parser(
        "remove_timestamps",
        help="Remove the file_timestamps.json file so that transpiling is done "
        "for all python files regardless of whether they were modified.",
    )
    parser_main = subparsers.add_parser(
        "do", help="transpile, format, build, and/or run."
    )
    parser_main.add_argument(
        "tasks",
        help="Transpile your python code to C++, format the generated C++ code, build "
        "the C++ code, and/or run the resulting executable. You can choose one or "
        "multiple, and in any order (though, not every order makes sense)."
        "For example, 'transpile format build run' will do everything and run the "
        "resulting executable.'",
        choices=["transpile", "format", "build", "run"],
        nargs="+",
    )

    args = parser.parse_args()
    absolute_dir = os.getcwd()
    pypp_dirs = PyppDirs(absolute_dir)
    if args.mode == "init":
        pypp_init(pypp_dirs)
    elif not os.path.exists(pypp_dirs.proj_info_file):
        parser.error(
            "pypp_data/proj_info.json file not found. "
            "Ensure your Py++ project is properly initialized."
        )

    if args.mode == "do":
        pypp_do(args.tasks, pypp_dirs)
    elif args.mode == "install":
        pypp_install(args.library, pypp_dirs)
    elif args.mode == "remove_timestamps":
        pypp_remove_timestamps(pypp_dirs)


if __name__ == "__main__":
    main()
