import json
from pathlib import Path

from pypp_cli.delete_timestamps.node import pypp_delete_timestamps
from pypp_cli.y.calc_cpp_dir import calc_cpp_dir
from pypp_cli.y.proj_info import ProjInfo, load_proj_info
import shutil


def pypp_delete_cpp(target_dir: Path):
    pypp_dir = target_dir / ".pypp"
    proj_info_file = pypp_dir / "proj_info.json"
    proj_info: ProjInfo = load_proj_info(proj_info_file)

    cpp_dir: Path = calc_cpp_dir(proj_info, target_dir)
    if not cpp_dir.exists():
        print("cpp directory does not exist, nothing to remove")
    else:
        shutil.rmtree(cpp_dir)
        print("cpp directory deleted")

    pypp_delete_timestamps(target_dir)
    _set_cpp_dir_is_dirty_and_save_json(proj_info, proj_info_file)


def _set_cpp_dir_is_dirty_and_save_json(proj_info: ProjInfo, proj_info_file: Path):
    proj_info.cpp_dir_is_dirty = True
    with open(proj_info_file, "w") as file:
        json.dump(proj_info.model_dump(), file, indent=4)
