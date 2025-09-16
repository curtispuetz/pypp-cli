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
    src_py_files: list[Path],
    py_files_tracker: PyFilesTracker,
) -> Transpiler:
    maps_cltr = MapsCltr(
        MapCltr1(bridge_libs, bridge_json_path_cltr),
        MapCltr2(bridge_libs, bridge_json_path_cltr),
        ImportMapCltr(bridge_libs, bridge_json_path_cltr),
    )
    return Transpiler(src_py_files, maps_cltr.calc_maps(), py_files_tracker)
