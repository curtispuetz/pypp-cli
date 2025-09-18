from collections.abc import Callable
from dataclasses import dataclass
import json
from pathlib import Path

from pypp_cli.src.transpilers.library.transpiler.d_types import PySpecificImport
from pypp_cli.src.transpilers.library.transpiler.maps.util.util import (
    MapCltrAlgo,
    calc_imp_str,
    calc_required_py_import,
)


@dataclass(frozen=True, slots=True)
class MapCltr2Helper(MapCltrAlgo):
    type Map = dict[str, set[PySpecificImport | None]]
    _default_map: Map
    _json_file_name: str
    _warning_fn: Callable[[str, str], str]

    def calc(self) -> Map:
        ret = self._default_map.copy()
        for lib, has_bridge_jsons in self._libs.items():
            if not has_bridge_jsons:
                continue
            json_path: Path = self._bridge_json_path_cltr.calc_bridge_json(
                lib, self._json_file_name
            )
            if not json_path.is_file():
                continue
            self._calc_for_lib(json_path, lib, ret)
        return ret

    def _calc_for_lib(self, json_path: Path, lib: str, ret: Map):
        with open(json_path, "r") as f:
            m: dict = json.load(f)
        for k, v in m.items():
            required_import = calc_required_py_import(v)
            if k in ret:
                if required_import in ret[k]:
                    print(
                        f"warning: {
                            self._warning_fn(
                                lib,
                                f'{k}{calc_imp_str(required_import)}',
                            )
                        }"
                    )
                ret[k].add(required_import)
            else:
                ret[k] = {required_import}
