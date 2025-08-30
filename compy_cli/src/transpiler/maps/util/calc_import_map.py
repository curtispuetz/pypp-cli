from dataclasses import dataclass
import json
from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr


def _calc_module_beginning(module: str) -> str:
    f = module.find(".")
    if f == -1:
        return module
    return module[:f]


@dataclass(frozen=True, slots=True)
class ImportMap:
    modules: set[str]
    # The value is the ignored set
    libraries: dict[str, set[str]]

    def contains(self, name: str) -> bool:
        if name in self.modules:
            return True
        key = _calc_module_beginning(name)
        if key in self.libraries:
            if name not in self.libraries[key]:
                return True
        return False


@dataclass(frozen=True, slots=True)
class ImportMapCltr:
    _installed_bridge_libs: dict[str, str]
    _bridge_json_path_cltr: BridgeJsonPathCltr

    def calc_import_map(self) -> ImportMap:
        modules: set[str] = set()
        libraries: dict[str, set[str]] = {}
        for installed_library in self._installed_bridge_libs:
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                installed_library, "import_map"
            )
            if json_path.is_file():
                with open(json_path, "r") as f:
                    # Note: Json should already be verified valid on library install.
                    r: dict[str, list[str]] = json.load(f)
                    if "direct_to_cpp_include" in r:
                        modules.update(r["direct_to_cpp_include"])
                    else:
                        assert "ignore" in r, (
                            f"Invalid import_map.json from library "
                            f"'{installed_library}'. "
                            f"This should not happen because the library should be "
                            f"verified on install."
                        )
                        if len(r["ignore"]) == 0:
                            libraries[installed_library] = set()
                        else:
                            libraries[installed_library] = set(r["ignore"])
        return ImportMap(modules, libraries)
