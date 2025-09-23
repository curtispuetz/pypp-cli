from pathlib import Path
import argparse

from pypp_cli.delete_cpp_libs.node import pypp_delete_cpp_libs
from pypp_cli.do.node import pypp_do
from pypp_cli.init.node import pypp_init
from pypp_cli.delete_timestamps.node import pypp_delete_timestamps
from pypp_cli.delete_cpp.node import pypp_delete_cpp


def main_cli(absolute_dir: Path | None = None) -> None:
    parser = argparse.ArgumentParser(description="pypp CLI tool.")
    subparsers = parser.add_subparsers(dest="mode", required=False)
    subparsers.add_parser(
        "init", help="Initialize a new Py++ project in the current directory."
    )
    subparsers.add_parser(
        "delete_timestamps",
        help="Delete the file_timestamps.json file so that the next transpile is done "
        "for all python files regardless of whether they were modified.",
    )
    subparsers.add_parser(
        "delete_cpp",
        help="Delete everything in the C++ directory so that all C++ code is "
        "regenerated. This also deletes the file_timestamps.json file and sets "
        "cpp_dir_is_dirty to true in proj_info.json.",
    )
    subparsers.add_parser(
        "delete_cpp_libs",
        help="Delete everything in the C++ libs directory. so that the C++ code from "
        "libraries is recopied into it on the next transpile. This also deletes the "
        "file_timestamps.json file.",
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

    args = parser.parse_args()
    if absolute_dir is None:
        absolute_dir = Path.cwd()
    if args.mode == "init":
        pypp_init(absolute_dir)
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
    elif args.mode == "delete_cpp":
        pypp_delete_cpp(absolute_dir)
    elif args.mode == "delete_cpp_libs":
        pypp_delete_cpp_libs(absolute_dir)


if __name__ == "__main__":
    main_cli()
