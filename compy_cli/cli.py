from pathlib import Path
import argparse

from compy_cli.src.do import compy_do
from compy_cli.src.initializers.init import compy_init
from compy_cli.src.initializers.init_bridge_library import compy_init_bridge_library
from compy_cli.src.initializers.init_pure_library import (
    compy_init_pure_library,
)
from compy_cli.src.install import compy_install
from compy_cli.src.delete_timestamps import compy_delete_timestamps
from compy_cli.src.run_python import compy_run_python
from compy_cli.src.uninstall import compy_uninstall


def main_cli(absolute_dir: Path | None = None) -> None:
    parser = argparse.ArgumentParser(description="compy CLI tool.")
    subparsers = parser.add_subparsers(dest="mode", required=False)
    subparsers.add_parser(
        "init", help="Initialize a new Compy project in the current directory."
    )
    parser_install = subparsers.add_parser("install", help="Install compy libraries")
    parser_install.add_argument(
        "libraries", help="Specify one or more libraries to install.", nargs="+"
    )
    parser_uninstall = subparsers.add_parser(
        "uninstall", help="Uninstall compy libraries"
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
    parser_main.add_argument(
        "--exe_name",
        "-e",
        help="The name of the executable to run "
        "(required if 'run' is one of the tasks).",
        required=False,
    )
    parser_init_bridge = subparsers.add_parser(
        "init_bridge_library",
        help="Initialize a new Compy bridge-library in the current directory.",
    )
    parser_init_bridge.add_argument(
        "library_name",
        help="The name of the bridge-library to initialize.",
    )
    parser_init_pure = subparsers.add_parser(
        "init_pure_library",
        help="Initialize a new Compy pure-library in the current directory.",
    )
    parser_init_pure.add_argument(
        "library_name",
        help="The name of the pure-library to initialize.",
    )

    args = parser.parse_args()
    if absolute_dir is None:
        absolute_dir = Path.cwd()
    if args.mode == "init":
        compy_init(absolute_dir)
    elif args.mode == "init_bridge_library":
        compy_init_bridge_library(args.library_name, absolute_dir)
    elif args.mode == "init_pure_library":
        compy_init_pure_library(args.library_name, absolute_dir)
    # TODO now: fix
    elif not (absolute_dir / "compy_files" / "proj_info.json").exists():
        parser.error(
            "compy_files/proj_info.json file not found. "
            "Ensure your Compy project is properly initialized."
        )

    if args.mode == "do":
        if "run" in args.tasks and not args.exe_name:
            parser.error(
                "argument --exe_name/-e is required when 'run' is one of the tasks."
            )
        compy_do(args.tasks, absolute_dir, args.exe_name)
    elif args.mode == "install":
        for lib in args.libraries:
            compy_install(lib, absolute_dir)
    elif args.mode == "uninstall":
        for lib in args.libraries:
            compy_uninstall(lib, absolute_dir)
    elif args.mode == "delete_timestamps":
        compy_delete_timestamps(absolute_dir)
    elif args.mode == "run_python":
        compy_run_python(args.file, absolute_dir)


if __name__ == "__main__":
    main_cli()
