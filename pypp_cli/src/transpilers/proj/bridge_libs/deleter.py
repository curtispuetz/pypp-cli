from pathlib import Path
import shutil

from pypp_cli.src.transpilers.proj.bridge_libs.util import calc_cpp_libs_dir


def delete_all_cpp_lib_files(cpp_dir: Path, lib_names: list[str]):
    for lib_name in lib_names:
        _delete_cpp_lib_files(cpp_dir, lib_name)
    if len(lib_names) > 0:
        # note: This line comes right after deleted libraries are listed.
        print("Deleted C++ lib files in cpp project directory for deleted libraries")


def _delete_cpp_lib_files(cpp_dir: Path, lib_name: str):
    dest_dir = calc_cpp_libs_dir(cpp_dir, lib_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
