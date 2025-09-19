from pathlib import Path
import argparse

from pypp_cli.do.node import pypp_do
from pypp_cli.init.node import pypp_init
from pypp_cli.init_bridge_lib.node import pypp_init_bridge_lib
from pypp_cli.init_pure_lib.node import (
    pypp_init_pure_lib,
)
from pypp_cli.delete_timestamps.node import pypp_delete_timestamps


def main_cli(absolute_dir: Path | None = None) -> None:
    parser = argparse.ArgumentParser(description="pypp CLI tool.")
    subparsers = parser.add_subparsers(dest="mode", required=False)
    subparsers.add_parser(
        "init", help="Initialize a new Py++ project in the current directory."
    )
    subparsers.add_parser(
        "delete_timestamps",
        help="Remove the file_timestamps.json file so that transpiling is done "
        "for all python files regardless of whether they were modified.",
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
    parser_init_bridge = subparsers.add_parser(
        "init_bridge_lib",
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
    elif args.mode == "init_bridge_lib":
        pypp_init_bridge_lib(args.library_name, absolute_dir)
    elif args.mode == "init_pure_lib":
        pypp_init_pure_lib(args.library_name, absolute_dir)
    elif not (absolute_dir / ".pypp" / "proj_info.json").exists():
        parser.error(
            ".pypp/proj_info.json file not found. "
            "Ensure your Py++ project is properly initialized."
        )

    if args.mode == "do":
        if "run" in args.tasks and not args.exe_name:
            parser.error(
                "argument --exe_name/-e is required when 'run' is one of the tasks."
            )
        pypp_do(args.tasks, absolute_dir, args.exe_name)
    elif args.mode == "delete_timestamps":
        pypp_delete_timestamps(absolute_dir)


if __name__ == "__main__":
    main_cli()
