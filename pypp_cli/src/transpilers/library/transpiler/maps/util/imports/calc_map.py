from dataclasses import dataclass
import json
from pathlib import Path

from pypp_cli.src.transpilers.library.transpiler.maps.util.util import MapCltrAlgo
from pypp_cli.src.transpilers.library.transpiler.util.modules import (
    calc_module_beginning,
)


@dataclass(frozen=True, slots=True)
class ImportMap:
    _direct_to_cpp_include: set[str]
    # The key is the library name and the value is the ignored set
    _ignore: dict[str, set[str]]

    def contains(self, module: str) -> bool:
        if module in self._direct_to_cpp_include:
            return True
        key = calc_module_beginning(module)
        if key in self._ignore:
            if module not in self._ignore[key]:
                return True
        return False


@dataclass(frozen=True, slots=True)
class ImportMapCltr(MapCltrAlgo):
    def calc_import_map(self) -> ImportMap:
        dtc_include: set[str] = set()
        ignore: dict[str, set[str]] = {}
        for lib, has_bridge_jsons in self._libs.items():
            if not has_bridge_jsons:
                # In this case every import should be included.
                ignore[lib] = set()
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                lib, "import_map"
            )
            if not json_path.is_file():
                continue
            self._calc_for_lib(json_path, lib, dtc_include, ignore)
        return ImportMap(dtc_include, ignore)

    def _calc_for_lib(
        self,
        json_path: Path,
        lib: str,
        dtc_include: set[str],
        ignore: dict[str, set[str]],
    ):
        with open(json_path, "r") as f:
            r: dict[str, list[str]] = json.load(f)
        if "direct_to_cpp_include" in r:
            dtc_include.update(r["direct_to_cpp_include"])
        else:
            assert "ignore" in r, (
                f"Invalid import_map.json from library "
                f"'{lib}'. "
                f"This should not happen because the library should be "
                f"verified on install."
            )
            if len(r["ignore"]) == 0:
                ignore[lib] = set()
            else:
                ignore[lib] = set(r["ignore"])
