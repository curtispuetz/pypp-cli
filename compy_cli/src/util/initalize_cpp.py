import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from compy_cli.src.compy_dirs import CompyDirs
from compy_cli.src.main_scripts.util.load_proj_info import ProjInfo
from compy_cli.src.util.util import rm_dirs_and_files


def initialize_cpp_project(dirs: CompyDirs, proj_info: ProjInfo):
    rm_dirs_and_files(dirs.cpp_dir, {"libs"})
    _copy_cpp_template_to_cpp_dir(dirs)
    # Need to remove the timestamps file because all the C++ files need to be
    # generated again.
    if dirs.timestamps_file.exists():
        dirs.timestamps_file.unlink()
    _set_cpp_dir_not_dirty_in_json(dirs, proj_info)


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


def _set_cpp_dir_not_dirty_in_json(dirs: CompyDirs, proj_info: ProjInfo):
    with open(dirs.proj_info_file, "w") as file:
        json.dump(
            {
                "cpp_dir_is_dirty": False,
                "ignore_src_files": proj_info.ignored_src_files,
                "ignore_main_files": proj_info.ignored_main_files,
                "installed_bridge_libraries": proj_info.installed_bridge_libs,
            },
            file,
            indent=4,
        )
