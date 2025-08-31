from pathlib import Path

from compy_cli.src.transpilers.other.other.bridge_json_path_cltr import (
    BridgeJsonPathCltr,
)
from compy_cli.src.transpilers.other.maps.maps import MapsCltr
from compy_cli.src.transpilers.other.maps.util.calc_import_map import ImportMapCltr
from compy_cli.src.transpilers.other.maps.util.calc_map_1 import MapCltr1
from compy_cli.src.transpilers.other.maps.util.calc_map_2 import MapCltr2
from compy_cli.src.transpilers.other.transpiler.transpiler import Transpiler


def create_transpiler(
    bridge_json_path_cltr: BridgeJsonPathCltr,
    bridge_libs: list[str],
    src_py_files: list[Path],
) -> Transpiler:
    maps_cltr = MapsCltr(
        MapCltr1(bridge_libs, bridge_json_path_cltr),
        MapCltr2(bridge_libs, bridge_json_path_cltr),
        ImportMapCltr(bridge_libs, bridge_json_path_cltr),
    )
    return Transpiler(src_py_files, maps_cltr.calc_maps())
