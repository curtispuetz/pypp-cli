from dataclasses import dataclass
import json
from typing import Callable
from pathlib import Path

from pypp_cli.src.transpilers.other.transpiler.d_types import (
    PySpecificImport,
)
from pypp_cli.src.transpilers.other.transpiler.maps.util.util import (
    MapCltrAlgo,
    calc_imp_str,
    calc_required_py_import,
)


@dataclass(frozen=True, slots=True)
class MapCltr2(MapCltrAlgo):
    def calc_map_2(
        self,
        default_map: dict[str, set[PySpecificImport | None]],
        json_file_name: str,
        warning_fn: Callable[[str, str], str],
    ) -> dict[str, set[PySpecificImport | None]]:
        ret = default_map.copy()
        for bridge_lib in self._bridge_libs:
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                bridge_lib, json_file_name
            )
            if json_path.is_file():
                with open(json_path, "r") as f:
                    m: dict = json.load(f)
                for _type, obj in m.items():
                    required_import = calc_required_py_import(obj)
                    if _type in ret:
                        if required_import in ret[_type]:
                            print(
                                f"warning: {
                                    warning_fn(
                                        bridge_lib,
                                        f'{_type}{calc_imp_str(required_import)}',
                                    )
                                }"
                            )
                        ret[_type].add(required_import)
                    else:
                        ret[_type] = {required_import}
        return ret
