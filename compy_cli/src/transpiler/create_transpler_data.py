from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.maps.maps import MapsCltr
from compy_cli.src.transpiler.maps.util.calc_import_map import ImportMapCltr
from compy_cli.src.transpiler.maps.util.calc_map_1 import MapCltr1
from compy_cli.src.transpiler.maps.util.calc_map_2 import MapCltr2
from compy_cli.src.transpiler.util.transpiler.transpiler import Transpiler


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
