import json
from typing import Callable
from pathlib import Path

from compy_cli.src.transpiler.maps.util.util import MapsCltrAlgoDeps
from compy_cli.src.transpiler.module.d_types import (
    PySpecificImport,
)
from compy_cli.src.transpiler.maps.util.util import (
    calc_imp_str,
    calc_required_py_import,
)


class MapCltr2:
    def __init__(self, d: MapsCltrAlgoDeps):
        self._d = d

    def calc_map_2(
        self,
        default_map: dict[str, set[PySpecificImport | None]],
        json_file_name: str,
        warning_fn: Callable[[str, str], str],
    ) -> dict[str, set[PySpecificImport | None]]:
        ret = default_map.copy()
        for installed_library in self._d.installed_bridge_libs:
            json_path: Path = self._d.bridge_json_path_cltr.calc_bridge_json(
                installed_library, json_file_name
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
                                        installed_library,
                                        f'{_type}{calc_imp_str(required_import)}',
                                    )
                                }"
                            )
                        ret[_type].add(required_import)
                    else:
                        ret[_type] = {required_import}
        return ret
