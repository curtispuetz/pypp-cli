from pathlib import Path
import argparse

from pypp_cli.src.doers.proj.do import pypp_do
from pypp_cli.src.initializers.init import pypp_init
from pypp_cli.src.initializers.init_bridge_library import pypp_init_bridge_library
from pypp_cli.src.initializers.init_pure_library import (
    pypp_init_pure_lib,
)
from pypp_cli.src.other.pypp_paths.util import calc_proj_info_path
from pypp_cli.src.package_managers.install import pypp_install
from pypp_cli.src.doers.pure_lib.do_pure_lib import pypp_do_pure_lib
from pypp_cli.src.timestamps_deleter.delete_timestamps import pypp_delete_timestamps
from pypp_cli.src.python_runner.run_python import pypp_run_python
from pypp_cli.src.package_managers.uninstall import pypp_uninstall


def main_cli(absolute_dir: Path | None = None) -> None:
    parser = argparse.ArgumentParser(description="pypp CLI tool.")
    subparsers = parser.add_subparsers(dest="mode", required=False)
    subparsers.add_parser(
        "init", help="Initialize a new Py++ project in the current directory."
    )
    parser_install = subparsers.add_parser("install", help="Install pypp libraries")
    parser_install.add_argument(
        "libraries", help="Specify one or more libraries to install.", nargs="+"
    )
    parser_uninstall = subparsers.add_parser(
        "uninstall", help="Uninstall pypp libraries"
    )
    parser_uninstall.add_argument(
        "libraries", help="Specify one or more libraries to uninstall.", nargs="+"
    )
    subparsers.add_parser(
        "delete_timestamps",
        help="Remove the file_timestamps.json file so that transpiling is done "
        "for all python files regardless of whether they were modified.",
    )
    parser_run_python = subparsers.add_parser(
        "run_python",
        help="run your code with the python interpreter. Behaviour should be the same "
        "as the C++ executable, but could be different if there is a bug.",
    )
    parser_run_python.add_argument(
        "file", help="The Python file to run. This should be a file with main block."
    )
    parser_do = subparsers.add_parser(
        "do", help="transpile, format, build, and/or run."
    )
    parser_do.add_argument(
        "tasks",
        help="Transpile your python code to C++, format the generated C++ code, build "
        "the C++ code, and/or run the resulting executable. You can choose one or "
        "multiple, and in any order (though, not every order makes sense)."
        "For example, 'transpile format build run' will do everything and run the "
        "resulting executable.'",
        choices=["transpile", "format", "build", "run"],
        nargs="+",
    )
    parser_do.add_argument(
        "--exe_name",
        "-e",
        help="The name of the executable to run "
        "(required if 'run' is one of the tasks).",
        required=False,
    )
    parser_do_pure_lib = subparsers.add_parser(
        "do_pure_lib", help="transpile and format a pure library"
    )
    parser_do_pure_lib.add_argument(
        "tasks",
        help="Transpile your python code to C++ and format the generated C++ code."
        "You can choose only transpile or transpile and format. "
        "For example, 'transpile format' will do both, and 'transpile' will only "
        "transpile.",
        choices=["transpile", "format"],
        nargs="+",
    )
    parser_init_bridge = subparsers.add_parser(
        "init_bridge_library",
        help="Initialize a new Py++ bridge-library in the current directory.",
    )
    parser_init_bridge.add_argument(
        "library_name",
        help="The name of the bridge-library to initialize.",
    )
    parser_init_pure = subparsers.add_parser(
        "init_pure_lib",
        help="Initialize a new Py++ pure-library in the current directory.",
    )
    parser_init_pure.add_argument(
        "library_name",
        help="The name of the pure-library to initialize.",
    )

    args = parser.parse_args()
    if absolute_dir is None:
        absolute_dir = Path.cwd()
    if args.mode == "init":
        pypp_init(absolute_dir)
    elif args.mode == "init_bridge_library":
        pypp_init_bridge_library(args.library_name, absolute_dir)
    elif args.mode == "init_pure_lib":
        pypp_init_pure_lib(args.library_name, absolute_dir)
    elif not calc_proj_info_path(absolute_dir).exists():
        parser.error(
            "pypp_files/proj_info.json file not found. "
            "Ensure your Py++ project is properly initialized."
        )

    if args.mode == "do":
        if "run" in args.tasks and not args.exe_name:
            parser.error(
                "argument --exe_name/-e is required when 'run' is one of the tasks."
            )
        pypp_do(args.tasks, absolute_dir, args.exe_name)
    if args.mode == "do_pure_lib":
        pypp_do_pure_lib(args.tasks, absolute_dir)
    elif args.mode == "install":
        for lib in args.libraries:
            pypp_install(lib, absolute_dir)
    elif args.mode == "uninstall":
        for lib in args.libraries:
            pypp_uninstall(lib, absolute_dir)
    elif args.mode == "delete_timestamps":
        pypp_delete_timestamps(absolute_dir)
    elif args.mode == "run_python":
        pypp_run_python(args.file, absolute_dir)


if __name__ == "__main__":
    main_cli()
