from pathlib import Path

from pypp_cli.src.transpilers.library.bridge_libs.path_cltr import (
    BridgeJsonPathCltr,
)
from pypp_cli.src.transpilers.library.file_tracker import PyFilesTracker
from pypp_cli.src.transpilers.library.transpiler.maps.maps import MapsCltr
from pypp_cli.src.transpilers.library.transpiler.maps.util.calc_import_map import (
    ImportMapCltr,
)
from pypp_cli.src.transpilers.library.transpiler.maps.util.calc_map_1 import MapCltr1
from pypp_cli.src.transpilers.library.transpiler.maps.util.calc_map_2 import MapCltr2
from pypp_cli.src.transpilers.library.transpiler.transpiler import Transpiler


def create_transpiler(
    bridge_json_path_cltr: BridgeJsonPathCltr,
    bridge_libs: list[str],
    py_files: list[Path],
    py_files_tracker: PyFilesTracker,
) -> Transpiler:
    maps_cltr = MapsCltr(
        MapCltr1(bridge_libs, bridge_json_path_cltr),
        MapCltr2(bridge_libs, bridge_json_path_cltr),
        ImportMapCltr(bridge_libs, bridge_json_path_cltr),
    )
    py_modules = _calc_all_modules_for_project(py_files)
    return Transpiler(py_modules, maps_cltr.calc_maps(), py_files_tracker)


def _calc_all_modules_for_project(py_files: list[Path]) -> set[str]:
    ret: set[str] = set()
    for p in py_files:
        if p.stem == "__init__":
            ret.add(p.parent.as_posix().replace("/", "."))
        else:
            ret.add(p.as_posix()[:-3].replace("/", "."))
    return ret
