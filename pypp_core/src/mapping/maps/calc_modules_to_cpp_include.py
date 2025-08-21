from dataclasses import dataclass
import json
from pathlib import Path
from pypp_core.src.config import PyppDirs


def _calc_module_beginning(module: str) -> str:
    f = module.find(".")
    if f == -1:
        return module
    return module[:f]


@dataclass(frozen=True, slots=True)
class ModulesToCppInclude:
    modules: set[str]
    libraries: set[str]

    def contains(self, name: str) -> bool:
        return name in self.modules or _calc_module_beginning(name) in self.libraries


def calc_modules_to_cpp_include(proj_info: dict, dirs: PyppDirs) -> ModulesToCppInclude:
    modules: set[str] = set()
    libraries: set[str] = set()
    for installed_library in proj_info["installed_libraries"]:
        json_path: Path = dirs.calc_bridge_json(
            installed_library, "modules_to_cpp_include_map"
        )
        if json_path.is_file():
            with open(json_path, "r") as f:
                # Note: Json should already be verified valid on library install.
                r: list[str] = json.load(f)
                if len(r) == 1 and r[0] == "all":
                    libraries.add(installed_library)
                else:
                    modules.update(r)
    return ModulesToCppInclude(modules, libraries)
