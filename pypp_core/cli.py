import os

import argparse

from pypp_core.src.config import PyppDirs
from pypp_core.src.main_scripts.do import pypp_do
from pypp_core.src.main_scripts.install import pypp_install
from pypp_core.src.main_scripts.remove_timestamps import pypp_remove_timestamps


def main():
    parser = argparse.ArgumentParser(description="pypp CLI tool")
    parser.add_argument("project_dir", help="Path to the Py++ project dir")
    subparsers = parser.add_subparsers(
        dest="mode", required=False, help="install or remove_timestamps"
    )
    subparsers.add_parser("install", help="Install pypp libraries")
    subparsers.add_parser("init", help="Initialize a new Py++ project in the given directory")
    subparsers.add_parser(
        "remove_timestamps",
        help="Remove the file_timestamps.json file so that Python transpiling is done "
        "for all files regardless of whether they were modified.",
    )
    parser_main = subparsers.add_parser(
        "do", help="transpile, format, build, and/or run"
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
    if not os.path.isdir(args.project_dir):
        parser.error(f"The path {args.project_dir} is not a valid directory.")
    absolute_dir = os.path.abspath(args.project_dir)
    print("Using directory:", absolute_dir)

    pypp_dirs = PyppDirs(absolute_dir)

    if args.mode == "do":
        pypp_do(args.tasks, pypp_dirs)
    elif args.mode == "install":
        pypp_install()
    elif args.mode == "remove_timestamps":
        pypp_remove_timestamps(pypp_dirs)


if __name__ == "__main__":
    main()
