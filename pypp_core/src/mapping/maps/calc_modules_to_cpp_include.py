import json
import os
from pypp_core.src.config import PyppDirs


def calc_modules_to_cpp_include(proj_info: dict, dirs: PyppDirs) -> set[str]:
    ret: set[str] = set()
    for installed_library in proj_info["installed_libraries"]:
        json_path = dirs.calc_bridge_json(
            installed_library, "modules_to_cpp_include_map"
        )
        if os.path.isfile(json_path):
            with open(json_path, "r") as f:
                # Note: Json should already be verified valid on library install.
                ret.update(json.load(f))
    return ret
