import json
from pathlib import Path
import shutil
from importlib.resources import files, as_file

from pypp_core.src.config import PyppDirs
from pypp_core.src.util.util import rm_dirs_and_files


def initialize_cpp_project(dirs: PyppDirs, proj_info: dict):
    rm_dirs_and_files(dirs.cpp_dir, {"libs"})
    _copy_cpp_template_to_cpp_dir(dirs)
    # Need to remove the timestamps file because all the C++ files need to be
    # generated again.
    if dir.timestamps_file.exists():
        dir.timestamps_file.unlink()
    _set_cpp_dir_not_dirty_in_json(dirs, proj_info)


def _copy_cpp_template_to_cpp_dir(dirs: PyppDirs):
    print("Copying the C++ template to the cpp project directory")
    # Copy files and directories from the template
    template_root = files("pypp_core.data.cpp_template")
    for item in template_root.iterdir():
        with as_file(item) as src_path:
            dst_path: Path = dir.cpp_dir / item.name
            if src_path.is_dir():
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)


def _set_cpp_dir_not_dirty_in_json(dirs: PyppDirs, proj_info: dict):
    proj_info["cpp_dir_is_dirty"] = False
    with open(dirs.proj_info_file, "w") as file:
        json.dump(proj_info, file, indent=4)
