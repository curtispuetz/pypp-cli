import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.transpiler.create_all_data import InitializeCppProjectDeps
from compy_cli.src.library.file_actions import rm_dirs_and_files


def initialize_cpp_project(d: InitializeCppProjectDeps):
    rm_dirs_and_files(d.dirs.cpp_dir, {"libs"})
    _copy_cpp_template_to_cpp_dir(d.dirs)
    # Need to remove the timestamps file because all the C++ files need to be
    # generated again.
    if d.dirs.timestamps_file.exists():
        d.dirs.timestamps_file.unlink()
    _set_cpp_dir_not_dirty_in_json(d)


def _copy_cpp_template_to_cpp_dir(dirs: CompyDirs):
    print("Copying the C++ template to the cpp project directory")
    # Copy files and directories from the template
    template_root = files("compy_cli.data.cpp_template")
    for item in template_root.iterdir():
        with as_file(item) as src_path:
            dst_path: Path = dirs.cpp_dir / item.name
            if src_path.is_dir():
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)


def _set_cpp_dir_not_dirty_in_json(d: InitializeCppProjectDeps):
    with open(d.dirs.proj_info_file, "w") as file:
        json.dump(
            {
                "cpp_dir_is_dirty": False,
                "ignore_src_files": d.proj_info.ignored_src_files,
                "ignore_main_files": d.proj_info.ignored_main_files,
                "installed_bridge_libraries": d.proj_info.installed_bridge_libs,
            },
            file,
            indent=4,
        )
