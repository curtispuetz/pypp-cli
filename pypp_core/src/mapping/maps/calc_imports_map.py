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
class ImportsMap:
    modules: set[str]
    libraries: set[str]

    def contains(self, name: str) -> bool:
        return name in self.modules or _calc_module_beginning(name) in self.libraries


def calc_imports_map(proj_info: dict, dirs: PyppDirs) -> ImportsMap:
    modules: set[str] = set()
    libraries: set[str] = set()
    for installed_library in proj_info["installed_libraries"]:
        json_path: Path = dirs.calc_bridge_json(installed_library, "imports_map")
        if json_path.is_file():
            with open(json_path, "r") as f:
                # Note: Json should already be verified valid on library install.
                r: dict[str, list[str]] = json.load(f)
                if "direct_to_cpp_include" in r:
                    modules.update(r["direct_to_cpp_include"])
                else:
                    assert "ignore" in r, (
                        f"Invalid imports_map.json from library '{installed_library}'. "
                        f"This should not happen because the library should be "
                        f"verified on install"
                    )
                    if len(r["ignore"]) == 0:
                        libraries.add(installed_library)
                    else:
                        raise NotImplementedError("ignore values in imports_map.json")
    return ImportsMap(modules, libraries)
