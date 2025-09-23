from pathlib import Path

from pypp_cli.delete_timestamps.node import pypp_delete_timestamps
from pypp_cli.y.proj_info import ProjInfo, load_proj_info
from pypp_cli.y.calc_cpp_dir import calc_cpp_dir
import shutil


def pypp_delete_cpp_libs(target_dir: Path):
    pypp_dir = target_dir / ".pypp"
    proj_info_file = pypp_dir / "proj_info.json"
    proj_info: ProjInfo = load_proj_info(proj_info_file)

    libs_dir: Path = calc_cpp_dir(proj_info, target_dir) / "libs"

    if not libs_dir.exists():
        print("C++ libs directory does not exist, nothing to remove")
    else:
        shutil.rmtree(libs_dir)
        print("C++ libs directory deleted")

    pypp_delete_timestamps(target_dir)
