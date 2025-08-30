from pathlib import Path
import shutil

from compy_cli.src.dirs_cltr import calc_cpp_libs_dir


def delete_all_bridge_lib_cpp_files(cpp_dir: Path, deleted_bridge_libs: list[str]):
    for lib in deleted_bridge_libs:
        _delete_cpp_library_files(cpp_dir, lib)


def _delete_cpp_library_files(cpp_dir: Path, library_name: str):
    dest_dir = calc_cpp_libs_dir(cpp_dir, library_name)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
