from dataclasses import dataclass
from pathlib import Path

from compy_cli.src.bridge_json_path_cltr import BridgeJsonPathCltr
from compy_cli.src.transpiler.maps.maps import MapsCltr, MapsCltrDeps
from compy_cli.src.transpiler.maps.util.calc_import_map import ImportMapCltr
from compy_cli.src.transpiler.maps.util.calc_map_1 import MapCltr1
from compy_cli.src.transpiler.maps.util.calc_map_2 import MapCltr2
from compy_cli.src.transpiler.maps.util.util import MapsCltrAlgoDeps
from compy_cli.src.transpiler.util.transpiler._helper import TranspilerDeps
from compy_cli.src.transpiler.util.transpiler.transpiler import (
    Transpiler,
)


@dataclass(frozen=True, slots=True)
class TranspilerData:
    _transpiler_deps: TranspilerDeps
    transpiler: Transpiler


def create_transpiler_data(
    bridge_json_path_cltr: BridgeJsonPathCltr,
    installed_bridge_libs: dict[str, str],
    src_py_files: list[Path],
) -> TranspilerData:
    maps_cltr = create_maps_cltr(bridge_json_path_cltr, installed_bridge_libs)
    transpiler_deps = TranspilerDeps(
        src_py_files,
        maps_cltr.calc_maps(),
    )
    return TranspilerData(transpiler_deps, Transpiler(transpiler_deps))


def create_maps_cltr(
    bridge_json_path_cltr: BridgeJsonPathCltr,
    installed_bridge_libs: dict[str, str],
):
    maps_cltr_algo_deps = MapsCltrAlgoDeps(installed_bridge_libs, bridge_json_path_cltr)
    map_cltr1 = MapCltr1(maps_cltr_algo_deps)
    map_cltr2 = MapCltr2(maps_cltr_algo_deps)
    import_map_cltr = ImportMapCltr(maps_cltr_algo_deps)
    maps_cltr_deps = MapsCltrDeps(map_cltr1, map_cltr2, import_map_cltr)

    return MapsCltr(maps_cltr_deps)
